from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Index page"""
    return "Hello world"


@app.route("/temperature")
def temperature():
    """Show temperature info"""
    return "Temperature"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
