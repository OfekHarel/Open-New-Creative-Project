import os

DEF_INNER_FOLDER = "prjs"
DEF_KINDS = ["C4D", "PR", "AE", "XD"]
DEFAULT_ROOT = r'A:\Editing\Data'
FORMAT_DICT = {"C4D": ".c4d", "PR": ".prproj", "AE": ".aep"}
DEF_PRJ_FOLDER_NAME = "Project"
DEF_SRC_FOLDER_NAME = "Resources"

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
        root = os.path.join(DEFAULT_ROOT, kind, DEF_INNER_FOLDER, name)
        os.makedirs(root)
        done = True
        print("Project folder created!")

    except OSError:
        print("Name exist! Try other options")
        done = False

try:
    os.makedirs(os.path.join(root, DEF_SRC_FOLDER_NAME))
    
    if kind is not "XD":
        os.makedirs(os.path.join(root, DEF_PRJ_FOLDER_NAME))
        print("Project preset folders created!")
        open(os.path.join(root, DEF_PRJ_FOLDER_NAME, name + FORMAT_DICT.get(kind)), 'x').close()
        print("Project file created!")

except OSError:
    print("Error")
