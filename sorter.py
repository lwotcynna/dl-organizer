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
docx = ["docx","doc","pdf","epub","bok","pptx","xlsx","txt"]
icons = ["png","ico"]
comps = ["zip","rar","tar","gz","xz","iso","7z","bz2","jar","lzma"]

#formats = [vids,imgs,auds,apks,docx,icons,comps]

exception = 'crdownload'

# create destination folder 
for i in range(len(folders)):
   if os.path.exists(dl+folders[i]) == False:
      os.makedirs(dl+folders[i])
      print(style.OKGREEN+"Successfully created folder:",style.HEADER+dl+style.OKBLUE+folders[i])
      

def sortit():

   files = os.listdir("./") # scan all files inside cwd
   for fl in files:
      if os.path.isfile(fl): # isfile only
         hidden = fl.startswith('.')
         ext = (fl.split(".")[-1]).lower() # split and convert extension to lowercase
        
         try:
             if hidden or ext in exception:
                 pass
             elif ext in vids:
                 shutil.move(fl,folders[0])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[0]+style.ENDC)
             elif ext in imgs:
                 shutil.move(fl,folders[1])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[1]+style.ENDC)
             elif ext in auds:
                 shutil.move(fl,folders[2])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[2]+style.ENDC)
             elif ext in apks:
                 shutil.move(fl,folders[3])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[3]+style.ENDC)
             elif ext in docx:
                 shutil.move(fl,folders[4])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[4]+style.ENDC)
             elif ext in icons:
                 shutil.move(fl,folders[5])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[5]+style.ENDC)
             elif ext in comps:
                 shutil.move(fl,folders[6])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[6]+style.ENDC)
             else:
                 shutil.move(fl,folders[-1])
                 print(style.HEADER+fl,style.OKGREEN+"moved to 👉", style.OKBLUE+"Download >", folders[-1]+style.ENDC)

         except:
             pass
# change the current working directory (cwd) to dl path
os.chdir(dl)

input(style.WARNING+"***\nThis script will running in the background until you stop it\n[CTRL+C]. Your downloaded or moved file to the Download/ folder will automatically move to its subfolder.\npress enter to continue\n***"+style.ENDC)
print(style.OKGREEN+"\nit's running...\n")

# make it possible to run in background
while True:
   sortit()
   
   
