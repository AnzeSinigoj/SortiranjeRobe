import os 
from shutil  import move
import shutil 

source = input("Vnesite pot do izvirne mape: ")
os.mkdir("./Audio")
os.mkdir("./Documents")
os.mkdir("./Video")
os.mkdir("./Pictures")
os.mkdir("./Other")
audiodst = "./Audio"
audioext = ["mp3", "wav", "flac", "m4a", "ogg"]
docsdst = "./Documents"
docsext = ["docx", "pdf", "txt", "doc", "html", "htm", "xls", "xlsx","ppt", "pptx", "odp", "key" ]
videodst = "./Video"
videoext = ["mp4", "avi", "mov","flv", "avchd"]
picsdst = "./Pictures"
picsext = ["jpg", "png", "gif", "jpeg", "svg", "tiff", "tif"]
filteredList =[]
dirlist = os.listdir(source)

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

