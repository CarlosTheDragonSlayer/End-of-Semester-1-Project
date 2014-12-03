from Tkinter import *
root = Tk()

dir1 = "C:\Users\Aubrey\Documents\GitHub\End of Semester 1 Project\End-of-Semester-1-Project\\"

drawpad = Canvas(root, width=1360,height=700, background='#BFF5ED')
drawpad.pack()
gif1 = PhotoImage(file = 'C:\Users\Aubrey\Documents\GitHub\End of Semester 1 Project\End-of-Semester-1-Project\Player.gif')
drawpad.create_image(700, 100, image = gif1)

root.mainloop()