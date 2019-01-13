"""
class readFromFile:
    
    def __init__(self):
        self.fileContents = []

    def readFile(self, fileName):
        try:
            f = open(fileName, "r")
        except:
            raise Exception("file does not exist or something")
        self.fileContents = f.readlines()
        return self.fileContents

"""

def readFromFile(path_to_file):
    infile = open(path_to_file, "r")
    line = infile.readline()
    return line