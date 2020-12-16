# import the required modules
import os, shutil

# Download path
dl = "/sdcard/Download/"
folders = ["Video","Music","Apps","Documents","Icons","Compressed","Others"]

# Declaring files' formats with arrays
vids = ["mp4","mkv","avi","mov"]
imgs = ["jpg","jpeg","img"]
icons = ["png","ico"]
docx = ["docx","doc","pdf","epub","bok","pptx","xlsx"]
apks = ["apk","xapk","exe"]
comps = ["zip","rar","tar","gz","iso","7z","bz2","jar","lzma"]

# Change the current working directory(cwd) to the Download path
os.chdir(dl)

# Running on background
while True:
    files = os.listdir("./") # scan all files inside cwd
    for fl in files:
        if os.path.isfile(fl): # isfile only
            ext = (fl.split(".")[-1]).lower() # split and convert extension to lowercase
            if ext in vids:
                shutil.move(fl, dl+folders[0]) # start moving 
                print(fl,"has been moved to",dl+folders[0])
            elif ext in imgs:
                shutil.move(fl, dl+folders[1])
                print(fl,"has been moved to",dl+folders[1])
            elif ext in apks:
                shutil.move(fl, dl+folders[2])
                print(fl,"has been moved to",dl+folders[2])
            elif ext in docx:
                shutil.move(fl, dl+folders[3])
                print(fl,"has been moved to",dl+folders[3])
            elif ext in icons:
                shutil.move(fl, dl+folders[4])
                print(fl,"has been moved to",dl+folders[4])
            elif ext in comps:
                shutil.move(fl, dl+folders[5])
                print(fl,"has been moved to",dl+folders[5])
            else:
                shutil.move(fl, dl+folders[6])
                print(fl,"has been moved to",dl+folders[6])



print("Save your time and you can chill!")






















