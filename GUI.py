import tkinter as tk
import os 
import shutil
from shutil  import move
from tkinter import filedialog as fd

root = tk.Tk()
root.geometry("500x300")


def exit():
    root.destroy()
    root.quit()

def open():
    global source 
    source = fd.askdirectory()
    path = tk.Label(text = f"Pot izbrane mape: {source}")
    path.place(relx= 0.5, rely= 0.435, anchor="n")
    
button  = tk.Button(root, text = "Izberi mapo!", command=open)
button.place(relx=0.5, rely=0.3, anchor="n")

def sorting():
    os.mkdir("./Audio")
    os.mkdir("./Documents")
    os.mkdir("./Video")
    os.mkdir("./Pictures")
    os.mkdir("./Other")
    audiodst = "./Audio"
    audioext = ["mp3", "wav", "flac"]
    docsdst = "./Documents"
    docsext = ["docx", "pdf", "txt"]
    videodst = "./Video"
    videoext = ["mp4", "avi", "mov",]
    picsdst = "./Pictures"
    picsext = ["jpg", "png", "gif", "jpeg"]

    filteredList = []
    dirlist  = os.listdir(source)

    for z in dirlist:
        for i in list (z):
            if i == ".":
                filteredList.append(z)

    print ("Sorting...")
    for x in filteredList:
        _, ext = x.split ('.')
        #print (ext)
        for y in docsext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, docsdst)

    for x in filteredList:
        _, ext = x.split ('.')
        #print (ext)
        for y in audioext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, audiodst)

    for x in filteredList:
        _, ext = x.split ('.')
        #print (ext)
        for y in videoext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, videodst)

    for x in filteredList:
        _, ext = x.split ('.')
        #print (ext)
        for y in picsext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, picsdst)

    destination = "./Other"
    allfiles = os.listdir(source)
    for f in allfiles:
        src_path  = os.path.join(source, f)
        dst_path = os.path.join(destination, f)
        shutil.move(src_path, dst_path)
        
    label3 = tk.Label(text="Sortiranje končano!")
    label3.place(relx=0.5, rely=0.80, anchor = "center")


button1  = tk.Button(root, text = "Sortiraj", command=sorting)
button1.place(relx=0.5, rely=0.6, anchor="center")


button2  = tk.Button(root, text = "Exit", command=exit)
button2.place(relx=0.85, rely=0.85, anchor="nw")

root.mainloop()