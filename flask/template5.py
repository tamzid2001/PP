from flask import Flask,render_template,request
import markov_v2 as markov
import fileio_v1 as reader
import sengen12 as sentt
from sengen12 import *
import Rotn as rottt
from random import choice
from random import random
from random import randint

USER = "p"
PASSWORD = "p"

template = Flask(__name__)
def authenticate( name, passwd ):
    return name==USER and passwd==PASSWORD
@template.route( '/' )
def root():
    return render_template( 'index.html' )
@template.route( '/login', methods = ['POST', 'GET'] )
def login_form():
    if request.method == 'GET':
        return render_template( 'index.html' )
    else:
        form_input = request.form
        u = form_input['txt_uname']
        p = form_input['pwd_upass']
    if u=='' or p=='':
        s='Please enter a username and password'
        return render_template( 'index.html', message = s)
    elif authenticate( u, p ):
        s='HuzzaaH! Access granted.'
        return render_template( 'base2.html', message = s )
    else:
        s='Access denied.'
        return render_template( 'index.html', message = s )

@template.route("/markov/")
@template.route("/markov/<source>")
def x(source = "sawyer"):
    t = ["sawyer", "sherlock", "wonderland", "war_of_the_worlds"]
    if source not in t:
        return "................"
    x = "%s.txt"%(source)
    chains = markov.generate_chains(x)
    text = markov.generate_text(chains, 100)
    return render_template("markov2.html", final = text, title = "Markov")

@template.route("/sen/")
def sent():
    return render_template("sen.html", sen = "sengen")

@template.route("/rot/")
def rott():
    rot = rottt.rotn("hello",13)
    return render_template("rot.html", rot = rot, title = "Rot")

if __name__ == '__main__':
    template.debug == True
    template.run()
