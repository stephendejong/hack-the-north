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
bgImage = PhotoImage(file = "leopard-bg.png")
background = Label(root, image = bgImage)
background.place(x=0, y=50)

#shirt label
shirtbox = Label(root, bg='white', width="70", height="15")
shirtbox.place(x=width/2-250, y=70)

#pant label
pantbox = Label(root, bg='white', width="70", height="15")
pantbox.place(x=width/2-250, y=365)

#image gallery
top2 = PhotoImage(file="top2.png")
top4 = PhotoImage(file="shirt4.png")
top5 = PhotoImage(file="top5.png")

toplist = [top2, top4, top5]

topindex = toplist[1]

shirtbox.config(image=topindex, width="300", height="300")

topindex = 0
bottomindex = 1

#DressMe button
def action(topindex, bottomindex):
    if (topindex == bottomindex):
        dressme = Label(root, bg='white', width="20", height="5", text="CUTE!", font=("Impact", 24))
        dressme.place(x=width / 2 - 250, y=200)
    else:
        dressme = Label(root, bg='white', width="20", height="5", text="You're totally buggin'!", font=("Impact", 24))
        dressme.place(x=width / 2 - 250, y=200)


dressmebutton = Button(root, text="DRESS ME", command=lambda: action(topindex, bottomindex))
dressmebutton.place(x=900, y=500)

#next top
def nexttop(topindex):
    newimg = toplist[topindex+1]
    shirtbox.configure(image=newimg)
    shirtbox.image = newimg


nextbutton = Button(root, text=">>", command=lambda: nexttop(topindex))
nextbutton.place(x=900, y=500)

# show window
root.mainloop()
