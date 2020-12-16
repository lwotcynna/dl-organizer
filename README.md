# dl-organizer
<p>Automatically sorts and arrange files on Your Download Folder.</>

### Requirements
1. [Termux app](https://play.google.com/store/apps/details?id=com.termux) with storage access permission
2. Internet connection (installing python) 

### Usage
Open Termux app and then type:
```bash
$ pkg update && pkg upgrade -y
$ pkg install git python 
$ git clone https://github.com/annazc-ann/dl-organizer
$ cd dl-organizer/
$ chmod +x *
$ sh mdir.sh
```
and then run the python script by typing:
```bash
$ python sorter.py
```
<p>It will move the files inside your Download folder to the specified subfolder (according to the file extension) created by <code>$ sh mdir.sh</code>.
<br>Once it starts, it will always running in the background until you stop it by hit <code>ctrl+c</code> or
 the Termux app is closed.</p>
Have a nice day, friends ✨
<h3>This project was inspired by:
https://youtu.be/JNl2krTKf-s
</h3>
