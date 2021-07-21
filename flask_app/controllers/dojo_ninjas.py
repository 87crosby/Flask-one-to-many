from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos = dojos)

@app.route('/dojos/new_dojo', methods = ['POST'])
def new_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def go_to_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', dojos = dojos)

@app.route('/add_ninja', methods = ['POST'])
def add_ninja():
    data = {
        'dojos_id' : request.form['dojo'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    Dojo.add_ninja_to_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def dojos_ninjas(dojo_id):
    dojos = Dojo.get_ninjas_by_dojo({'id': dojo_id})
    return render_template('ninjas_in_dojo.html', dojos = dojos)