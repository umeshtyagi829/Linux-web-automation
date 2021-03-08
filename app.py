from flask import Flask
from flask import render_template
from flask import request
import subprocess as sp

app = Flask("myapp")

@app.route('/')
def home():
    home = render_template("home.html")
    return home


@app.route('/form')
def form():
    name = "Umesh Tyagi"
    web = render_template("form.html")
    return web

@app.route("/menu", methods = ["GET"])
def menu():
    cmd = request.args.get("cmd")
    res = sp.getoutput(cmd)
    return "<pre>" + res + "</res>"


