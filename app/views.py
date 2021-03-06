from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from app import viewValues as vv

@app.route('/')
@app.route('/index')

def index():
    return render_template(vv.template['index'],
                           title=vv.title['index'],
                           user=vv.dummyUser,
                           posts=vv.posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])