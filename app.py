import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.on('message')
def my_message(sid, data):
    print('message ', data)
    sio.emit('logs ', data)


@sio.on('ping')
def ping_event(sid, data):
    print('message ', data)
    sio.emit('capture', data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
