from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)

# para crear una instancia de Socket.IO en una aplicación Flask
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


# Escuchar un mensaje
@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')


# Escuchando cuando el cliente se desconecta.
@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')


# escuchando por message
@socketio.on('message')
def recibirMsj(message_chat):
    print('Recibiendo mensaje: ' + message_chat)
    ''' 
    broadcast=True se utiliza al emitir un evento desde el servidor para especificar 
    que dicho evento debe ser transmitido a todos los clientes conectados, 
    excepto al cliente que generó el evento.
    '''
    emit('message', message_chat, broadcast=True)
    # emit('my response', {'data': message}, broadcast=True)


# Arrancando mi aplicacion flask y arrancando socketio tambien
if __name__ == '__main__':
    socketio.run(app, debug=True, port=5200)
