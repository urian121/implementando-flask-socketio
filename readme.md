## Implementando Flask-SocketIO 🐍

###### Construye una sala de chat en tiempo real utilizando Flask y SocketIO. Esta poderosa combinación te permite crear una aplicación web interactiva con capacidades de chat en tiempo real.

##### Paquetes necesarios

`pip install flask`
`pip install flask-socketio`

##### Generar archivo requirement.txt

`pip freeze > requirements.txt`

##### Instalar todos los paquetes del proyecto

`pip install -r requirements.txt`

### Nota

Puedes crear un entorno virtual con `virtualenv env` e instalar todos los paquetes del proyecto ejecutando ``pip install -r requirements.txt`
obvio cambiar los parametros para la conexión a BD e importar la tabla que se requiere para almacenar los mensajes de la sala de chat.

##### broadcast=True

Se utiliza al emitir un evento desde el servidor para especificar
que dicho evento debe ser transmitido a todos los clientes conectados,
excepto al cliente que generó el evento.

##### Documentación

https://flask-socketio.readthedocs.io/en/latest/index.html

### Resultado Final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/implementando-flask-socketIO-Urian-viera.PNG)

# Por favor no olvides dejar tu comentario y like en el canal 👍 ah suscríbete 😀
