from tkinter import *
from Point import Point
import random

def quit(window):
    window.quit()
####### --- Functions for mouse and Buttons --- #######
def draw_point(event):
    global x,y
    global point_counter
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    x = (event.x)
    y = (event.y)
    can.create_oval(x,y,x,y,width=5,fill="black")
    can.create_text(x+7,y,text=letters[point_counter])
    route.append(Point(x,y))
    point_counter +=1
    if point_counter >=26:
        point_counter =0
    print(len(route))

def draw_cities():
    global point_counter
    
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
    print(len(route))


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

def tsp():
    for i in range(len(route)-1):
        can.create_line(route[i].x,route[i].y,route[i+1].x,route[i+1].y,fill="blue")
    can.create_line(route[len(route)-1].x,route[len(route)-1].y,route[0].x,route[0].y,fill="blue")
####### --- window --- #######
window = Tk()
####### --- Input --- #######
dot_input = Entry(window)
####### --- Buttons --- #######
exit_button= Button(window,text="Exit",background="red",command=lambda:quit(window))
generate_cities_button = Button(window,text="add Cities", background="green",command=lambda:draw_cities())
tsp_button=Button(window,text="TSP",background="blue", command=lambda:tsp())
####### --- canvas --- #######
can = Canvas(window,width=500, height=500)
####### --- placing of Entry widgets, Labels, Buttons --- #######
exit_button.grid(row=0,column=0)
generate_cities_button.grid(row=1,column=0)
dot_input.grid()
tsp_button.grid()
can.grid()
####### --- binding functions and mouse input --- #######
can.bind("<Button-1>",draw_point)
can.bind("<Button-3>",draw_line)
####### --- variables --- #######
point_counter=0
click_number=0
route = []
####### --- mainloop --- #######
mainloop()