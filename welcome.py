from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/welcome")
def welcome():
    return "<h1>Welcome to the Bulletin! </h1>"