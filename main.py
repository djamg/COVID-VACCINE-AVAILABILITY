from flask import Flask, render_template, request
import logic
import datetime
from datetime import timedelta

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

        if request.form['age'] == "18":
            availablilty = 0
        elif request.form['age'] == "45":
            availablilty = 1
        if request.form['day'] == "TODAY":
            day = current_day_str
        elif request.form['day'] == "TOMORROW":
            day = one_day_str
        # print(request.form['day'])
        # print(day)
        output = logic.search(
            day=day, age=int(request.form['age']), availablilty=availablilty)
        # print(output)
        return render_template("index.html", output=output)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('index.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
