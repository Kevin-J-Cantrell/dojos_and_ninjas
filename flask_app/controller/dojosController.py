from flask_app import app
from flask import Flask, redirect, session, request, render_template, url_for, flash
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route("/")
def index():
    
    
    return redirect ("/dojos/home")

@app.route("/dojos/home")
def home():
    
    return render_template("index.html",dojos=Dojo.get_all())



@app.route("/dojos/<int:id>/show")
def show(id):
    data = {
        "id" :id,
        
    }
    
    return render_template("dojo_show.html",dojo=Dojo.get_one_dojo(data))


@app.route("/dojos/create", methods=["POST"])
def create_dojo():
    data = {
        'name': request.form["dojo_name"] 
    }
    Dojo.create(data)
    return redirect("/dojos/home")


@app.route("/dojos/<int:id>/delete")
def Delete(id):
    print('deleted')
    data = {
        'id' : id
    }
    Dojo.delete(data)
    print('deleted')
    return redirect("/dojos/home")

