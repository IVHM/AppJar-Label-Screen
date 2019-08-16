#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:15:12 2019

HOLDS ALL THE COMPONENTS NEED FOR DISPLAY

Square screen made of label grid
    +Takes in a a 3d array and outputs label based screen



@author: hmatthyseniv
"""
from appJar import gui
from config import SCREEN, PS_DEFAULTS
from numpy.random import randint


app = gui(SCREEN["TITLE"],
          str(SCREEN["WIDTH"]) + "x" + str(SCREEN["HEIGHT"]))


# ----LABEL SCREEN ----
# Creates and displays a screen
class Label_Screen():
    def __init__(self, name, size=PS_DEFAULTS["SIZE"],
                 color_map=PS_DEFAULTS["COLOR_MAP"] ):
        # ---- INPUT VARIABLES
        self.name = name  # unique identifier for
        self.size = size  # Number of pixels in rows& cols
        self.color_map = color_map  #array of strings of color names ["blue", "red"...]

        # ---- CONTAINERS ----
        self.pxl_map = []
        # Intializes all pixels and sets to off 0
        for x in range(self.size):
            self.pxl_map.append([])
            for y in range(self.size):
                self.pxl_map[x].append(0)
        self.last_pxl_map = [] # Used to make sure we're only changing what needs to be changed


    # Create a 2d array of random pixel for testing
    def test_screen(self):
        self.last_pxl_map = self.pxl_map[:]
        for x in range(self.size):
            r = randint(0, 2, self.size).tolist()
            self.pxl_map[x] = r
            print(r)
            print("test screen px map: \n",self.pxl_map, "\n",self.last_pxl_map)


        # Loads in a square array of values
    def load_pxl_map(self, image_data):
        is_square = None
        if len(image_data) != self.size:
            is_square = False
            print('--------------------------------',
                  "Array in is wrong size.\n",
                  "Got: ", len(image_data), "   Need: ", self.size, '\n',
                  '--------------------------------')

        # Make sure we are getting a square array
        if is_square == None:
            for i in range(self.size):
                crnt_size = len(image_data[i])
                if  crnt_size != self.size:
                    is_square = False
                    print("\n----------------------------------------\n",
                          "Image is not a square image.\n",
                          "There was a ", crnt_size - self.size, "discrepency.\n",
                          "In row ", i, ".\n",
                          "----------------------------------------\n"
                          )
                    break
                else:
                    is_square = True

        if is_square:
            ## This is where we load the arrays into
            self.last_pxl_map = self.pxl_map[:]
            self.pixel_map = image_data

    # Called ONLY ONCE the first time we create this array
    def create(self):
        app.startFrame(self.name)
        for x in range(self.size):
            for y in range(self.size):
                crnt_lbl_name = self.name + str(x) + str(y)
                pxl_state = self.pxl_map[x][y]

                app.addLabel(crnt_lbl_name, "", x, y)
                app.setLabelBg(crnt_lbl_name, self.color_map[pxl_state])
        app.stopFrame()
        app.setFrameWidth(self.name,800)
        app.setFrameHeight(self.name, SCREEN["WIDTH"])


    # Called after every time the screen is updated with new data
    def draw(self):
        app.openFrame(self.name)
        print("opened draw frame")
        for x in range(self.size):
            for y in range(self.size):
                print(self.pxl_map[x][y], self.last_pxl_map[x][y])
                if self.pxl_map[x][y] != self.last_pxl_map[x][y]:
                    crnt_lbl_name = self.name + str(x) + str(y)
                    pxl_state = self.pxl_map[x][y]
                    print("set pixel (", crnt_lbl_name, ") to ", pxl_state)
                    app.setLabelBg(crnt_lbl_name, self.color_map[pxl_state])
        app.stopFrame()
#############################################################################


# ----DISPLAY CONTROL FUNCTIONS
active_screens = {}  # name IDed dictionary of all the label screens


def build_screen(name, size=PS_DEFAULTS["SIZE"],
                 color_map=PS_DEFAULTS["COLOR_MAP"]):
    global active_screens
    active_screens[name] = Label_Screen(name, size, color_map)
    active_screens[name].create()


def load_image(name,image):
    active_screens[name].load_pxl_map(image)
    active_screens[name].draw()


def test_update(name):
    name = name[4:]
    active_screens[name].test_screen()
    active_screens[name].draw()
    print("test update called")

def test_screen(name):
    a = app.getRow()
#    active_screens[name].test_screen()
#    active_screens[name].draw()
    app.addButton("test" + name, test_update,4)
    print(active_screens[name].name, active_screens[name].pxl_map )



