from app import app, db
from app.forms import PasswordForm, stringGen
from flask import render_template, flash, redirect, url_for, request, g
import timedelta
import datetime

@app.route('/', methods=('GET', 'POST'))
def index():
    form = PasswordForm()
#    if form.generate_pass:
#        securestring = passwordGen()
#        return render_template('index.html', form=form, securestring=securestring)
    if form.validate_on_submit():
        generated_url = stringGen(stringLength=70, characters="ascii_letters")
        db.set(generated_url, form.password.data)
        db.expire(name=generated_url, time=60)
        return password(generated_url, form.password)
#    print(form.errors)
    else:
        return render_template('index.html', form=form)


@app.route('/password')
def password(generatedUrl, password):
        return render_template('password.html', password=password, generatedUrl=generatedUrl)

@app.route('/collect/<generatedUrl>')
def collect_password_by_url(generatedUrl):
    password=db.get(generatedUrl)
    db.expire(generatedUrl, 3)
    return render_template('collect.html', password=password)
