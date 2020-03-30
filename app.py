import os
from flask import Flask, request, render_template


app = Flask(__name__)

# defining url and function powiazana z nim
@app.route("/")
def home():
    return "Hello World!"


@app.route("/about")
def about():
    return "<h1>Hello, we are the Devs!</h1><p>We are using Flask to make web apps</p>"


@app.route("/monday")
def monday():
    return render_template("monday.html")


@app.route("/tuesday")
def tuesday():
    return render_template("tuesday.html", title="Tuesday", header="Tuesday", weather="It is snowing")


@app.route("/wednesday")
def wednesday():
    return render_template("wednesday.html", banana="I ate banana for breakfast")


@app.route("/thursday")
def thursday():
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render_template("thursday.html", title="Week", week_days=week_days)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)


