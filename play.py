# EGG GAME 
# Made by Eshaan Buddhisagar
# install pygame before using
print("Thank you for playing the Egg Game!\nVersion 2.0")
print("Make sure you line up the eggs exactly with the catcher!")
from tkinter import messagebox
from tkinter import * # import tkinter
import pickle # import pickle for loading high-score
FILENAME = 'highscore.eggfile'
hscoref = open(FILENAME, 'rb')
hscore = pickle.load(hscoref)
try:
    import random, time, pygame # import random module for egg spawning, time for waiting between spawns, pygame for music
    pygameworks = True
except ModuleNotFoundError:
    pygameworks = False
tk = Tk() # create Tk window
tk.title("Egg Game") # set title
def highscore():
    messagebox.showinfo('High Score', 'Your high score is '+str(hscore))
def tkinfo():
    messagebox.showinfo('Egg Info', 'Copyright © 2024 by Eshaan Buddhisagar, Crea\
ted in 2024 using Python. Drawings except for egg were created with Procreate. \
Code by Eshaan Buddhisagar.')
newscore = None
infoshow = Button(tk, text="Show Info...", command=tkinfo)
infoshow.pack()
if pygameworks:
    pygame.mixer.init()
    bgmusic = pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
hscoreb = Button(tk, text="Show High Score", command=highscore)
hscoreb.pack()
eggfile = PhotoImage(file="egg.png") # import egg image
catchfile = PhotoImage(file="catcher.png") # import catcher image
bgfile = PhotoImage(file="bg.png") # import background
canvas = Canvas(tk, width=600, height=600, highlightthickness=0, border=0) # create canvas
canvas.pack() # pack
def callback():
    print("""
This is a warning message from the Egg Game.
Click the Stop Game button to close the game.
Do not click the '[X]' or '(x)' button to close.
""")
def endegggame():
    global score, hscore, oldscore, FILENAME
    endinggame = messagebox.askyesno(title="Ending Game", message="Do you want to end the Egg Game?")
    if endinggame:
        hscoref.close()
        if score > hscore:
            oldscore = hscore+0
            hscore = score+0
            filew = open(FILENAME, 'wb')
            DUMP_OBJECT = pickle.dumps(hscore)
            filew.write(DUMP_OBJECT)
            filew.close()
            messagebox.showinfo("YAY!", f"You beat the high score of {oldscore}. Your score was {hscore}.")
        messagebox.showwarning('Game Ending', 'The game is ending.')
        quit()
        del hscore, score, oldscore, DUMP_OBJECT, FILENAME, filew
        del egg1, egg2, egg3, egg4
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        print('Game Over - Game Over - Game Over - Game Over - Game Over - ')
        pygame.mixer.music.pause()
        tk.destroy()
    else:
        messagebox.showinfo('Game Continuing', 'The game is continuing. Click the game window to keep playing.')
endgame = Button(tk, text="Stop Game", command=endegggame)
endgame.pack()
tk.protocol("WM_DELETE_WINDOW", endegggame)
bgid = canvas.create_image(0, 0, anchor=NW, image=bgfile) # create background
score = 0 # set score to 0
scoreid = canvas.create_text(500, 15, text=f"Egg Points: {score}", font=('Avenir', 30),
                             fill='black') # place score text

class Egg: # create Egg class
    def __init__(self, pos, imgid): # __init__ method
        self.x = pos[0] # set self.y to first object in list
        self.y = pos[1] # set self.x to second object in list
        self.id = imgid # set image self.id to id
    def update(self): # create update function (moves eggs down)
        self.y += 31 # move y down by 31
        canvas.move(self.id, 0, 31) # move on-screen

class Catcher: # Catcher class
    def __init__(self, pos, imgid): # __init__ method
        self.x = pos[0] # set self.y to first object in list
        self.y = pos[1] # set self.x to second object in list
        self.id = imgid # set image self.id to id
    def left(self, event): # create catcher left function
        canvas.move(self.id, -17, 0) # move on-screen
        self.x -= 7 # update y
    def right(self, event): # create catcher right function
        canvas.move(self.id, 17, 0) # move on-screen
        self.x += 7 # update y
        
def newegg(eggnum, class0='Egg'): # create function to replace existing eggs with new ones at the top of screen
    global egg1, egg2, egg3, egg4, eggid1, eggid2, eggid3, eggid4, catch, canvas # global variables
    try: 
        randomint = random.randint(99, 500) # create random number
        if eggnum == 1: # if provided num refers to egg1
            if str(type(egg1)) == f"<class '__main__.{class0}'>": # check if it's already an Egg
                canvas.delete(eggid1) # then delete it
            eggid1 = canvas.create_image(randomint, 0, anchor=NW, image=eggfile) # create the id again
            egg1 = Egg([randomint, 0], eggid1) # create another object of Egg
        elif eggnum == 2: # if provided num refers to egg2
            if str(type(egg2)) == f"<class '__main__.{class0}'>": # check if it's already an Egg
                canvas.delete(eggid2) # then delete it
            eggid2 = canvas.create_image(randomint, 0, anchor=NW, image=eggfile) # create the id again
            egg2 = Egg([randomint, 0], eggid2) # create another object of Egg
        elif eggnum == 3: # if provided num refers to egg3
            if str(type(egg3)) == f"<class '__main__.{class0}'>": # check if it's already an Egg
                canvas.delete(eggid3) # then delete it
            eggid3 = canvas.create_image(randomint, 0, anchor=NW, image=eggfile) # create the id again
            egg3 = Egg([randomint, 0], eggid3) # create another object of Egg
        elif eggnum == 4: # if provided num refers to egg4
            if str(type(egg4)) == f"<class '__main__.{class0}'>": # check if it's already an Egg
                canvas.delete(eggid4) # then delete it
            eggid4 = canvas.create_image(randomint, 0, anchor=NW, image=eggfile) # create the id again
            egg4 = Egg([randomint, 0], eggid4) # create another object of egg
        return 1 # if function worked
    except:
        return 0 # if error occured
eggid1, eggid2, eggid3, eggid4 = 0, 0, 0, 0 # set variables to blank integers (0)
egg1, egg2, egg3, egg4 = 1, 1, 1, 1 # set eggs to blank integers (1)
catcherid = canvas.create_image(0, 470, anchor=NW, image=catchfile) # create catcher id
catch = Catcher([0, 470], catcherid) # create Catcher object
tk.bind("<Left>", catch.left) # set the left arrow key to left catcher
tk.bind("<Right>", catch.right) # set the right arrow key to right catcher
gameon = True
def multicheckeggs():
    global score, scorecounts, canvas, score
    global score
    t1, t2, t3, t4 = False, False, False, False
    if egg1.y > 350 and egg1.x > catch.x+110 and egg1.x < catch.x+315: # check if touching
        score += 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}") # change text
        t1 = True # needs replacing
    if egg2.y > 350 and egg2.x > catch.x+110 and egg2.x < catch.x+315: # check if touching
        score += 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}") # change text
        t2 = True # needs replacing
    if egg3.y > 350 and egg3.x > catch.x+110 and egg3.x < catch.x+315: # check if touching
        score += 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}") # change text
        t3 = True # needs replacing
    if egg4.y > 350 and egg4.x > catch.x+110 and egg4.x < catch.x+315: # check if touching
        score += 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}") # change text
        t4 = True # needs replacing
        
    if egg1.y > 550: # if below screen
        t1 = True # replace
        score -= 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}")
    if egg2.y > 550: # if below screen
        score -= 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}")
        t2 = True # replace
    if egg3.y > 550: # if below screen
        score -= 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}")
        t3 = True # replace
    if egg4.y > 550: # if below screen
        score -= 1 # update score
        canvas.itemconfigure(scoreid, text=f"Egg Points: {score}")
        t4 = True # replace
    
    return t1, t2, t3, t4 # return replace values
def simplecheck(num): # define simple function to get value of one egg
    return list(multicheckeggs())[num-1] # return list of multi check function with indice of egg num
def update_game(): # like a main loop
    simplereplace() # replaces eggs that need replacing
    egg1.update() # move egg down
    egg2.update() # move egg down
    egg3.update() # move egg down
    egg4.update() # move egg down
    tk.after(600, update_game) # do function again after 600 milliseconds
def simplereplace(start=False): # function to replace eggs if they need replacing
    global eggid1, eggid2, eggid3, eggid4, egg1, egg2, egg3, egg4 # global variables
    if start: # if game just started and eggs need creating
        eggid1 = canvas.create_image(300, 100, anchor=NW, image=eggfile) # create id
        egg1 = Egg([300, 100], eggid1) # create Egg
        eggid2 = canvas.create_image(100, 300, anchor=NW, image=eggfile) # create id
        egg2 = Egg([100, 300], eggid2) # create Egg
        eggid3 = canvas.create_image(400, 400, anchor=NW, image=eggfile) # create id
        egg3 = Egg([400, 400], eggid3) # create Egg
        eggid4 = canvas.create_image(300, 300, anchor=NW, image=eggfile) # create id
        egg4 = Egg([300, 300], eggid4) # create Egg
    else: # if eggs need replacing
        if simplecheck(1): # check eggs
            newegg(1) # new egg
        if simplecheck(2): # check eggs
            newegg(2) # new egg
        if simplecheck(3): # check eggs
            newegg(3) # new egg
        if simplecheck(4): # check eggs
            newegg(4) # new egg
simplereplace(True) # create new eggs
update_game() # loop
tk.mainloop() # Tk mainloop to update images and classes
