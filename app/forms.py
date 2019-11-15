from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import random 
import string





def passwordGen(stringLength=12):
    chars = string.printable
    return ''.join(random.choice(chars) for i in range(stringLength))

class PasswordForm(FlaskForm):
    securestring = passwordGen()
    password = StringField('Password', validators=[
        DataRequired(), 
        Length(min=12, message=('Password does not meet requirements.'))
    ])
    #generate_pass = SubmitField('Generate secure password')
    submit = SubmitField('Generate Link')

