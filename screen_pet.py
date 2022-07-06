"""Screen Pet"""
from tkinter import HIDDEN, NORMAL, Tk, Canvas

"""
if you want to hide a Tkinter canvas object, you must change the state of the object to HIDDEN, otherwise the state 
is normal

"""

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill') #first check to see what eye color (white is open and blue is closed)
    new_color = c.body_color if current_color == 'white' else 'white' #new color is the body color of pet if the eyes are currently open, if not then change to white
    current_state = c.itemcget(pupil_left, 'state') #checks the current state of pupil is NORMAL or HIDDEN
    new_state = NORMAL if current_state == HIDDEN else HIDDEN #if current is NORMAL then change to HIDDEN  and vice versa
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes() #close the eyes
    root.after(250, toggle_eyes) #wait 250 ms and open the eyes
    root.after(3000, blink) #wait 3000 ms and blink again

def toggle_pupils(): #code checks to see if eyes are crossed already
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False

def toggle_tongue():
    if not c.tongue_out: #if tongue_out is False, show the tongue and change flag to true
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:#else do the opposite
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False
def cheeky(event):
    toggle_tongue() #stick the tongue out
    toggle_pupils() #cross the pupils
    hide_happy(event)#hide the happy face
    root.after(1000, toggle_tongue) #put the tongue back in after 1000 ms
    root.after(1000, toggle_pupils) #uncross the eyss after 1000 ms
    return

def show_happy(event): #note that the event parameter signals to the program that this function is an event, an actual variable doesn't need to passed into the function when called
    if (20 <= event.x <= 350) and (20 <= event.y <= 350): #checks to see where mouse pointer is and if its over the mouth do below
        c.itemconfigure(cheek_left, state=NORMAL) #show the pink cheeks
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)#show the happy mouth
        c.itemconfigure(mouth_normal, state=HIDDEN) #hide the normal mouth
        c.itemconfigure(mouth_sad, state=HIDDEN)  #hide the sad mouith
    return

def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN) #hide the pink cheeks
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL) #show the normal mouth
    c.itemconfigure(mouth_sad, state=HIDDEN) #hide the sad mouth
    return

def sad():
    if c.happy_level == 0: #if there is no more happy level, make character sad
        print("hi")
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
        c.happy_level=10 #replenish once normal
    else:
        c.happy_level -= 2 #if not, then subtract from the happy level
    print(c.happy_level)
    root.after(5000, sad) #call sad again after 5000 ms

###############################################################MAIN FUNCTION###################################################
root = Tk()
c = Canvas(root,width=400,height=400)
c.configure(bg='dark blue',highlightthickness=0)

#draw the character
c.body_color = 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill= c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill= c.body_color)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
#remember that Tkinter gui upper left corner is (0,0) and bottom right is (400,400)
#CREATING A SAD MOUTH STATE THAT IS HIDDEN
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)
##DRAW TRHE TONGUE
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)


c.pack() #arranges things within the Tkinter window


# bind() https://www.pythontutorial.net/tkinter/tkinter-event-binding/       widget.bind(event,handler,add=None)
c.bind('<Motion>',show_happy) #<Motion> is the event that is passed into the function
c.bind('<Leave>',hide_happy)
c.bind('<Double--1>', cheeky) #event is a double click

c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False

root.after(1000,blink)#wait 1000 ms and start blinking
root.after(1000,sad)
root.mainloop()

