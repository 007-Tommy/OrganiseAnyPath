import os
import shutil
import sys

directories = {
    "Images": {".png", ".jpg", ".webp", ".jpeg", ".svg", ".bmp", ".avif"},
    "Videos": {".webm", ".gif", ".avi", ".mp4", ".mpg", ".mpeg", ".m4v"},
    "Audio": {".mp3", ".ogg", ".m4a", ".wav", ".opus", ".raw"},
    "Applications": {".exe", ".msi", ".apk", ".pkg", ".jar"},
    "Documents": {".txt", ".csv", ".pdf", ".md", ".json", ".xml", ".doc", ".docx", ".odt"},
    "Compressed": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".lz", ".lzma", ".lz4", ".zst", ".zstd"},
    "Code": {".py", ".java", ".c", ".cpp", ".cs", ".js", ".ts", ".html", ".htm", ".css", ".php", ".sql", ".rb", ".pl", ".sh", ".bat", ".ps1", ".swift", ".kt", ".dart"},
    "Presentations": {".ppt", ".pptx", ".key", ".odp"},
    "Spreadsheets": {".xls", ".xlsx", ".ods", ".csv"},
    "Fonts": {".ttf", ".otf", ".woff", ".woff2"},
    "Torrents": {".torrent"},
    "Rainmeter": {".rmskin"},
    "Anki decks": {".apkg"},
    "Other": {"N/A"}
}

rootPath = "EMPTY"
combine = False
conflictingDirectories = []

def checkForConflict(directories):
    """
    Check for conflicts between existing directories and the given directories.

    Args:
        directories (dict): A dictionary containing the directories to check.

    Returns:
        bool: True if there is a conflict, False otherwise.
    """
    conflict = False
    for key in directories.keys():
        dirPath = rootPath + "\\" + key
        if os.path.exists(dirPath):
            conflict = True
            conflictingDirectories.append(key)
    
    return conflict

def createFolders(directories):
    """
    Create folders based on the provided dictionary of directories.
    Args:
        directories (dict): A dictionary containing the names of the directories to be created.
    """

    global combine
    global rootPath

    for key in directories.keys():
        dirPath = rootPath + "/" + key
        if os.path.exists(dirPath):
            if not combine:
                os.rename(dirPath, rootPath + "\\" + getValidName(key + "Old", rootPath))
                os.mkdir(dirPath)
            # If combine is True, no need to do anything
        else:
            os.mkdir(dirPath)

def sortFiles(directories):
    """
    Sorts files in rootPath based on the specified directories.

    Args:
        directories (dict): A dictionary containing the directory names as keys and a list of file extensions as values.

    Returns:
        None
    """

    global rootPath

    for f in os.listdir(rootPath):

        # Skip our own directories
        if f in directories.keys():
            continue

        fileLocation = rootPath + "\\" + f
        fileName, extension = os.path.splitext(f)

        fileSorted = False
        for directoryName in directories:

            # Skip sorted files
            if fileSorted:
                break

            # Skip the 'Other' directory
            if directoryName == "Other":
                continue

            # Check if the file extension is in the list of extensions for the current directory
            # If it is, move the file to the directory, and set fileSorted to True

            dirPath = rootPath + "\\" + directoryName
            for testExt in directories[directoryName]:
                if extension == testExt:
                    fileSorted = True
                    newPath = dirPath + f"\\{getValidName(f, dirPath)}"
                    shutil.move(fileLocation, newPath)
        
        if not fileSorted:
            otherDirPath = rootPath + "\\Other"
            shutil.move(fileLocation, otherDirPath + "\\" + getValidName(f, otherDirPath))

def cleanUp(directories):
    global rootPath

    # Remove empty directories
    for directory in directories:
        if len(os.listdir(rootPath + "\\" + directory)) == 0:
            os.rmdir(rootPath + "\\" + directory)

def getValidName(fileName, path):
    i = 1

    # If the file already exists...
    if os.path.exists(path + "\\" + fileName):
        fileN, extension = os.path.splitext(fileName)

        # ...increment the number at the end of the file name until a valid name is found
        while os.path.exists(path + "\\" + f"{fileN}_{i}{extension}"):
            i += 1  

        return f"{fileN}_{i}{extension}"
        
    else:
        # ...otherwise, return the original file name
        return fileName
                    
def setup():
    """
    Prompts the user to input a directory path and validates if it exists and is a directory.
    If the path is valid, it sets the rootPath variable to the input path.

    This function also checks for directory conflicts in the rootPath and prompts the user to decide
    whether to combine the contents of conflicting folders or rename them to 'DIRNAME_old'.
    """

    global rootPath
    global combine

    valid = False
    while not valid:
        pathInput = input("The directory to organise: ")
        if os.path.exists(pathInput) and os.path.isdir(pathInput):
            rootPath = pathInput
            valid = True
        else:
            print("Invalid path!")

    # Check for directory conflicts in rootPath
    # If there are conflicts, prompt the user to decide whether to combine the contents of conflicting folders

    conflict = checkForConflict(directories)

    if conflict:
        print(f"\"{rootPath}\"")
        print("The following folders in the selected directory conflict with the directories the program is trying to create to organise your files:")
        for conflictingDir in conflictingDirectories:
            print(conflictingDir)

    while conflict:
        combineInput = input("Would you like to combine the contents of these folders with their new versions? If not, they will simply be renamed to \"[Current name]Old\" and moved to the \"Other\" directory. (Y/N) ").upper()
        if combineInput == "Y":
            conflict = False
            combine = True
        elif combineInput == "N":
            conflict = False
            # combine is already False

    

    

    
setup()
createFolders(directories)
sortFiles(directories)
cleanUp(directories)

print("Organisation complete!")
print("It is recommended to check the 'Other' folder for any files that could not be sorted.")
input("You can now close the program.\n")
