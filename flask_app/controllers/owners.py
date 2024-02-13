from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.owner import Owner 

@app.route('/')
def index():
    return redirect ('/owners')

@app.route('/owners')
def owners():
    owners = Owner.get_all()
    print(owners)
    return render_template("home.html", all_owners = owners)

@app.route('/owners/create',methods=['POST'])
def create_owner():
    Owner.save(request.form)
    return redirect('/owners')

@app.route('/owners/<int:id>')
def view(id):
    data ={
        "id":id
    }
    return render_template("owners.html", owner=Owner.get_one_pets(data))