# import the required modules
import os, shutil

# Download path
dl = "/sdcard/Download/"
folders = ["Video","Images","Music","Apps","Documents","Icons","Compressed","Others"]

# create destination folder 
for i in range(len(folders)):
   def mkdirs():
      os.makedirs(dl+folders[i])
   if os.path.exists(dl+folders[i]) == False:
      mkdirs()
      os.system("echo '\n\e[92mSuccessfully created folder:'")
      print(folders[i]) 

# Declaring files' formats with arrays
vids = ["mp4","mkv","avi","mov"]
imgs = ["jpg","jpeg","img"]
icons = ["png","ico"]
auds = ["mp3","aac","m4a"]
docx = ["docx","doc","pdf","epub","bok","pptx","xlsx"]
apks = ["apk","xapk","exe"]
comps = ["zip","rar","tar","gz","iso","7z","bz2","jar","lzma"]

# Change the current working directory(cwd) to the Download path

files = os.listdir(dl) # scan all files inside cwd
for fl in files:
   for i in range(len(folders)):
      if os.path.isfile(fl): # isfile only
         ext = (fl.split(".")[-1]).lower() # split and convert extension to lowercase
         try:
            if ext in vids:
               shutil.move(fl, dl+folders[i]) # start moving 
               print(fl,"has been moved to",dl+folders[0])
            elif ext in imgs:
               shutil.move(fl, dl+folders[i])
               print(fl,"has been moved to",dl+folders[1])
            elif ext in auds:
               shutil.move(fl, dl+folders[i])
               print(fl,"has been moved to",dl+folders[2])
            elif ext in apks:
               shutil.move(fl, dl+folders[i])
               print(fl,"has been moved to",dl+folders[3])
            elif ext in docx:
               shutil.move(fl, dl+folders[i])
               print(fl,"has been moved to",dl+folders[4])
            elif ext in icons:
               shutil.move(fl, dl+folders[i])
               print(fl,"has been moved to",dl+folders[5])
            elif ext in comps:
               shutil.move(fl, dl+folders[i])
               print(fl,"has been moved to",dl+folders[6])
            else:
               shutil.move(fl, dl+folders[i]) 
               print(fl,"has been moved to",dl+folders[7])
         except:
            print("Can't move file, file already exist") 

os.system('echo "\n\e[92mNow you can chill!\e[0m\n"')




