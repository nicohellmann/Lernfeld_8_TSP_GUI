from tkinter import *
global linex1,liney1
linex1 = 0
liney1 = 0
def quit(window):
    window.quit()

def draw_point(event):
    global x,y
    x = (event.x)
    y = (event.y)
    can.create_oval(x,y,x,y,width=5,fill="black")

def click_corrdinates(event):
    global x,y
    x = (event.x)
    y = (event.y)
    print(str(x) +'/' +str(y))

def bind_points(event):
    global x,y
    can.create_line(x,y,event.x,event.y,fill="orange")
    x = (event.x)
    y = (event.y)

def line_start(event):
    global linex1,liney1
    linex1,liney1 = event.x, event.y

def line_done(event):
    global linex2,liney2
    linex2,liney2 = event.x, event.y
    can.create_line(linex1,liney1,linex2,liney2)
window = Tk()

exit_button= Button(window,text="Exit",background="red",command=lambda:quit(window))
can = Canvas(window,width=500, height=500)
exit_button.grid(row=0,column=0)
can.bind("<Button-1>",click_corrdinates)
can.bind("<Button-1>",draw_point)
can.bind("<B1-Motion>",bind_points)
can.bind("<Button-2>",line_start)
can.bind("<ButtonRelease-2>",line_done)

can.grid()
mainloop()