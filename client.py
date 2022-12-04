import socketio

# create a Socket.IO Client
sio = socketio.Client()

# connect to the server
sio.connect('http://localhost:8000')

# send a message to the server
while True:
    sio.emit('message', input('Message: '))
