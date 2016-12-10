import os
import string

class Project(object):
    '''
    The Project class holds data pertaining to past and current
    architecture projects.  It reads a text file from its current
    directory and keeps a list of all associated images by virtue of
    existing in the same directory.  To be used for dynamic generation
    of slideshows for showing off a portfolio
    '''
    def __init__(self, projectfolder):
        self.data = {}
        
        description, images, paths = self.getFiles(projectfolder)
        self.data['longtext'] = description
        self.data['shorttext'] = self.truncate_body(description, 200)
        self.data['images'] = images
        self.data['paths'] = paths
        self.data['folder'] = os.path.basename(projectfolder)
        
    def getFiles(self, projectfolder):
        '''
        Get list of files under the specified project folder including
        description.txt and all images for potential slideshow
        '''
        text = ''
        imgformats = ('.jpg', '.jpeg', '.gif', '.png' )
        
        filelist = os.listdir(projectfolder)
        filepaths = [os.path.join(projectfolder, f) for f in filelist]
        
        with open(os.path.join(projectfolder, 'description.txt'), 'r') as descrFile:
            text = descrFile.read()
            
        images = list(filter(lambda x: x.lower().endswith(imgformats), filelist))
        return text, images, filepaths
    
    def truncate_body(self, text, numchars):
        '''
        Return truncated body of text such that no words are half
        displayed
        '''
        subtext = text[:numchars]
        if subtext[-1] in string.whitespace: # Return 1 less if whitespace
            return subtext[:-2] + "..."
        elif subtext[-1] in string.punctuation: # Return if period, etc.
            return subtext
        else:
            return self.truncate_body(subtext, numchars-1)