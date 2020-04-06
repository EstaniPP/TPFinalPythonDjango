Proyecto final para la materia optativa "Taller de Python y Aplicaciones" el cual consiste en una aplicacion web hecha en el framework django.

Es una aplicacion muy sencilla en la cual se muestra como se integran los archivos HTML al framework, como se realizan las transiciones entre las paginas web utilizando los componentes url.py y views.py provistos por el framework asi como tambien se muestra como se realiza el envio de mails desde un mail creado solo para el proyecto y la configuracion que se realiza desde el archivo settings.py tambien provisto por el framework. Todos los archivos html se encuentran en la carpeta templates.

La aplicacion provee una pagina principal en la cual se tienen dos botones que llevan a las paginas de registrarse o a la seccion de ha perdido su contraseña. Ambas paginas tienen un formulario HTML el cual una vez llenado y confirmado enviara un mail a la casilla de correo que se haya ingresado en el formulario avisando que operacion realizo.

Cabe aclarar que las operaciones no son reales porque no se llego a trabajar con una base de datos ni con un modelo en particular ya que no fue parte de la consigna, por lo que los mail que lleguen al usuario seran solo mails informativos. 

Nota: la aplicacion fue desarrollada con python 3 y DJango 3.0.5 por lo que si se utilizan versiones anteriores del mismo puede que no funcione correctamente.

Nota 2: para probar la aplicacion se debe parar en la carpeta del proyecto y correr el comando "python manage.py runserver" en la consola se especificara cual es la direccion IP y el puerto de acceso(por defecto es la 127.0.0.1).
