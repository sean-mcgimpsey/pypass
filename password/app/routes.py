from app import app, db
from app.forms import PasswordForm
from flask import render_template, flash, redirect, url_for, request, g
from app.forms import passwordGen

@app.route('/', methods=('GET', 'POST'))
def index():
    form = PasswordForm()
#    if form.generate_pass: 
#        securestring = passwordGen()
#        return render_template('index.html', form=form, securestring=securestring)
    if form.validate_on_submit():
        return redirect(url_for('password'))
#        db.hset(name="TEST", key="TESTING", value=form.password)
#        db.expire(name="TESTING", time=60)
    print(form.errors)
    return render_template ('index.html', form=form)


app.route('/password')
def password():
    return render_template('password.html')