from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import owner, pet 

@app.route('/pets')
def pets():
    owners = owner.Owner.get_all()
    print(pets)
    return render_template("pets.html", owners = owners)

@app.route('/pets/create', methods=['POST'])
def create_pet():
    pet.Pet.save(request.form)
    return redirect('/')