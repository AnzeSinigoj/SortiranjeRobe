import os 
from shutil  import move
import shutil 

source = "/home/anze/Downloads/Source"


audioext = ["mp3", "wav", "flac", "m4a", "ogg"]
docsext = ["docx", "pdf", "txt", "doc", "html", "htm", "xls", "xlsx","ppt", "pptx", "odp", "key" ]
videoext = ["mp4", "avi", "mov","flv", "avchd"]
picsext = ["jpg", "png", "gif", "jpeg", "svg", "tiff", "tif"]

audiodst = os.path.join(source, "Audio")
docsdst = os.path.join(source, "Documents")
videodst = os.path.join(source, "Video")
picsdst = os.path.join(source, "Pictures")
otherdst = os.path.join(source, "Others")

paths = [audiodst, docsdst, videodst, picsdst, otherdst]

for i in paths:
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
print (filteredList)

def sorting():
    print ("Entering sorting stage...")
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

sorting()
