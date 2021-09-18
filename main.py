#hackthenorth elle woods CHER outfit customizer

from tkinter import *

# making window
root = Tk()
root.wm_title("Clueless")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()-75
root.geometry("%dx%d" % (width, height))

bg = tkinter.PhotoImage(file="leopard-bg.PNG")

#banner
banner = tkinter.Label(root, width="1000", height="50")
banner.place(x=0, y=0)
banner.config(bg='black')

chers = tkinter.Label(root, text="CHER'S WARDROBE", font=("Impact", 30), fg='white')
chers.place(x=0, y=0)
chers.config(bg='black')

cheetah = tkinter.Label(root, image=bg)
cheetah.place(x=0, y=50)

# show window
root.mainloop()


