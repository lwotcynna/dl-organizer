# import the required modules
import os
import shutil as sh
from colors import colorz as C # styling terminal output

# Download path
dl = "/storage/D639-79B5/Download/"
folders = ["Video","Images","Music","Apps","Documents","Compressed","Others"]
   
# declaring file formats with arrays
# you can add your desired file format
vids = ["mp4","mkv","avi","mov"]
imgs = ["jpg","jpeg","img","png","ico","webp"]
auds = ["mp3","aac","m4a"]
apks = ["apk","xapk","exe"]
docx = ["docx","doc","pdf","epub","bok","pptx","xlsx","txt"]
comps = ["zip","rar","tar","gz","xz","iso","7z","bz2","jar","lzma"]
sc = ["html","css","js","py","cpp","c","xml","json"]
exception = 'crdownload'

os.chdir('/sdcard')
files = os.listdir("./") # scan all files inside cwd


# create destination folder 
for i in range(len(folders)):
    if os.path.exists(dl+folders[i]) == False:
        os.makedirs(dl+folders[i])
        print(C.OK+"Successfully created folder:",C.HEAD+dl+C.BLUE+folders[i])

def sortit():
    files = os.listdir("./") # scan all files inside cwd
    for fl in files:
        if os.path.isfile(fl):
            hidden = fl.startswith('.')
            ext = (fl.split(".")[-1]).lower()
        
            try:
                if hidden or ext in exception:
                    pass
                elif ext in vids:
                    sh.move(fl,folders[0])
                    print(C.HEAD+fl,C.OK+"moved to 👉", C.BLUE+"Download >", folders[0]+C.O)
                elif ext in imgs:
                    sh.move(fl,folders[1])
                    print(C.HEAD+fl,C.OK+"moved to 👉", C.BLUE+"Download >", folders[1]+C.O)
                elif ext in auds:
                    sh.move(fl,folders[2])
                    print(C.HEAD+fl,C.OK+"moved to 👉", C.BLUE+"Download >", folders[2]+C.O)
                elif ext in apks:
                    sh.move(fl,folders[3])
                    print(C.HEAD+fl,C.OK+"moved to 👉", C.BLUE+"Download >", folders[3]+C.O)
                elif ext in docx:
                    sh.move(fl,folders[4])
                    print(C.HEAD+fl,C.OK+"moved to 👉", C.BLUE+"Download >", folders[4]+C.O)
                elif ext in comps:
                    sh.move(fl,folders[5])
                    print(C.HEAD+fl,C.OK+"moved to 👉", C.BLUE+"Download >", folders[5]+C.O)
                else:
                    sh.move(fl,folders[-1])
                    print(C.HEAD+fl,C.OK+"moved to 👉", C.BLUE+"Download >", folders[-1]+C.O)

            except FileExistsError:
                print(C.FAIL+"Can't move",C.BLUE+fl+C.FAIL+", file exists")
                pass
            except:
                pass

# change the current working directory (cwd) to dl path

input(C.WARN+"""
*==================================================*
| This script will running in the background until |
| you stop it by hit [CTRL+C]                      |
|                                                  |
| Your downloaded or moved file to the Download/   |
| folder will automatically move to its subfolder. |
|                                                  |
| [•••] Press enter to continue                    |
*==================================================*
"""+C.O)

print("")
print(C.OK+"it's running...\n")

os.chdir(dl)
# make it possible to always run in background
while True:
    try:
        sortit()
    except KeyboardInterrupt:
        print(C.FAIL+"\nStopped!",C.O)
        break
   
