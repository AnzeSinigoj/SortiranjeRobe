import os 
from shutil  import move

source = input("Vnesite pot do izvirne mape: ")
audiodst = "./Audio"
audioext = ["mp3", "wav", "flac"]
docsdst = "./Documents"
docsext = ["docx", "pdf", "txt"]
videodst = "./Video"
videoext = ["mp4", "avi", "mov",]
filteredList = []
dirlist  = os.listdir(source)

for z in dirlist:
    for i in list (z):
        if i == ".":
            filteredList.append(z)
print (filteredList)

def sorting():
    print ("Entering sorting stage...")
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
sorting()
