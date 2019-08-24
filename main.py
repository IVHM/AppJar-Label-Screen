#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:18:27 2019
Runs the player character and map

@author: hmatthyseniv
"""

from appJar import gui
import time 
from random import randint
from config import SCREEN
import display as ds
from maps import MAPS
from display import Label_Screen, app
from config import SCREEN, PS_DEFAULTS
from enviroment import Agent


print("----->  Imports succesful\n")

# ---- DISPLAY CONTROL FUNCTIONS ----
active_screens = {}  # name IDed dictionary of all the label screens


def build_screen(name, size=PS_DEFAULTS["SIZE"],
                 color_map=PS_DEFAULTS["COLOR_MAP"]):
    global active_screens
    active_screens[name] = Label_Screen(name)
    active_screens[name].create()
    app.showSubWindow(name)


def load_image(name, image):
    active_screens[name].load_pxl_map(image)



# Maze game initializer
def maze_game():
    global pc
    map_screen = Label_Screen("Map")
    print("Map screen")

    pc = Agent(7, 6, MAPS[0], 2)

    def create_mov_controls():
        app.startSubWindow("Controls")
        print("COntrols window started")
        app.setSize(300, 200)
        app.addButton("Up", user_input)
        app.addButtons(["Left", "Right"], user_input)
        app.addButton("Down", user_input)
        app.addButtons(["Do1", "Do2"], user_input)
        app.stopSubWindow()
        app.showSubWindow("Controls")

    # ---- PLAYER CNTRL ----
    def user_input(button):
        dX, dY = 0, 0

        if button == "Up":
            dX = -1
        elif button == "Down":
            dX = 1
        elif button == "Left":
            dY = -1
        elif button == "Right":
            dY = 1
        elif button == "Do1":
            print("Did action 1")
        elif button == "Do2":
            print("Did action 2")
        else:
            print("How did you do that?")
        print("{button} button was pressed. ")
        pc.move(dX, dY)
        print("Moved player")
        map_screen.mov_pxl(pc.pos,
                        pc.last_pos,
                        pc.color,
                        pc.last_ground)
        print("loaded new position")


    map_screen.create()
    app.hide()
    map_screen.load_pxl_map(MAPS[0])
    map_screen.update_pxl(pc.pos[0], pc.pos[1], pc.color)
    create_mov_controls()

    

def disco_floor(name):
    print("Disco floor")

    def stahp_it():
        global dancing
        dancing = False

    app.startSubWindow("disco control")
    app.addButton("Oh stop", stahp_it)
    app.stopSubWindow()
    app.showSubWindow("disco control")

    disco_col = ["blue", "green", "orange", "yellow", "red", "pink"]
    floor = Label_Screen("Disco dan", 9, 800, color_map=disco_col)
    
    s = time.time()
    floor.create()
    fin = time.time() - s
    print(f"\n-----Loaded screen in {fin:.3f} seconds\n")

    tiles=[]
    for x in range(9):
        tiles.append([])
        for y in range(9):
            # Set each tile to a random color from the list
            tiles[x].append(randint(0, len(disco_col) - 1))
    
    
    dancing = 0
    refresh_rates = []
    


    def draw_floor():    
        global dancing
        if dancing < 30:
            s = time.time()  # Start timer
            for x in range(9):
                for y in range(9):
                    # Set each tile to a random color from the list
                    tiles[x][y] = randint(0, len(disco_col) - 1)
            floor.load_pxl_map(tiles)

            fin = time.time() - s 
            time.sleep(1)
            refresh_rates.append(fin)
            dancing+=1
            print(f"Frame: {len(refresh_rates)}  |  Secs:  {refresh_rates[-1]:.3f}")
            
    app.registerEvent(draw_floor)

    avg = 0
    for i in refresh_rates:
        avg += i
    avg /= len(refresh_rates)
    print("\n------------------------")
    print(f" Average Frame Rate : {avg:.3f}   Across {len(refresh_rates)} ")



# UI Styling ----
app.setStretch("both")
app.setSticky("news")

# MAIN SCREEN
app.addLabel("Welcome1", "Welcome to the useless screen demo")
app.addLabel("Welcome2", "Please choose an option.")
app.setLabelBg("Welcome1", "light blue")
app.setLabelBg("Welcome2", "light blue")
app.addHorizontalSeparator()
app.addButton("Start Maze", maze_game)
app.addButton("Disco Floor", disco_floor)
app.addButton("Exit", app.stop)

app.show()
app.go()
