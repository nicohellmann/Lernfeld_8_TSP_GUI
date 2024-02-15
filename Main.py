from tkinter import *
from Point import Point
import random
route = []
def quit(window):
    window.quit()

def draw_point(event):
    global x,y
    global point_counter
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    x = (event.x)
    y = (event.y)
    can.create_oval(x,y,x,y,width=5,fill="black")
    can.create_text(x+7,y,text=letters[point_counter])
    point_counter +=1
    if point_counter >=26:
        point_counter =0

def click_corrdinates(event):
    global x,y
    x = (event.x)
    y = (event.y)
    print(str(x) +'/' +str(y))
def draw_cities():
    global point_counter
    
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    print(dot_input.get())
    city_count = int(str(dot_input.get()))
    for i in range(0,city_count):
        x = random.randint(0,500)
        y = random.randint(0,500)
        can.create_oval(x,y,x,y,width=5,fill="black")
        can.create_text(x+7,y,text=letters[point_counter])
        route.append(Point(x,y))
        point_counter +=1
        if point_counter >=26:
            point_counter =0


def draw_line(event):
    global click_number
    global x1,y1
    if click_number==0:
        x1 = event.x
        y1 = event.y
        click_number=1
    else:
        x2 = event.x
        y2 = event.y
        can.create_line(x1,y1,x2,y2,fill="blue")
        click_number=0
window = Tk()
dot_input = Entry(window)
exit_button= Button(window,text="Exit",background="red",command=lambda:quit(window))
tsp_button = Button(window,text="Cities", background="green",command=lambda:draw_cities())
can = Canvas(window,width=500, height=500)
exit_button.grid(row=0,column=0)
tsp_button.grid()
dot_input.grid()
can.bind("<Button-1>",click_corrdinates)
can.bind("<Button-1>",draw_point)

can.bind("<Button-3>",draw_line)
point_counter=0
click_number=0


can.grid()
mainloop()