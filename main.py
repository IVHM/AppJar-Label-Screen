#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:18:27 2019

@author: hmatthyseniv
"""

from appJar import gui
from config import SCREEN
import display as ds
from display import Label_Screen, app

image = [[1,0,0,1],
         [1,0,0,1],
         [1,0,0,1],
         [0,1,1,0]
        ]


ds.build_screen("test", 4)
ds.test_screen("test")
ds.load_image("test",image)



app.go()