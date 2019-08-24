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
from copy import deepcopy


app = gui(SCREEN["TITLE"],
          str(SCREEN["WIDTH"]) + "x" + str(SCREEN["HEIGHT"]))


def shutdown_check():
    app.destroyAllSubWindows()
    return True


app.setStopFunction(shutdown_check)


'''
Screen is setup like this with x and y axis swapped from their usual places
Allows you to draw in stacked arrays in a way that makes sense visually

    Y-->
      __________
 X   |0,0    0,n
 |   |
 V   |n,0

'''


# ----LABEL SCREEN ----
# Creates and displays a screen
class Label_Screen():
    def __init__(self, name,
                 size=PS_DEFAULTS["SIZE"],
                 height=PS_DEFAULTS["HEIGHT"],
                 color_map=PS_DEFAULTS["COLOR_MAP"]):
        # ---- INPUT VARIABLES
        self.name = name  # unique identifier for
        self.size = size  # Number of pixels in rows& cols
        self.height = height - height % size  # Size of the subwindow created
                                              
        # array of strings of color names ["blue", "red"...]
        self.color_map = deepcopy(color_map)
        
        self.drawing = False
        self.moving = False
        self.testing = False
        
        # ---- CONTAINERS ----
        self.pxl_map = []
        self.pc_col = 2
        
        # Intializes all pixels and sets to off 0
        for x in range(self.size):
            self.pxl_map.append([])
            for y in range(self.size):
                self.pxl_map[x].append(0)
        self.last_pxl_map = []  # Used to make sure we're only changing what needs to be changed

    # Shortcut for getting cell's label name
    def cell_name(self, x, y):
        return self.name + "_" + str(x) + "_" + str(y)

    # Create a 2d array of random pixel for testing
    def test_screen(self):
        if not self.testing:
            self.testing = True
            self.last_pxl_map = deepcopy(self.pxl_map)
            for x in range(self.size):
                r = randint(0, 2, self.size).tolist()
                self.pxl_map[x] = r
            self.testing = False
            self.draw()

    # Loads in a square array of values
    def load_pxl_map(self, image_data):
        print("Load pixl map called")
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
                if crnt_size != self.size:
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
            # This is where we load the arrays into
            self.last_pxl_map = deepcopy(self.pxl_map)
            self.pxl_map = deepcopy(image_data)
            self.draw()

    # 
    def mov_pxl(self, pos, last_pos, new_col, org_col):
        if not self.moving:
            self.moving = True
            self.last_pxl_map = deepcopy(self.pxl_map)
            self.pxl_map[last_pos[0]][last_pos[1]] = org_col
            self.pxl_map[pos[0]][pos[1]] = new_col
            
            app.openSubWindow(self.name)
            app.setLabelBg(self.cell_name(pos[0], pos[1]), 
                                          self.color_map[new_col])
            app.setLabelBg(self.cell_name(last_pos[0], last_pos[1]), 
                                          self.color_map[org_col])
            app.stopSubWindow()
            self.moving = False

    # Change a single pixels color 
    def update_pxl(self, x, y, color):
        self.last_pxl_map[x][y] = self.pxl_map[x]
        self.pxl_map[x][y] = color

        app.openSubWindow(self.name)
        app.setLabelBg(self.cell_name(x, y), self.color_map[color])
        app.stopSubWindow()

    # Called ONLY ONCE the first time we create this array

    def create(self):
        app.startSubWindow(self.name)
        app.setStopFunction(app.show)
        app.setStretch("both")
        app.setSticky("nesw")
        app.setSize(self.height, self.height)

        # Create the screen pixel's label entity
        for x in range(self.size):
            for y in range(self.size):
                crnt_lbl_name = self.cell_name(x, y)
                pxl_state = self.pxl_map[x][y]

                app.addLabel(crnt_lbl_name, crnt_lbl_name, x, y)
                app.setLabelBg(crnt_lbl_name, self.color_map[pxl_state])

        app.stopSubWindow()
        app.showSubWindow(self.name)

    # Called after every time the screen is updated with new data

    def draw(self):
        print("opened draw window")
        #self.diag("draw pxl maps")
        if not self.drawing:
            self.drawing = True
            app.openSubWindow(self.name)
            for x in range(self.size):
                for y in range(self.size):
                    if self.pxl_map[x][y] != self.last_pxl_map[x][y]:
                        pxl_state = self.pxl_map[x][y]
                        app.setLabelBg(self.cell_name(x, y),
                                       self.color_map[pxl_state])
            app.stopSubWindow()
            self.drawing = False
    
    # Prints out stats for testing
    def diag(self, note):
        print("\n----------------------------")
        print(note)  # Add a note for easier testing
        for i in range(self.size):
                print(self.pxl_map[i], "  |  ", self.last_pxl_map[i])
            