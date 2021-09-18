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

# adding background image
bgImage = PhotoImage(file = "leopard-bg.png")
background = Label(root, image = bgImage)
background.place(x=0, y=50)

#shirt label
shirtbox = tkinter.Label(root, bg='white', width="70", height="20")
shirtbox.place(x=width/2-250, y=50)

# show window
root.mainloop()
