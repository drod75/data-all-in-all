from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'd23b5a76c202b3ab3c4d5bccf4b1d985'

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@gmail.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form, title='Home')

@app.route('/data-cleaning')
def data_cleaning():
    return render_template('cleaning.html', title='Cleaning')

@app.route('/data-processing')
def data_processing():
    return render_template('processing.html', title='Processing')