from tkinter import *
def conv():
    m=float(miles.get())
    km = 1.609*m
    l4.config(text=f"{km}")


window = Tk()
window.title("Miles to kilometer converter")

miles = Entry()
miles.grid(column=1,row=0)
ll = Label(text="enter miles")
ll.grid(column=0 , row=0 )

l1 = Label(text="Miles")
l1.grid(column=2 , row=0)
l2 = Label(text=" is equal to ")
l2.grid(column=0 , row=1)
l3 = Label(text="kilometers")
l3.grid(column=2 , row=1)
b1 = Button(text="convert",command=conv)
b1.grid(column=1 , row=2)
l4 = Label(text="0")
l4.grid(column=1 , row=1)


window.mainloop()