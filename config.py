#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:19:20 2019

config file

@author: hmatthyseniv
"""

SCREEN = {
    "TITLE": "The Menu Game - WIP",
    "WIDTH": 350,
    "HEIGHT": 200

}

PS_DEFAULTS = {
    "HEIGHT": 801,
    "SIZE": 9,
    "COLOR_MAP": ["White", "Black", "Red", "Green", "Yellow"]

}
# This adjusts the height so it's a factorable by size
PS_DEFAULTS["HEIGHT"] -= PS_DEFAULTS["HEIGHT"] % PS_DEFAULTS["SIZE"]
