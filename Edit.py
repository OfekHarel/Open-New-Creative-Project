import os
import pyperclip

DEF_INNER_FOLDER = "prjs"
DEF_KINDS = ["C4D", "PR", "AE", "XD"]
DEFAULT_ROOT = r'A:\Editing\Data'
FORMAT_DICT = {"C4D": r'C:\Program Files\Maxon Cinema 4D R21\Cinema 4D.exe',
                "PR": r'C:\Program Files\Adobe\Adobe Premiere Pro 2021\Adobe Premiere Pro.exe',
                "AE": r'C:\Program Files\Adobe\Adobe After Effects 2021\Support Files\AfterFX.exe'}
DEF_PRJ_FOLDER_NAME = "Project"
DEF_SRC_FOLDER_NAME = "Resources"

os.system('cls')
print("Open your new project here:")

kind = input("Which platform? " + str(DEF_KINDS) + ": ")
kind.capitalize()

while kind not in DEF_KINDS:
    print("Try again! Project type not supported!")
    kind = input("Which platform? " + str(DEF_KINDS) + ": ")
    kind.capitalize()

done = False
root = ""
while not done:
    try:
        name = input("The name of the project: ")

        if kind == "XD": 
            root = os.path.join(DEFAULT_ROOT, kind, name)
        else:
            root = os.path.join(DEFAULT_ROOT, kind, DEF_INNER_FOLDER, name)

        os.makedirs(root)
        done = True
        print("Project folder created!")

    except OSError:
        print("Name exist! Try other options")
        done = False

try:
    os.makedirs(os.path.join(root, DEF_SRC_FOLDER_NAME))
    
    if kind != "XD":
        os.makedirs(os.path.join(root, DEF_PRJ_FOLDER_NAME))
        print("Project preset folders created!")

    

except OSError:
    print("Error")

pyperclip.copy(root)
os.startfile(FORMAT_DICT.get(kind))
os.startfile(str(root))
