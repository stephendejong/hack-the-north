
from tkinter import *

# making window
root = Tk()
root.wm_title("Clueless")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()-75
root.geometry("%dx%d" % (width, height))

# banner
banner = Label(root, width="1000", height="50")
banner.place(x=0, y=0)
banner.config(bg='black')

# Chers Wardrobe Text
chersWardrobeText = Label(root, text="CHER'S WARDROBE", font=("Impact", 30), fg='white')
chersWardrobeText.place(x=0, y=0)
chersWardrobeText.config(bg='black')

#fall fashions
fallFashionsText = Label(root, text="FALL FASHIONS", font=("Impact", 24), fg='white', relief='raised')
fallFashionsText.place(x=width/2-100, y=2)
fallFashionsText.config(bg='black')

# adding background image
bgImage = PhotoImage(file="leopard-bg.png")
background = Label(root, image=bgImage)
background.place(x=0, y=50)

#shirt label
shirtbox = Label(root, bg='white', width="70", height="15")
shirtbox.place(x=width/2-250, y=60)

#pant label
bottombox = Label(root, bg='white', width="70", height="15")
bottombox.place(x=width/2-250, y=400)

#image gallery
top2 = PhotoImage(file="top2.png")
top4 = PhotoImage(file="shirt4.png")
top5 = PhotoImage(file="top5.png")
bottom1 = PhotoImage(file="skirt1.png")
bottom2 = PhotoImage(file="skirt2.png")
bottom3 = PhotoImage(file="skirt3.png")

toplist = [top2, top4, top5]
bottomlist = [bottom1, bottom2, bottom3]

currentimg = toplist[0]
currentbot = bottomlist[0]
topindex = 0
bottomindex = 0

shirtbox.config(image=currentimg, width="500", height="300")
bottombox.config(image=currentbot, width="500", height="300")

def dressmereaction(topindex, bottomindex):
    if topindex == bottomindex:
        dressme = Label(root, bg='white', width="20", height="5", text="CUTE!", font=("Impact", 24))
        dressme.place(x=1060, y=200)
    else:
        dressme = Label(root, bg='white', width="20", height="5", text="You're totally buggin'!", font=("Impact", 24))
        dressme.place(x=1060, y=200)


dressmebutton = Button(root, text="DRESS ME", width = "15", height = "2", bd=5, font=("Impact", 24), command=lambda: dressmereaction(topindex, bottomindex))
dressmebutton.place(x=1100, y=500)

def nexttop(ti):
    global topindex
    if (ti == len(toplist)-1):
        newimg = toplist[0]
        topindex = 0
    else:
        newimg = toplist[ti+1]
        topindex = topindex+1
    shirtbox.configure(image=newimg)
    shirtbox.image = newimg

def nextbottom(bi):
    global bottomindex
    if (bi == len(bottomlist) - 1):
        newimg = bottomlist[0]
        bottomindex = 0
    else:
        newimg = bottomlist[bi + 1]
        bottomindex = bottomindex + 1
    bottombox.configure(image=newimg)
    shirtbox.image = newimg


#placing the button
photoL = PhotoImage(file = "left-arrow.png")
photoR = PhotoImage(file = "right-arrow.png")
#Bottom left
buttonBL = Button(root, text = "Howdy", width = "240", height = "50",bd=5,image=photoL)
buttonBL.pack()
buttonBL.place(x=width/2-250, y=695)
#Bottom right
buttonBR = Button(root, text = "Howdy", width = "242", height = "50",bd=5, image=photoR, command=lambda: nextbottom(bottomindex))
buttonBR.pack()
buttonBR.place(x=width/2, y=695)
#Top left
buttonTL = Button(root, text = "Howdy", width = "240", height = "50",bd=5, image=photoL)
buttonTL.pack()
buttonTL.place(x=width/2-250, y=350)
#Top right
buttonTR = Button(root, text = "Howdy", width = "242", height = "50",bd=5, image=photoR, command=lambda: nexttop(topindex))
buttonTR.pack()
buttonTR.place(x=width/2, y=350)

# show window
root.mainloop()
