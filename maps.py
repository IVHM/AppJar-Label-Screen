#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:58:17 2019

@author: hmatthyseniv
"""

from config import PS_DEFAULTS

MAPS =  [
       [
      [1,	1,	1,	1,	1,	1,	1,  1,  1],
      [1,	0,	0,	0,	1,	1,	0,	1,  1],
      [1,	0,	1,	0,	0,	0,	0,	1,  1],
      [1,	1,	1,	1,	1,	1,	0,	1,  1],
      [1,	0,	0,	0,	0,	1,	0,	1,  1],
      [1,	0,	1,	1,	0,	0,	0,	1,  1],
      [1,	0,	1,	1,	1,	1,	1,	1,  1],
      [1,	0,	0,	0,	0,	0,	0,	1,  1],
      [1,	1,	1,	1,	1,	1,	1,	1,  1]
       ],

        ]


# Test_image

test_image = []
for x in range(PS_DEFAULTS["SIZE"]):
    if x%2 == 0:
        pxl = 0
    else:
        pxl = 1
    test_image.append([])
    for y in range(PS_DEFAULTS["SIZE"]):
        test_image[x].append(pxl)

