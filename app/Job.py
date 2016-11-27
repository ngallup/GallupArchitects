import re

class Job(object):
    
    def parseHeaders(self, jobtext):
        '''Extract header information'''
        pass
    
    def __init__(self, jobfile):
        '''Do everything and populate dictionary'''
        self.jobfile = jobfile
        self.contents = {}
        
        text = ''
        with open(jobfile, 'r') as infile:
            text = infile.read()
            
        