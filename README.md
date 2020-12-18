# dl-organizer
<p>Automatically sorts and arrange files on Your Download folder.</p>

## Requirements
1. [Termux](https://play.google.com/store/apps/details?id=com.termux) app with storage access permission
2. Internet connection (installing python) 

### Usage
Open Termux app and then type:
```bash
$ pkg update && pkg upgrade -y
$ pkg install git python -y
```
clone this repo:
```bash
$ git clone https://github.com/annazc-ann/dl-organizer
```
enter the cloned dir:
```bash
$ cd dl-organizer/
$ chmod +x *
```
and then run the python script by typing:
```bash
$ python sorter.py
```
<p>It will move the files inside your <code>Download/</code> folder to the specified subfolder (according to the file extension).
<br>Once it starts, it will always running on background until you stop it by hit<code> ctrl + c </code>or the Termux app is closed. <br>
<br>So when you download something (especially with chrome), it will immediately move your downloaded file once it finished. </p>

Have a nice day, friends ✨

### was inspired by:
https://youtu.be/JNl2krTKf-s
