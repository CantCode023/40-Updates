from flask import Flask, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/get_version")

@app.route('/add_version', methods=["POST"])
def add_version():
    version = request.args.get("version", type=str)
    with open('db.json', 'r') as f:
        json_obj = json.load(f)
    json_obj['versions'].append(version)
    with open('db.json', 'w') as f:
        json.dump(json_obj, f)
    with open('db.json', 'r') as f:
        tags = ""
        for i in json.load(f)['versions']:
            tags += f"<p>{i}</p>"
        return tags

@app.route("/get_version", methods=["GET"])
def get_version():
    with open('db.json', 'r') as f:
        tags = ""
        for i in json.load(f)['versions']:
            tags += f"<p>{i}</p>"
        return tags