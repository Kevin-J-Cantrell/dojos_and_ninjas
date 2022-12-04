from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.ninjas import Ninja 
from flask_app.models.dojos import Dojo

@app.route('/ninjas')
def Ninjas():
    
    return render_template("new_ninja.html",dojos=Dojo.get_all())

@app.route("/ninja/edit/<int:id>/page")
def Edit_page(id):
    data = {
        'id' : id,
        
    }
    return render_template("edit.html",ninja=Ninja.get_one(data))

@app.route("/ninja/edit/<int:dojo_id>", methods= ['POST'])
def Edit(dojo_id):

    
    Ninja.update(request.form)
    return redirect(f"/dojos/{dojo_id}/show")

@app.route('/ninjas/<int:id>/<int:dojo_id>/delete')
def Ninjas_delete(id,dojo_id):
    data = {
        'id' : id
    }
    Ninja.delete(data)
    return redirect(f'/dojos/{dojo_id}/show')


@app.route('/ninja/add', methods = ['POST'])
def Add_ninja():
    id = request.form['dojo_id']
    Ninja.create(request.form)
    return redirect(f'/dojos/{id}/show') 

