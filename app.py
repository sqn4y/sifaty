from datetime import datetime

from flask import Flask, render_template

from data.navigation import NAVIGATION
from data.rules import RULES
from data.lessons import LESSONS

app = Flask(__name__)

@app.context_processor
def inject_globals():

    return {
        "navigation": NAVIGATION,
        "current_year": datetime.now().year,
    }

@app.route("/")
def home():

    return render_template(
        "index.html",
        lessons=LESSONS,
    )

@app.route("/rules")
def rules():

    return render_template(
        "rules.html",
        rules=RULES,
    )

@app.route("/sifaty")
def sifaty():
    return render_template(
        "sifaty.html",
        rules=RULES
    )


@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):

    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)