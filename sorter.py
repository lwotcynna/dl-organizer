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
auds = ["mp3","aac","m4a"]
apks = ["apk","xapk","exe"]
docx = ["docx","doc","pdf","epub","bok","pptx","xlsx"]
icons = ["png","ico"]
comps = ["zip","rar","tar","gz","xz","iso","7z","bz2","jar","lzma"]

formats = [vids,imgs,auds,apks,docx,icons,comps]

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
            for i in range(len(folders)):
                if hidden:
                    pass
                elif ext in exception:
                    pass
                elif ext in formats[i]:
                    shutil.move(fl, folders[i]) # start moving 
                    print(fl,"has been moved to",dl+folders[i])
                else:
                    shutil.move(fl,folders[-1])
                    print(fl,"has been moved to",dl+folders[-1])
         except:
            for x in range(len(folders)):
               exists = os.listdir(folders[x])
               if fl in exists:
                  print(f"\n{style.FAIL}Can't move {fl}, already exist"+style.ENDC) 
                  pass

while True:
   loop()
   
   
