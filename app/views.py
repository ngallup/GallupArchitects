from flask import render_template
from app import app
from app import Job
import os

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
    # Read contents of all job text files
    basedir = os.path.abspath(os.path.dirname(__file__))
    jobdir = os.path.join(basedir, 'jobs')
    jobfiles = os.listdir(jobdir)
    jobfiles.remove('example.txt') # Remove example file from list
    jobfiles = [os.path.join(jobdir, job) for job in jobfiles]

    # Inovoke Job class for cleanliness
    jobs = [Job(jobfile) for jobfile in jobfiles]
    #for job in jobfiles:
    #    with open(job, 'r') as infile:
            
    
    return render_template('careers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')