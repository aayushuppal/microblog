from flask import render_template
from app import app
from app import viewValues as vv

@app.route('/')
@app.route('/index')

def index():
    return render_template(vv.template['index'],
                           title=vv.title['index'],
                           user=vv.dummyUser)