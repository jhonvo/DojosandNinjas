from dojoninja_app import app
from flask import Flask, render_template, request, redirect, session
from dojoninja_app.models import dojos
from dojoninja_app.models.ninjas import Ninja


@app.route('/ninja/new', methods=['GET','POST'])
def newninja():
    dojolist = dojos.Dojo.get_dojos()
    return render_template('/createninja.html', dojolist = dojolist)

@app.route('/ninja/create', methods=['POST'])
def createninja():
    data = request.form
    newninja = Ninja.new_ninja(data)
    dojoid = f"/dojo/{data['dojo_id']}"
    return redirect (dojoid)

