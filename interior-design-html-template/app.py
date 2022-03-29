from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login.html")
def login():
    return render_template("login.html")
@app.route("/addcourse.html")
def addcourse():
    return render_template("addcourse.html")
@app.route("/addDepartment.html")
def addDepartment():
    return render_template("addDepartment.html")
@app.route("/addSubject.html")
def addSubject():
    return render_template("addSubject.html")
app.run(debug="True",port=5067)

