import os
import sys

class Rearrange():
    def __init__(self, SOURCE, DESTINATION):
        self.SOURCE = SOURCE
        self.DESTINATION = DESTINATION
        self.Folders = {"Document": ["docx", "pdf", "doc"],
                        "Images": ["png", "jpg", "jpeg", "gif"],
                        "Videos": ["mp4", "mkv", "mpeg"],
                        "Compressed": ["zip", "rar"],
                        "Executable": ["exe", "sh", "deb"]}

    def checkPath(self, path):
        return os.path.exists(path)
    
    def createDirectory(self, path):
        os.system("mkdir " + path)
    
    def moveFiles(self, path, fileType):
        os.system("mv " + self.SOURCE + "/*." + fileType + " " + path)
    
    def arrange(self):
        for folder in self.Folders:
            for fileType in self.Folders[folder]:
                print(fileType + "  is Arranging in " + folder)
                if self.checkPath(self.DESTINATION+"/"+folder):
                    self.moveFiles(self.DESTINATION+"/"+folder, fileType)
                else:
                    self.createDirectory(self.DESTINATION+"/"+folder)
                    self.moveFiles(self.DESTINATION+"/"+folder, fileType)


if __name__ == "__main__":
    args = sys.argv
    obj = Rearrange(args[-2], args[-1])
    obj.arrange()