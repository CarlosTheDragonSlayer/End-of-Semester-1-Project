from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=1360,height=700, background='#BFF5ED')
drawpad.pack()
from PIL import Image, ImageTk
image = Image.open("Game BG.jpg")
photo = ImageTk.PhotoImage(image)
drawimg = drawpad.create_image(50,50,image=photo)

root.mainloop()