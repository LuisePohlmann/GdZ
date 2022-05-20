from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from app.config import Config
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired
import app.blog as blog
import app.termin as termin
import pandas as pd
import datetime

app = Flask(__name__)
app.config.from_object(Config)

class AddEmail(FlaskForm):
    Name = StringField('Name', validators=[InputRequired() ])
    E_Mail = StringField("Email Adresse")


format_str = '%d.%m.%Y'
for i in blog.Posts:
     i["Date"] = datetime.datetime.strptime(i["date"], format_str)
blog.Posts.sort(key=lambda item:item['Date'], reverse=True)


@app.route("/")
@app.route("/Home")
def home():
    return render_template("Home.html", articles = blog.Posts, Termine = termin.Termine)

@app.route("/Projekte")
def projekte():
    return render_template("Projekte.html")

@app.route("/Waldgarten")
def waldgarten():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "Waldgarten":
            articles.append(i)
    return render_template("Waldgarten.html", articles = articles)

@app.route("/Luecelium")
def luecelium():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "Luecelium":
            articles.append(i)
    return render_template("Luecelium.html", articles = articles)

@app.route("/vert_farming")
def vert_farming():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "vertical_farming":
            articles.append(i)
    return render_template("vert_farming.html", articles = articles)

@app.route("/Kunterbunt")
def kunterbunt():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "Kunterbunt":
            articles.append(i)
    return render_template("Kunterbunt.html", articles = articles)

@app.route("/soz_Begegnung")
def soz_Begegnung():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "soziale Begegnung":
            articles.append(i)
    return render_template("soz_Begegnung.html", articles = articles)

@app.route("/Algen")
def algen():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "Algen":
            articles.append(i)
    return render_template("Algen.html", articles = articles)

@app.route("/Weihnachtspilze")
def weihnachtspilze():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "Weihnachtspilze":
            articles.append(i)
    return render_template("Algen.html", articles = articles)

@app.route("/Kraeutergarten")
def kraeuter():
    articles = []
    for i in blog.Posts:
        if i["Kategorie"] == "Kräutergarten":
            articles.append(i)
    return render_template("Kraeutergarten.html", articles = articles)

@app.route("/Unterstuetzen")
def unterstuetzen():
     return render_template("Unterstuetzen.html")

@app.route("/Mitmachen",  methods=["POST", "GET"])
def mitmachen():
    form = AddEmail()
    return render_template("Mitmachen.html", form = form)

@app.route("/Kooperationen")
def kooperation():
    return render_template("Kooperationen.html")

@app.route("/Spenden")
def spenden():
    return render_template("Spenden.html")

@app.route("/Galerie")
def galerie():
    return render_template("Galerie.html", articles = blog.Posts)

@app.route("/About")
def Me():
    return render_template("About.html")


@app.route("/FAQ")
def faq():
    return render_template("FAQ.html")

@app.route("/Impressum")
def impressum():
    return render_template("Impressum.html")

@app.route("/Kontakt")
def kontakt():
    return render_template("Kontakt.html")
