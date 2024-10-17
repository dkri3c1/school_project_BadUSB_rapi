from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    with open("payload.ps", "r") as f:
        result = f.read()
    return result

@app.route("/payload2")
def payload2():
    with open("payload2.ps", "r") as f:
        result = f.read()
    return result

app.run("0.0.0.0", 80, debug = False)
