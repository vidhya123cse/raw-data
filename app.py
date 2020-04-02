from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.oracle import BLOB



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer,primary_key=True , autoincrement=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(15),nullable=False)
    type = db.Column(db.String(15),nullable=False)

    def __init__(self,username,password,type):
        self.username=username
        self.password=password
        self.type=type
class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    
class Authority(db.Model):
    __tablename__ = 'Authority'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(50))
    job = db.Column(db.String(50))
    proof=db.Column(db.BLOB)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,usr_name,fname,lname,phone,mail,job,proof):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.job=job
        self.proof=proof    

class Ordinary(db.Model):
    __tablename__ = 'Ordinary'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(20))
    state = db.Column(db.String(20))
    city = db.Column(db.String(20))
    proof=db.Column(db.BLOB)
    address=db.Column(db.String(50))
    zip = db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,usr_name,fname,lname,phone,mail,state,city,address,zip,proof):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.job=job
        self.proof=proof    
        self.state=state
        self.city=city
        self.zip=zip


@app.route('/')
def third():
    return 'd0ne'





if(__name__ == "__main__"):
    db.create_all()
    app.run(debug=True)
    