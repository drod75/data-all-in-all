from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/data-cleaning')
def data_cleaning():
    return render_template('cleaning.html')

@app.route('/data-processing')
def data_processing():
    return render_template('processing.html')