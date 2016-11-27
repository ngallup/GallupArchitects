import re

class Job(object):
    
    def parseHeaders(self, jobtext):
        '''Extract header information'''
        contentDict = {}
        
        # Might be good to generalize more at a later point
        title = ['title', re.search(r'\s*<jobtitle>\s*(.*?)\s*<', 
                                    jobtext, 
                                    re.I | re.S)]
        summary = ['summary', re.search(r'\s*<summary>\s*(.*?)\s*<', 
                                        jobtext, 
                                        re.I | re.S)]
        reqs = ['reqs', re.search(r'\s*<requirements>\s*(.*?)\s*<', 
                                  jobtext, 
                                  re.I | re.S)]
        skills = ['skills', re.search(r'\s*<skills>\s*(.*?)\s*<', 
                                      jobtext, 
                                      re.I | re.S)]
        special = ['special', re.search(r'\s*<special>\s*(.*?)\s*<', 
                                        jobtext, 
                                        re.I | re.S)]
        
        contList = [title, summary, reqs, skills, special]
        for header, cont in contList:
            try:
                contentDict[header] = cont.group(1)
            except:
                break
            
        return contentDict
                
    def __init__(self, jobfile):
        '''Do everything and populate dictionary'''
        self.jobfile = jobfile
        self.contents = {}
        
        text = ''
        with open(jobfile, 'r') as infile:
            text = infile.read()
            
        self.contents = self.parseHeaders(text)
            
        