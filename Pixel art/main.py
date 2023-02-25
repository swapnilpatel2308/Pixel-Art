
from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import Image,ImageDraw
main_window = tk.Tk()
main_window.geometry("600x650+20+20")
main_window.title("Draw Pixel")
main_window.resizable(False,False)
canvas = Canvas(main_window,background="#ffffff",width=600,height=600)
canvas.place(x=0,y=0)
color = "#ff0000"
rect_list = []
for j in range(60):
    for i in range(60):
        rect_list.append(canvas.create_rectangle(10*i,j*10,10*i+10,10*j+10,width=1,outline="#000000"))

def run(e):
    global color
    global size
    global box_size
    if(e.x<=600 and e.y<=600 and e.x>=0 and e.y>=0):
        a = (size*(e.y//box_size))+(e.x//box_size)
        canvas.itemconfig(rect_list[a],fill=color)
    
def set_color(c):
    global color
    color = c

red_color = Button(main_window,width=1,height=1,text="",background="#ff0000",command=lambda:set_color("#ff0000"))
red_color.place(x=10,y=610)

green_color = Button(main_window,width=1,height=1,text="",background="#00ff00",command=lambda:set_color("#00ff00"))
green_color.place(x=30,y=610)

blue_color = Button(main_window,width=1,height=1,text="",background="#0000ff",command=lambda:set_color("#0000ff"))
blue_color.place(x=50,y=610)

yellow_color = Button(main_window,width=1,height=1,text="",background="#ff00ff",command=lambda:set_color("#ff00ff"))
yellow_color.place(x=70,y=610)

pink_color = Button(main_window,width=1,height=1,text="",background="#00ffff",command=lambda:set_color("#00ffff"))
pink_color.place(x=90,y=610)

as_color = Button(main_window,width=1,height=1,text="",background="#9FE2BF",command=lambda:set_color("#9FE2BF"))
as_color.place(x=110,y=610)

black_color = Button(main_window,width=1,height=1,text="",background="#000000",command=lambda:set_color("#000000"))
black_color.place(x=130,y=610)

white_color = Button(main_window,width=1,height=1,text="",background="#55cc22",command=lambda:set_color("#55cc22"))
white_color.place(x=150,y=610)

size_l = Label(main_window,text="select size",font=font.BOLD)
size_l.place(x=180,y=610)

n = tk.StringVar()
size_list = ttk.Combobox(main_window, width = 10, textvariable = n,font=font.BOLD)
size_list.place(x=280,y=610)

size_list['values'] = ("5x5","6x6","8x8","10x10","12x12","15x15","20x20","25x25","30x30","40x40","60x60")
size_list.current(10)

box_size = 10
size = 60
def set_grid():
    global size
    a = n.get().split("x")
    size = int(a[0])
    global rect_list
    global box_size
    rect_list = []
    canvas.delete("all")
    box_size = 600//size
    for j in range(size):
        for i in range(size):
            rect_list.append(canvas.create_rectangle(box_size*i,j*box_size,box_size*i+box_size,box_size*j+box_size,width=1,outline="#000000"))

set_btn = Button(main_window,text="Set",command=set_grid,width=5)
set_btn.place(x=420,y=610)

def save():
    global size
    global rect_list
    global box_size
    img= Image.new("RGB",(600,600),color="#ffffff")
    img1 = ImageDraw.Draw(img)
    for i in range(size):
        for j in range(size):
            a = canvas.itemcget(rect_list[i*size+j],"fill")
            if(a==""):
                a = "#ffffff"
            img1.rectangle([(box_size*i,j*box_size),(box_size*i+box_size,box_size*j+box_size)],fill=f"{a}",width=1)
    img.show()
  

save_btn = Button(main_window,text="Save",width=6,command=save)
save_btn.place(x=470,y=610)

canvas.bind("<B1-Motion>",run)
main_window.mainloop()