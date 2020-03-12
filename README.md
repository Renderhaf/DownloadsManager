# DownloadsManager
This is a python script that organizes your downloads folder 

## Settings
The origninal settings file looks like this:
```json
{   
    "quitShortcut" : "ctrl+shift+k",
    "workingFolder" : "C:\\Users\\USER\\Downloads",
    "Default" : "Other",
    "Extensions" : {
        "Documents" : ["pdf", "doc", "docx", "ppt", "xlsx", "ppsx", "pptx", "txt", "csv"],
        "Images" : ["jpg", "jpeg", "png", "tiff", "bmp", "webp"],
        "Executables" : ["exe", "jar", "msi"],
        "Zipped Folders" : ["zip", "rar"],
        "Music" : ["mp3", "mid", "wav"],
        "Code" : ["java", "c", "ino", "cpp", "py", "pkl", "json", "js", "html", "css"],
        "Videos" : ["avi", "mov", "mp4", "mpeg", "webm"],
        "WORKFILE" : ["download", "crdownload"]
    }
}
```
**quitShortcut**: a keyboard shortcut that, when used, exits the program.

**workingForlder**: the folder in which the program runs

**default**: the default folder name (Used for files with no known file extension)

**Extensions**: this is the dictionary for file extensions and folders. Each key is the folder name that corresponds with the list of file extensions which are its value.

___Each of these can be changed in order to change how the script functions___

