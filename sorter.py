# import the required modules
import os, shutil
from styl import * # styling terminal output

# Download path
dl = "/sdcard/Download/"
folders = ["Video","Images","Music","Apps","Documents","Icons","Compressed","Others"]
   
# declaring file formats with arrays
# you can add your desired file format
vids = ["mp4","mkv","avi","mov"]
imgs = ["jpg","jpeg","img"]
icons = ["png","ico"]
auds = ["mp3","aac","m4a"]
docx = ["docx","doc","pdf","epub","bok","pptx","xlsx"]
apks = ["apk","xapk","exe"]
comps = ["zip","rar","tar","gz","iso","7z","bz2","jar","lzma"]
exception = 'crdownload'

# create destination folder 
for i in range(len(folders)):
   if os.path.exists(dl+folders[i]) == False:
      os.makedirs(dl+folders[i])
      print(style.OKGREEN+"Successfully created folder:",style.HEADER+dl+style.OKBLUE+folders[i])
      
# change the current working directory (cwd) to dl path
os.chdir(dl)

def loop():
   files = os.listdir("./") # scan all files inside cwd
   for fl in files:
      if os.path.isfile(fl): # isfile only
         hidden = fl.startswith('.')
         ext = (fl.split(".")[-1]).lower() # split and convert extension to lowercase
         try:
            if hidden:
               pass
            elif ext in exception:
               pass
            elif ext in vids:
               shutil.move(fl, folders[0]) # start moving 
               print(fl,"has been moved to",dl+folders[0])
            elif ext in imgs:
               shutil.move(fl, folders[1])
               print(fl,"has been moved to",dl+folders[1])
            elif ext in auds:
               shutil.move(fl, folders[2])
               print(fl,"has been moved to",dl+folders[2])
            elif ext in apks:
               shutil.move(fl, folders[3])
               print(fl,"has been moved to",dl+folders[3])
            elif ext in docx:
               shutil.move(fl, folders[4])
               print(fl,"has been moved to",dl+folders[4])
            elif ext in icons:
               shutil.move(fl, folders[5])
               print(fl,"has been moved to",dl+folders[5])
            elif ext in comps:
               shutil.move(fl, folders[6])
               print(fl,"has been moved to",dl+folders[6])
            else:
               shutil.move(fl, folders[7]) 
               print(fl,"has been moved to",dl+folders[7])
         except:
            for x in range(len(folders)):
               exists = os.path.isfile(folders[x])
               if fl == exists:
                  print(f"\n{style.FAIL}Can't move {fl}, already exist") 
                  pass
         
while True:
   loop()
   
os.system('echo "\n\e[92mNow you can chill!\e[0m\n"')
   
