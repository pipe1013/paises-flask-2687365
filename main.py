# Improtar las dependecias flask
from flask import Flask, render_template
# Crear el objeto Flask
app = Flask(__name__)
# Crear una ruta de prueba
@app.route('/Hello')
def hola():
    return 'hola'

#ruta de paises
@app.route("/paises")
def paises():
    username = 'Felipe Moreno'
#MULTI LISTAS
    continentes = [{
        'nombre': 'america',
        'poblacion' : 1036900579,
        'superficie':   42549000 ,
        'numeropaises': 35,
        'densidad': 228,
        "paises" :[
            {
                "nom" : "Colombia",
                "mon" : "Peso",
                "cap" : "Bogotá"
            },
            {
                "nom" : "Argentina",
                "mon" : "peso argentino ",
                "cap" : "Buenos Aires"    
            },
            {
                "nom" : "Chile",
                "mon" : "peso chileno",
                "cap" : "Santiago"
            }
        ]
    },
    {
        'nombre': 'Europa',
        'poblacion' : 747747395,
        'superficie':10530751 ,
        'numeropaises': 50,
        'densidad': 71,
        "paises" : [
            {
               "nom" : "Alemania",
                "mon" : "Euro",
                "cap" : "Berlin"
            },
            {
                "nom" : "Rusia",
                "mon" : "Rublo ruso",
                "cap" : "Moscú"
            }
        ]
        }]
    return render_template('paises.html', username=username, continentes=continentes)