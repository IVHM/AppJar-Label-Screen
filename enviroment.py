"""
Created on Fri Aug 16 20:19:23 2019

COntains information about the world and actors

@author: hmatthyseniv
"""

class Agent():

    def __init__(self, x, y, world_map, color):
        self.pos = [x, y]
        self.ground = world_map[x][y]
        self.world_map = world_map[:]
        self.last_pos = self.pos[:]  # Used to track changes in the screen
        self.color = color
        self.last_ground = self.ground

    def update_map(self,new_map):
        self.world_map = new_map[:]

    def teleport(self, x, y):
        self.last_pos = self.pos[:]
        self.pos = [x,y]

    def move(self, dX, dY):
        new_X = self.pos[0] + dX
        new_Y = self.pos[1] + dY
        if self.world_map[new_X][new_Y] == 0:
            self.last_pos = self.pos[:]
            self.pos = [new_X, new_Y]
            self.last_ground = self.ground
            self.ground = self.world_map[new_X][new_Y]
        else:
            print("Bump")

