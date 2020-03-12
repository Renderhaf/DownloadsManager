import os

def getFilesFromFolder(folderPath : str):
    allChildren = os.listdir(folderPath)
    filePaths = list(filter(lambda x : os.path.isfile(folderPath + "\\" + x), allChildren))
    return filePaths

def getFileExtension(fileName : str) -> str:
    return fileName.split(".")[-1].lower()

def makeFolder(folderPath : str) -> bool:
    try:
        os.mkdir(folderPath)
        return True
    except FileExistsError:
        return False

def getFoldersFromFolder(folderPath : str):
    allChildren = os.listdir(folderPath)
    filePaths = list(filter(lambda x : not os.path.isfile(folderPath + "\\" + x), allChildren))
    return filePaths

def moveFile(originalPath : str, destinationPath : str):
    os.rename(originalPath, destinationPath)

def getFolderName(fileExtension : str, settingsDict : dict) -> str:
    for key in settingsDict["Extensions"].keys():
        if (fileExtension in settingsDict["Extensions"][key]):
            return key
    return settingsDict["Default"]