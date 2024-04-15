# FastAPI Chat Application

This is a simple chat application built with FastAPI, allowing users to join chat rooms and exchange messages in real-time using WebSocket connections.

---

### Features

- Real-time Communication: Users can join chat rooms and send messages instantly, with updates visible to all participants in real-time.
- Multiple Chat Rooms: Users can join different chat rooms, each with its own set of participants and conversations.
- Simple Interface: The user interface is designed to be intuitive and easy to use, with a clean and minimalistic design.

---

### Technologies Used

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- WebSocket: Provides full-duplex communication channels over a single TCP connection, allowing for real-time communication between the client and server.
- Jinja2 Templates: Used for rendering HTML templates to create dynamic web pages.
- Static Files: Static files (e.g., CSS, JavaScript) are served using FastAPI's StaticFiles class for enhanced frontend functionality.
- UUID: Universally Unique Identifier (UUID) is used to generate unique identifiers for WebSocket connections.
- JSON: JavaScript Object Notation (JSON) is used for exchanging messages between the client and server.
  
---

### Getting Started

1. Clone the Repository:

```python
git clone https://github.com/your_username/chat_app.git

```
2. Create a virtual environment and activate it:

```python
python -m venv venv && source venv/bin/activate

```


3. Install Dependencies:

```python
cd chat_app
pip install -r requirements.txt

```

4. Run the Application:

```python
uvicorn main:app --reload
```

5. Open the Chat Application:

Navigate to <http://localhost:8000> in your web browser to access the chat application.

---

### Usage

1. Join a Chat Room:

- Access the chat application in your web browser.
- Enter a username and join a chat room.

2. Send Messages:

- Type your message in the input field at the bottom of the chat room.
- Press Enter or click the "Send" button to send your message.

3. Leave a Chat Room:

- Close the web browser tab or navigate away from the chat application to leave the chat room.
