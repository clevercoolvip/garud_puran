from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import pandas as pd


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///confessions.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Confession(db.Model):
    id = db.Column("ID", db.Integer, primary_key=True)
    message = db.Column("Confession", db.String(2000))

    def __init__(self, message):
        self.message = message



penalty = pd.read_csv("./penalty.csv")
punishments = penalty.iloc[:, 0].to_list()
penalty_dic = {}
 
for i in range(len(penalty)):
    penalty_dic[penalty.iloc[i, 0]] = penalty.iloc[i, 1]


@app.route("/result")
def result():
    punishment = random.choice(punishments)
    return render_template("result.html", punishment=punishment, details = penalty_dic[punishment])



@app.route("/", methods=["POST", "GET"])
def ping():
    if request.method=="POST":
        message = request.form.get("message")
        confession = Confession(message)
        db.session.add(confession)
        db.session.commit()
        return redirect(url_for("result"))


    return render_template("index.html")


if __name__=="__main__":
    db.create_all()
    app.run(debug=True, port=8080)