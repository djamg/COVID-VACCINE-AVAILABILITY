from flask import Flask, render_template, request
import logicv2
import datetime
from datetime import timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dateutil.tz import gettz
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        output = logicv2.search(day="02-05-2021", age=18, availablilty=0)
        print(type(json.loads(output)))
        print(output)
        return render_template("indexv2.html", output=json.loads(output))
    elif request.method == "POST":
        pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
