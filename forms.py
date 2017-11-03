from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email, Length,
                                EqualTo)

from model import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exist')

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exist')
class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Regexp(r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, ""numbers, and underscore only.")
            ),
            name_exists
        ])
    email = StringField('Email', validators=[ DataRequired(), Email(),  email_exists ])
    password = PasswordField('password', validators=[ DataRequired(),Length(min=4),
           EqualTo('password2', message='Password must much!')
       ])
    password2 = PasswordField( 'Confirm Password', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired])

class PostForm(FlaskForm):
    content = TextAreaField("What's up?", validators=[DataRequired()])
