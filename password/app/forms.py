from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import random 
import string


from flask import Flask, render_template
app = Flask(__name__)
 

def stringGen(stringLength=12, characters="printable"):
    chars = getattr(string, characters)
    return ''.join(random.choice(chars) for i in range(stringLength))



class PasswordForm(FlaskForm):
    securestring = stringGen()
    password = StringField('Password', validators=[
        DataRequired(), 
        Length(min=12, message=('Password does not meet requirements.'))
    ])
    generate_pass = SubmitField('Generate secure password')
    submit = SubmitField('Generate Link')

