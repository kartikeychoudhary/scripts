import os
import requests
import flask
import json
from flask import jsonify
from flask import make_response
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'+os.getcwd() + \
    '//database.db'

db = SQLAlchemy(app)

class Active(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50))

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50))
    device = db.Column(db.Integer)
    name = db.Column(db.String(50))
    group = db.Column(db.String(50))

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50))
    memeber = db.Column(db.String(1000))

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    d_type = db.column(db.String(10))
    tag = db.Column(db.String(50))

def checkTag(tag):
    device = Device.query.all()
    for d in device:
        if tag == d.tag:
            return True
    
    return False
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    a = {'response': 200, 'status': 'OK'}
    return jsonify(a)
    
@app.route('/register', methods=['POST'])
def register():
    content = request.json
    username = content['username']
    password = content['password']
    device = int(content['device'])
    name = content['name']
    temp = username+password+"kc"
    tag = hashlib.md5(temp.encode())
    tag = tag.hexdigest()
    if(checkTag(tag)):
        j = '{"response":'+str(422)+', "status":"user already exists,"tag":'+tag+'}'
    else:
        obj = Device(tag=tag, device=device, name=name, group="nil")
        db.session.add(obj)
        db.session.commit()
        j = '{"response":'+str(202)+', "status":"user registered","tag":'+tag+'}'
    
    return jsonify(j)

@app.route('/status' ,methods=['POST','GET'])
def status():
    if request.method == 'GET':
        active = Active.query.all()
        temp = []
        for a in active:
            tag = a.tag
            t = {'tag':tag}
            temp.append(t)
        
        json = {'response':202,'count':len(temp),'active':temp}
    elif request.method == 'POST':
        content = request.json
        tag = content['tag']
        for a in active:
            if tag == a.tag:
                json = {'response':202, 'active':True}
                break
        json = {'response':202, 'active':False}
        
    return jsonify(str(json))

if __name__ == '__main__':
    app.run(debug=True)
