from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dataclasses import dataclass
from typing import Dict
import uuid
import json
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

@dataclass
class ConnectionManager:

  """
    A class to manage WebSocket connections.

    Attributes:
        active_connections (dict): A dictionary to store the active WebSocket connections.

    Methods:
        __init__(self) -> None: Initializes the ConnectionManager object.
        connect(self, websocket: WebSocket) -> None: Accepts the connection from the client and assigns a unique ID.
        send_message(self, ws: WebSocket, message: str) -> None: Sends a message to the client.
        find_connection_id(self, websocket: WebSocket) -> str: Finds the unique ID associated with the given WebSocket connection.
        broadcast(self, webSocket: WebSocket, data: str) -> None: Broadcasts a message to all active connections.
        disconnect(self, websocket: WebSocket) -> str: Disconnects the given WebSocket connection and returns its unique ID.
    """
  def __init__(self) -> None:
    self.active_connections: dict = {}

  async def connect(self, websocket: WebSocket):
    await websocket.accept()
    id = str(uuid.uuid4())
    self.active_connections[id] = websocket

    await self.send_message(websocket, json.dumps({"isMe": True, "data": "Have joined!!", "username": "You"}))

  async def send_message(self, ws: WebSocket, message: str):
    await ws.send_text(message)

  def find_connection_id(self, websocket: WebSocket):
    websocket_list = list(self.active_connections.values())
    id_list = list(self.active_connections.keys())

    pos = websocket_list.index(websocket)
    return id_list[pos]

  async def broadcast(self, webSocket: WebSocket, data: str):
    decoded_data = json.loads(data)

    for connection in self.active_connections.values():
      is_me = False
      if connection == webSocket:
        is_me = True

      await connection.send_text(json.dumps({"isMe": is_me, "data": decoded_data['message'], "username": decoded_data['username']}))

  def disconnect(self, websocket: WebSocket):
    id = self.find_connection_id(websocket)
    del self.active_connections[id]

    return id

app = FastAPI(
    title="FastAPI WebSocket Chat Application",
    description="The FastAPI WebSocket Chat Application is a real-time chat system built using FastAPI framework. "
    "It allows users to connect to a chat room via WebSocket, send messages, and receive messages instantly. The application provides a seamless user experience with features like WebSocket connection management, message broadcasting, and graceful disconnection handling. Users can join the chat room by accessing the provided endpoint and interact with other participants in real-time. Additionally, the application serves HTML templates for both joining the chat room and the chat interface, enhancing the user interface experience."
)
app.mount("/static", StaticFiles(directory="static"), name="static")
connection_manager = ConnectionManager()

@app.get("/", response_class=HTMLResponse)
def get_room(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/message")
async def websocket_endpoint(websocket: WebSocket):
  # Accept the connection from the client.
  await connection_manager.connect(websocket)

  try:
    while True:
      # Recieves message from the client
      data = await websocket.receive_text()
      await connection_manager.broadcast(websocket, data)
  except WebSocketDisconnect:
    id = await connection_manager.disconnect(websocket)
    return RedirectResponse("/")

@app.get("/join", response_class=HTMLResponse)
def get_room(request: Request):
   return templates.TemplateResponse("room.html", {"request": request})