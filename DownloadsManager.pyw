import json
import threading
import time

import keyboard

import FileSorter as fs
import SystemManager as sysman

settings = {}

with open("settings.json", "r") as f:
    settings = json.loads(f.read())

downloadsFolder = settings["workingFolder"]

fileSorter = fs.FileSorter(downloadsFolder)

lastFolderContents = []

end = False

def breakerFunction():
    global end
    while not end:
        if keyboard.is_pressed(settings["quitShortcut"]):
            end = True

breakThread = threading.Thread(target=breakerFunction)
breakThread.start()

while not end:
    if (len(lastFolderContents) < len(sysman.getFilesFromFolder(downloadsFolder))):
        #Folder has a new file
        fileSorter.sortInFolders()
    lastFolderContents = sysman.getFilesFromFolder(downloadsFolder)
    time.sleep(3)
