from flask import render_template
from app import app
from app import Job
from app import project
import os

basedir = os.path.abspath(os.path.dirname(__file__))

contact = {
     'name': 'Timothy Gallup',
     'phone': '(918) 553-0625',
     'addr1': '555 S. Blah Ave',
     'addr2': 'Tulsa, OK 55555',
     'comp': 'Gallup Architects Pllc'
 }

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html',
                           contact=contact)
    
projectdir = os.path.abspath(os.path.join(os.path.join(basedir, 'static'), 'projects'))
subdirs = [os.path.join(projectdir, subdir) for subdir in os.listdir(projectdir)]
projectlist = [project.Project(subdir) for subdir in subdirs]
    
    
@app.route('/projects')
def projects():
    return render_template('projects.html',
                           contact=contact,
                           proj=projectlist)    

@app.route('/team')
def team():
    return render_template('team.html',
                           contact=contact)


@app.route('/careers')
def careers():
    '''Should read text files in a jobs folder with description,
    requirements, etc. and populate a side toolbar with each of these
    fields
    '''
    # Get list of all job descriptor files
    basedir = os.path.abspath(os.path.dirname(__file__))
    jobdir = os.path.join(basedir, 'jobs')
    jobfiles = os.listdir(jobdir)
    #jobfiles.remove('example.txt') # Remove example file from list
    jobfiles = [os.path.join(jobdir, job) for job in jobfiles]
        
    # Inovoke Job class for cleanliness and remove empty contents
    jobs = [Job.Job(jobfile) for jobfile in jobfiles]
    jobs = list(filter(lambda job: job.contents, jobs))     
                
    # Careers will need to react dynamically to job list
    return render_template('careers.html',
                           contact=contact,
                           joblist=jobs)


@app.route('/contact')
def contactus():
    return render_template('contact.html',
                           contact=contact)