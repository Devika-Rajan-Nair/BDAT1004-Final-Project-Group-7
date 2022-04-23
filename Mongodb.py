from flask import Flask,jsonify,request,render_template
import flask
import pandas as pd
from pymongo import MongoClient

app = flask.Flask(__name__)

client = MongoClient("mongodb+srv://sahet74736:Password123@cluster0.mlv1d.mongodb.net/Test_DB?retryWrites=true&w=majority")
db=client.get_database("Test_DB")
records=db.Test_Collection
#@app.route("/")
#def home():
    
   
Test_Collection = db.Test_Collection.find()
df = pd.DataFrame(Test_Collection)
print (df)
#print (flask.jsonify([collecti for collecti in Test_Collection]))



