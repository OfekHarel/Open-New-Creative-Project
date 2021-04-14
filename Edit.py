import os

print("Open your new project here:")

DEF_KINDS = ["C4D", "PR", "AE"]
DEFAULT_ROOT = r'A:\Editing\Data'
kind = input("Which platform? " + str(DEF_KINDS) + ": ")
kind.capitalize()

while kind not in DEF_KINDS:
    print("pls try again")
    kind = input("Which platform? " + str(DEF_KINDS) + ": ")
    kind.capitalize()

done = False
root = ""
while not done:
    try:
        name = input("The name of the project: ")
        root = os.path.join(DEFAULT_ROOT, kind, "prjs", name)
        os.makedirs(root)
        done = True
        print("Project folder created!")

    except OSError:
        print("error")
        done = False

try:
    os.makedirs(os.path.join(root, "src"))
    os.makedirs(os.path.join(root, "prj"))
    print("Project util folders created!")
except OSError:
    print("Error")
