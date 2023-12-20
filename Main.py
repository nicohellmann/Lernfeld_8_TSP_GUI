from tkinter import *

def quit(window):
    window.quit()

def draw_point():
    pass
window = Tk()
exit_button= Button(window,text="Exit",background="red",command=lambda:quit(window))
can = Canvas(window,width=500, height=500)
exit_button.grid(row=0,column=0)
can.grid()
mainloop()