import os

from flask import Flask, render_template, request, session
from sqlalchemy import create_engin
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine  =  create_engin(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine)) 

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")
