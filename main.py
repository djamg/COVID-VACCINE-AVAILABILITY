from flask import Flask, render_template, request
import logic
import datetime
from datetime import timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dateutil.tz import gettz
import json


# Use a service account
cred = credentials.Certificate(
    'F:\Programming\COWIN API\static\cowin-vaxify-firebase-adminsdk-unuxn-092e83f077.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


date_object = datetime.date.today()
current_day_str = date_object.strftime("%d-%m-%Y")
# print(current_day_str)

one_day = date_object + timedelta(days=1)
one_day_str = one_day.strftime("%d-%m-%Y")
# print(one_day.strftime("%d-%m-%Y"))

two_day = date_object + timedelta(days=2)
two_day_str = two_day.strftime("%d-%m-%Y")
# print(two_day.strftime("%d-%m-%Y"))

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        # output = request.form['email'] + \
        #     request.form['age'] + request.form['day']
        # print(str(output))
        db.collection(u'users').add({
            u'email': request.form['email'],
            u'age': request.form['age'],
            u'day': request.form['day'],
            u'timestamp': datetime.datetime.now(tz=gettz('Asia/Kolkata'))
        })

        availability = 1
        age = 45

        if request.form['age'] == "18":
            availablilty = 0
        elif request.form['age'] == "45":
            availablilty = 1
        if request.form['day'] == "TODAY":
            day = current_day_str
        elif request.form['day'] == "TOMORROW":
            day = one_day_str
        elif request.form['day'] == "DAY AFTER":
            day = two_day_str

        # print(request.form['day'])
        # print(day)
        output = logic.search(day=day, age=int(
            request.form['age']), availablilty=availablilty)
        # print(type(json.loads(output)))
        # print(output)
        return render_template("index.html", output=json.loads(output))


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('index.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
