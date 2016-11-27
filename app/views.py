from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def homepage():
    contact = {
        'name': 'Timothy Gallup',
        'phone': '(918) 553-0625',
        'addr1': '555 S. Blah Ave',
        'addr2': 'Tulsa, OK 55555',
        'comp': 'Gallup Architects Pllc'
    }
    
    return render_template('home.html',
                           contact=contact)
    
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/careers')
def careers():
    '''Should read text files in a jobs folder with description,
    requirements, etc. and populate a side toolbar with each of these
    fields
    '''
    return render_template('careers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')