from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)

@app.route("/home")
def home():
    title = "KABU CS HUB"
    return render_template("home.html", title = title)

@app.route("/news")
def news():
    return render_template("check.html", title = "Coming Soon")

@app.route("/links")
def links():
    return render_template("check.html", title = "Coming Soon")

@app.route("/sem1of1")
def sem1of1():
    return render_template("sem1-1.html", title = "Semester 1.1")

@app.route("/sem2of1")
def sem2of1():
    return render_template("sem1-2.html", title = "Semester 1.2")

if __name__ == "__main__":
    app.run(debug = True)
