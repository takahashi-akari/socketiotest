import socketio
import uvicorn

# create a Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi')

# create a Socket.IO ASGI application
app = socketio.ASGIApp(sio)

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

# receive a message from a client
@sio.event
def message(sid, data):
    print('message: ', data)

# start the Socket.IO server
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="error")
