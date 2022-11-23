import os, shutil, time, tkinter as tk
from tkinter import*
from shutil  import move
from tkinter import filedialog as fd
from PIL import ImageTk, Image

source = None

root = tk.Tk()
root.geometry("600x400")
root.configure(bg="white")

root.title("Auto File Organizer")
#root.iconbitmap("/home/anze/Documents/Python/data/IkonaProgram.ico")

logo = ImageTk.PhotoImage(Image.open("./data/FileOrganizerLogo.png"))
label = Label(image=logo, width=510, height=150, bg="white")
label.pack() 

#btn_yes =  tk.Button(newwindow, text="Yes", bg="grey", fg="white")


audioext = ["mp3", "wav", "flac", "m4a", "ogg"]
docsext = ["docx", "pdf", "txt", "doc", "html",
           "htm", "xls", "xlsx", "ppt", "pptx", "odp", "key"]
videoext = ["mp4", "avi", "mov", "flv", "avchd"]
picsext = ["jpg", "png", "gif", "jpeg", "svg", "tiff", "tif"]

custom_paths = []

def open():
    global source
    source = fd.askdirectory()
    path = tk.Label(text = f"Pot izbrane mape: {source}")
    path.place(relx= 0.5, rely= 0.7, anchor="n")
    global cus_Audio
    global cus_Docs
    global cus_Drugo
    global cus_Video
    global cus_Slike
    cus_Docs = os.path.join(source, "Documents")
    cus_Audio = os.path.join(source, "Audio")
    cus_Video = os.path.join(source, "Video")
    cus_Slike = os.path.join(source, "Pictures")
    cus_Drugo = os.path.join(source, "Other")

def sortingDF():
    audiodst = os.path.join(source, "Audio")
    docsdst = os.path.join(source, "Documents")
    videodst = os.path.join(source, "Video")
    picsdst = os.path.join(source, "Pictures")
    otherdst = os.path.join(source, "Others")

    global def_paths
    def_paths = [audiodst, docsdst, videodst, picsdst, otherdst]

    for i in def_paths:
        if os.path.exists(i):
            pass
        else:
            os.mkdir(i)

    filteredList =[]

    dirlist = os.listdir(source)


    for z in dirlist:
        for i in list (z):
            if i == ".":
                filteredList.append(z)

    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in docsext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, docsdst)

    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in audioext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, audiodst)

    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in videoext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, videodst)
        
    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in picsext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, picsdst)
        
    ost = []
    for path in os.listdir(source):
        if os.path.isfile(os.path.join(source, path)):
            ost.append(path)

    for i in ost:
        temp1 = os.path.join(source, i)
        move(temp1, otherdst)

        
    label3 = tk.Label(text="Sortiranje končano!")
    label3.place(relx=0.5, rely=0.80, anchor = "center")

def customSort():
    custom = [cus_Audio, cus_Docs, cus_Drugo, cus_Slike, cus_Video]

    for i in custom:
        if os.path.exists(i):
            pass
        else:
            os.mkdir(i)

    filteredList =[]

    dirlist = os.listdir(source)


    for z in dirlist:
        for i in list (z):
            if i == ".":
                filteredList.append(z)

    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in docsext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, cus_Docs)

    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in audioext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, cus_Audio)

    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in videoext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, cus_Video)
        
    for x in filteredList:
        arr = x.split ('.')
        ext = arr[-1]
        for y in picsext:
            if ext == y:
                temp1 = os.path.join(source, x)
                move(temp1, cus_Slike)
        
    ost = []
    for path in os.listdir(source):
        if os.path.isfile(os.path.join(source, path)):
            ost.append(path)

    for i in ost:
        temp1 = os.path.join(source, i)
        move(temp1, cus_Drugo)
    
    label4 = tk.Label(newwindow2, text="Sortiranje končano!")
    label4.place(relx=0.55, rely=0.9, anchor = "center")


def gumb_okno():
    global newwindow2
    newwindow2 = tk.Tk()
    newwindow2.title("Auto File Organizer")
    newwindow2.geometry("600x300")
    newwindow2.configure(bg="white")

    video_text = tk.Button(newwindow2, text = "Videi", bg="white", fg="black",width=5, font=("Arial", 14), borderwidth=0)
    video_text.grid(row=1, column=1)
    slike_text = tk.Button(newwindow2, text = "Slike", bg="white", fg="black",width=5, font=("Arial", 14), borderwidth=0)
    slike_text.grid(row=2, column=1)
    docs_text = tk.Button(newwindow2, text = "Docs", bg="white", fg="black",width=5, font=("Arial", 14), borderwidth=0)
    docs_text.grid(row=3, column=1)
    audio_text = tk.Button(newwindow2, text = "Audio", bg="white", fg="black",width=5, font=("Arial", 14), borderwidth=0)
    audio_text.grid(row=4, column=1)
    other_text = tk.Button(newwindow2, text = "Drugo", bg="white", fg="black",width=5, font=("Arial", 14), borderwidth=0)
    other_text.grid(row=5, column=1)

    btn_video = tk.Button(newwindow2, text = "Izberi mapo", bg="grey", fg="white",width=11, font=("Arial", 14), borderwidth=2,
    command=gumbVideo)
    btn_video.grid(row=1, column=4,columnspan=2)
    btn_slike = tk.Button(newwindow2, text = "Izberi mapo", bg="grey", fg="white",width=11, font=("Arial", 14), borderwidth=2,
    command=gumbSlike)
    btn_slike.grid(row=2, column=4,columnspan=2)
    btn_docs = tk.Button(newwindow2, text = "Izberi mapo", bg="grey", fg="white",width=11, font=("Arial", 14), borderwidth=2,
    command=gumbDoc)
    btn_docs.grid(row=3, column=4, columnspan=2)
    btn_audio = tk.Button(newwindow2, text = "Izberi mapo", bg="grey", fg="white",width=11, font=("Arial", 14), borderwidth=2,
    command=gumbAudio)
    btn_audio.grid(row=4, column=4,columnspan=2)
    btn_other = tk.Button(newwindow2, text = "Izberi mapo", bg="grey", fg="white",width=11, font=("Arial", 14), borderwidth=2,
    command=gumbOth)
    btn_other.grid(row=5, column=4,columnspan=2)

    CusSort = tk.Button (newwindow2, text="Poljubno sortiraj!", bg="white", fg="grey", width=23, font=("Arial", 14),
    borderwidth=4, command=customSort)
    CusSort.grid(row=8, column=6, columnspan=3)

    def izberimapo():
        global btn_video
        global btn_slike
        global btn_other
        global btn_docs
        global btn_audio
    izberimapo()
    newwindow.destroy()
    root.destroy()
def gumbVideo():
    source2 = fd.askdirectory()
    global cus_Video
    cus_Video = source2
    path2 = tk.Label(newwindow2,text = f"Pot izbrane mape: {source2}")
    #path2.place(relx= 0.5, rely= 0.52, anchor="n")
    path2.grid(row=1, column=6)

def gumbSlike():
    source2 = fd.askdirectory()
    global cus_Slike
    cus_Slike = source2
    path2 = tk.Label(newwindow2, text = f"Pot izbrane mape: {source2}")
    #path2.place(relx= 0.5, rely= 0.52, anchor="n")
    path2.grid(row=2, column=6)

def gumbDoc():
    source2 = fd.askdirectory()
    global cus_Docs
    cus_Docs = source2
    path2 = tk.Label(newwindow2, text = f"Pot izbrane mape: {source2}")
    #path2.place(relx= 0.5, rely= 0.52, anchor="n")
    path2.grid(row=3, column=6)

def gumbAudio():
    source2 = fd.askdirectory()
    global cus_Audio
    cus_Audio = source2
    path2 = tk.Label(newwindow2,text = f"Pot izbrane mape: {source2}")
    #path2.place(relx= 0.5, rely= 0.52, anchor="n")
    path2.grid(row=4, column=6)

def gumbOth():
    source2 = fd.askdirectory()
    global cus_Drugo
    cus_Drugo = source2
    path2 = tk.Label(newwindow2, text = f"Pot izbrane mape: {source2}")
    #path2.place(relx= 0.5, rely= 0.52, anchor="n")
    path2.grid(row=5, column=6)

def OpenNewWindow():
    global newwindow
    open()
    newwindow = Toplevel(root)
    newwindow.title("Auto File Organizer")
    newwindow.geometry("218x65")

    def yn():
        btn_privzeto = tk.Button(newwindow,text = "Sortiraj kot privzeto",bg="grey", fg="white", width=23, font=("Arial", 12),
         borderwidth= 3,command=sortingDF)
        btn_privzeto.grid(row=1, column=6, columnspan=3)
        btn_poljubno = tk.Button(newwindow,text = "Sortiraj poljubno",bg="grey", fg="white", width=23, font=("Arial", 12),
         borderwidth= 3,command=gumb_okno)  
        btn_poljubno.grid(row=3, column=6, columnspan=3)
    yn()
    
button = tk.Button(root, text = "Izberite mapo, ki jo želite sortirati!", width=25, height= 2, bg= "grey",fg="white", 
font=("Arial", 14), command=OpenNewWindow)
button.place(relx=0.5, rely=0.54, anchor="n")

exit_btn = PhotoImage(file = "./data/shutdown.png")
label = Label(image=exit_btn)
btn = Button(root, image=exit_btn, command=root.quit, borderwidth=0)
btn.place(relx=0.85, rely=0.85, anchor="center")

root.mainloop()