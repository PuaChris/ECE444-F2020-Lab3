from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

import re
from datetime import datetime

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Email

def validate_uoft_email_domain(email):
  domain = re.search("@[\w.]+", email)
  if domain.group() == "@mail.utoronto.ca":
    return True
  else:
    return False

class NameForm(Form):
  name = StringField('What is your name?', validators=[Required()])
  email = EmailField('What is your UofT Email address?', validators=[Required(), Email()])
  submit = SubmitField('Submit')  


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

boostrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET','POST'])
def index():
  name = None
  email = None
  isUoftEmail = False
  form = NameForm()
  
  
  if form.validate_on_submit():
    old_name = session.get('name')
    old_email = session.get('email')
    
    if old_name is not None and old_name != form.name.data:
      flash('Looks like you changed your name!')
    
    if old_email is not None and old_email != form.email.data:
      flash('Looks like you changed your email!')

    isUoftEmail = validate_uoft_email_domain(form.email.data)
      
    session['name'] = form.name.data
    session['email'] = form.email.data
    session['isUoftEmail'] = isUoftEmail
    
    return redirect(url_for('index'))
  
  return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'), isUoftEmail = session.get('isUoftEmail'))

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500

if __name__ == '__main__':
  app.run(debug=True)