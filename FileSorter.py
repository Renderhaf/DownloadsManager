import SystemManager as sysman
import json


class FileSorter():
    def __init__(self, path):
        self.path = path

        with open("settings.json", "r") as f:
            self.settings = json.loads(f.read())
        
    def sortInFolders(self):
        fileList = sysman.getFilesFromFolder(self.path)

        for fileNumber, fileName in enumerate(fileList):
            extension = sysman.getFileExtension(fileName)
            folderName = sysman.getFolderName(extension, self.settings)
            if (folderName == "WORKFILE"):
                print("{} is still downloading, skipping that one".format(fileName))
                continue
            
            folderStatus = sysman.makeFolder(self.path + "\\" + folderName)
            if (folderStatus):
                print("Working on {}, creating {} folder".format(fileName, folderName))
            else:
                print("Working on {}, placing in {} folder".format(fileName, folderName))

            sysman.moveFile(self.path + "\\" + fileName, self.path + "\\" + folderName + "\\" + fileName)

            print("Finished file {} out of {}".format(fileNumber+1, len(fileList)))

