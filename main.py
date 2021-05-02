from flask import Flask, render_template
import logic


app = Flask(__name__)


@app.route("/")
def home():
    output = logic.search(day="one_day_str", age=45, availablilty=1)
    # print(type(output))
    return render_template("index.html", output=output)


@app.route("/18")
def teen():
    output = logic.search(day="one_day_str", age=18, availablilty=0)
    # print(type(output))
    return render_template("index.html", output=output)


@app.route("/45")
def adult():
    output = logic.search(day="one_day_str", age=45, availablilty=1)
    # print(type(output))
    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
