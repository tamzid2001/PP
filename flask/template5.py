from flask import Flask,render_template
import markov_v2 as markov
import fileio_v1 as reader
import sengen12 as sentt
from sengen12 import *
import Rotn as rottt
from random import choice
from random import random
from random import randint

template = Flask(__name__)
@template.route('/')
def root():
    return render_template("base2.html", title = "Hi")
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
    return "sengen"
    
    
    sen = np + vp
    return render_template("sen.html", sent = sen, title = "Sengen")

@template.route("/rot/")
def rott():
    rot = rottt.rotn("hello",13)
    return render_template("rot.html", rot = rot, title = "Rot")

if __name__ == '__main__':
    template.debug == True
    template.run()
