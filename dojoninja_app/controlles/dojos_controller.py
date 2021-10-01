from dojoninja_app import app
from flask import Flask, render_template, request, redirect, session
from dojoninja_app.models.dojos import Dojo

@app.route('/')
def home():
    return redirect ('/dojo')

@app.route('/dojo', methods=['GET','POST'])
def dojopage():
    dojos = Dojo.get_dojos()
    # print (dojos[0].id)
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojo/create', methods=['POST'])
def newdojo():
    data = request.form
    results = Dojo.new_dojo(data)
    return redirect ('/dojo')

@app.route('/dojo/<int:num>')
def ninjalist(num):
    list = Dojo.ninjasAtDojo(num)
    return render_template('ninjas.html', dojo=list)

