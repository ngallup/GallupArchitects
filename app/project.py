import os

class Project(object):
    def __init__(self, projectfolder):
        self.data = {}
        
        description, images, paths = self.getFiles(projectfolder)
        self.data['longtext'] = description
        self.data['shortext'] = self.data['longtext'][:400] + "..."
        self.data['images'] = images
        self.data['paths'] = paths
        self.data['folder'] = os.path.basename(projectfolder)
        
    def getFiles(self, projectfolder):
        text = ''
        imgformats = ('.jpg', '.jpeg', '.gif', '.png' )
        
        filelist = os.listdir(projectfolder)
        filepaths = [os.path.join(projectfolder, f) for f in filelist]
        
        with open(os.path.join(projectfolder, 'description.txt'), 'r') as descrFile:
            text = descrFile.read()
            
        images = list(filter(lambda x: x.lower().endswith(imgformats), filelist))
        return text, images, filepaths