# Importar las librerias y funciones 
from flask import Flask, render_template 
import requests # permite hacer pedidos a la API

# Creamos una aplicacion de Flask sobre el programa app.py 
app = Flask(__name__)
      
# Creacion de rutas 
@app.route("/tarjeta") # cuando se abra esta ruta en el navegador...  
def index (): # ... ejecutame esta funcion, porfa 
    nombre = 'Pablito Pinguino'
    especie = 'Pinguino'
    color = 'Azul'

    # Llamar a la funcion render_template para construit index.html
    return render_template("index.html", nombre=nombre, especie=especie, color=color)

# Crear una nueva ruta para el proyecto
@app.route("/consultar_personaje")
def funcion_consultar_personaje():
    # Definimos la url a la que se hace el pedido 
    url = 'https://rickandmortyapi.com/api/character/4'
    
    # Hacemos el pedido a la API -- nos devuelve un diccionario
    respuesta_api = requests.get(url).json()

    # Creamos variables a traves de acceder la respuesta
    nombre = respuesta_api['name']
    estado = respuesta_api["status"]
    imagen = respuesta_api['image']
    # print(nombre, estado)

    # Enviamos los datos al html
    return render_template('consultar_personaje.html', nombre=nombre, estado=estado, imagen=imagen)

@app.route("/")
def proyecto_final(): 
    # definir la url para la consulta 
    link = 'https://rickandmortyapi.com/api/character/'

    # consultar a la api con el link de la info que enecesitamos 
    respuesta = requests.get(link).json()

    # acceder a la lista de personajes 
    lista_de_personajes = respuesta ['results']
    
    return render_template('proyecto_final.html', lista_de_personajes=lista_de_personajes)

# cuando se corra el programa... (cuando se apriete play)
if __name__ == '__main__': 
    app.run(debug=True) 
