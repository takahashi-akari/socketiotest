import socketio
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

# create a Socket.IO Client
sio = socketio.Client(engineio_logger=False, logger=False, ssl_verify=False)

# connect to the server
sio.connect('https://0.0.0.0:8000')

# send a message to the server
while True:
    sio.emit('message', input('Message: '))
