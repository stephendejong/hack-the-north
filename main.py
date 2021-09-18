#hackthenorth elle woods CHER outfit customizer

from tkinter import *

# making window
root = Tk()
root.wm_title("Clueless")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()-75
root.geometry("%dx%d" % (width, height))

# adding background image
bgImage = PhotoImage(file = "leopard-bg.png")
label1 = Label(root, image = bgImage)
label1.place(x=0, y=0)

# show window
root.mainloop()


