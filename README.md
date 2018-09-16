DEPENDENCIAS INSTALADAS EN ENTORNO VIRTUAL:

    Ejecutar en una terminal en el directorio del proyecto el siguiente
    comando, de esta forma dispondrá de todas las dependencias necesarias:
        $ source env/bin/activate

TESTS:

    Tanto en el directorio de API como WEBAPP hay un script que permite testear
    algunas funciones de los respectivos proyectos. Esto es util para asegurar
    que todo funciona si se ha realizado algun cambio.
        Ejecutar mediane:
            $ python3 test_api.py
            $ python3 test_web.py


API (flask)

    Esta Api dispone de una apikey para hacer peticiones a la api de 
    openweathermap  y así obtener los datos metereológicos necesarios. En
    futuras modificaciones se puede contemplar poner la apiKey en un archivo
    de configuración

    Para arrancar la Api, ejecutar en una terminal con virtual env activo
    el siguiente comando:
        $ python3 api.py

    Para probar el resultado de la misma, abrir un navegador y insertar:
        http://localhost:5000/city_weather/Palma


WEBAPP (flask)

    Esta aplicación web consume la API descrita mas arriba. Esta dispuesta en
    el puerto 80. En el código podemos observar como las rutas en flask se 
    utilizan con decoradores.
    
    Para poner en marcha la aplicació web, ejecutamos en una terminal con el 
    virtual env activo, el siguiente comando:
        $ sudo python3 web_app.py 

    En un navegador podemos acceder a la siguiente ruta y ver su funcionamiento:
        http://0.0.0.0/dayman_weather/inca


SCRIPT (python3)
    
    Este script hace una petición al web service anterior, y muestra por
    pantalla    una frase indicando la temperatura que hará el dia siguiente en
    una ciudad dada.

    Para ejecutarlo, escribir en una terminal:
        $ python3 script.py nombre_de_ciudad

        Si la ciudad dispone de un nombre compuesto, separarla mediante guion
        bajo.


NOTA: cada ejecutable tiene que ser arrancado en una terminal distinta
