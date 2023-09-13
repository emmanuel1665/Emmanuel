import os
import uuid

from math import ceil

from io import BytesIO

from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for 

from sqlalchemy import or_
from sqlalchemy import and_

from flask_session import Session

#importasiones para la base
from database import Database
from database import engine

from database import get_db_session



from werkzeug.utils import secure_filename
from datetime import datetime

import uuid

import models



SECRET_KEY = 'dmo5S4DxuD^9IWK1k33o7Xg88J&D8fq!'
app = Flask(__name__)
app.config.from_object(__name__)
#crear al base
Database.metadata.create_all(engine)
Session(app)

@app.get('/')
def index():
    return render_template("index.html")

@app.get('/formulario')
def registro():

    return render_template('registros.html')

@app.post('/formulario')
def formulario_form():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    cct = request.form['cct']
    email = request.form['email']
    carreras = request.form['carreras']

    db_session = get_db_session()

    nuevo_registro = models.Unidades(
        nombre = nombre,
        direccion = direccion,
        cct = cct,
        email = email,
        carreras = carreras)
    
    db_session.add(nuevo_registro)
    db_session.commit()
    db_session.refresh(nuevo_registro)
    #flash('Horas registradas exitosamete!!.')
    return render_template('registros.html')

@app.get('/registros_unidad')
def registrosUnidad():

    db_session =get_db_session()
    unidades = db_session.query(models.Unidades).all()

    return render_template('unidades.html',unidades=unidades)

@app.get('/modificarUnidad/<id>')
def modificarfun(id):
    db_session = get_db_session()
    unidades = db_session.query(models.Unidades).get(id)
 
    
    return render_template('modificar.html', unidades=unidades)


@app.post('/modalidades/<id>/update')
def form_unidad_actualizar(id):
    
    db_session = get_db_session()
    unidades = db_session.query(models.Unidades).get(id)
    

    nombre = request.form['nombre']
    direccion = request.form['direccion']
    cct = request.form['cct']
    email = request.form['email']
    carreras = request.form['carreras']

    if nombre != None and nombre != "":
        unidades.nombre = nombre
    if direccion != None and direccion != "":     
        unidades.direccion = direccion
    if cct != None and cct != "": 
        unidades.cct = cct
    if email != None and email != "": 
        unidades.email = email
    if carreras != None and carreras != "":  
        unidades.carreras = carreras

    db_session.add(unidades)
    db_session.commit()
    
    #return render_template('unidades.html')
    return redirect(url_for('registrosUnidad'))

@app.get('/catalogo')
def catalogo():

    return render_template('catalogo.html')



if __name__ == '__main__':
    app.run('0.0.0.0',port=8080, debug=True)