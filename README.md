# Menu-Game -WIP-
A completely useless pixel screen built around the appJar library. It's built utilizing a 2D array to initialize background color values in a square array of  appJar's label objects. With added methods for use in a variety of equally useless projects. 

AppJar is a powerful library that allows non-UI designers a chance to create a piece of python code that isn't just a bunch of incomprehensible terminal inputs and outputs that look like an Amiga-500 was having a seizure over it's alphabet soup. With such a powerful and useful library at your disposal one must conclude that it should be put to use doing, what can only be described as "a waste of your week" and "a stain upon open source developers everywhere". So here goes a feature extension to appJar, that literally nobody asked for and several people begged to stop.  



### Features:
**Resolution**: I don't know but like a square?
**Refresh rate**: 1hz - 1.2hz *If you ask nicely*.
**Multi-threading**: Nope, it can barely deal with one thread as is. 
**Commit history**: Ugh why even bother? 
**Demos**: Dude, do you like mazes!? NO?..Oh uh, well nevermind. 
**Extra Features**: The satisfaction of knowing where the bottom of the barrel is




## Mini-doc 
A short outline of the main class and it's features, because I'm struggling at this point to justify the week spent working on this thing and at least having some sort of documentation makes this feel even the smallest part official and legit. God me and my therapist have a lot to talk about this week, huh?

So if you want to use this, just take everything out of the display file and config file and dump it into your code like you're seven shots in and got nothing to lose.
See code examples for less hand wavey explanation.  

#### Label_Screen(self, name, size, height, color_map)
**name**- The name of the created subwindow in appJar, make sure it isn't used by any other subwindow or else appjar will throw a fit and not let you play with any of its toys
**size**- The number of labels per row, and also the number of rows  
**height**- How big the actual subWindow is in real life pixels, it's then trimmed down if you don't know how to find two numbers that are factors of each other, you git.
**color_map**- A list of color values in the format of words ie ["red", "blue", "orange"], look i'd like to do RGB values too, don't blame me, go take it up with jarvis

##### Class Methods
Without these this thing would be even more unusable than it already is

###### self.create()
Initializes all the labels for appJar to use, if you don't call it before any other method your code will not work and you will look more foolish than you did when you opened up this repository in the first place.

###### self.load_pxl_map(image_data)
Takes in a 2d array of values and loads it into the classes internal pixel map. If this is not the exact dimensions you specified when initializing the class it will not work, and you will look silly.
- **image_data**- This has got to be a list of integers, since it's referencing the values in your self.color_map list

###### self.mov_pxl(pos, last_pos, new_col, org_col)
Takes a pixel that used to be over there and moves it here. Or just changes the values of two specific pixels if you want to be pedantic about it.
- **pos & last_pos** - An array containing the x and y coords of the labels you want to change
- **new_col & org_col** - The location in your color_map variable you want to change the label's color to, or in other words, an integer

###### self.test_screen() 
Just generates a random image on your screen to make sure everything is working.
To be honest this is what it will look like if everything is not working too, so good luck.

###### self.update_pxl(x, y, color)
Updates the value of a single pixel. Now that I'm thinking about it you could basically just call this twice instead of using the mov_pxl method but at this point, does it really matter? Does anything matter? Is meaning and truth inherent in our world or are we all just floating sacks of purposeless atoms, bouncing around in a brownian soup of chaos till we reach our final blissful entropic dissipation. Also the color value is still an integer in case you were wondering.


###### self.diag(note)
Prints out the current and last pxl_map so you can figure out what part of your overactive reptilian brain got a little slap happy on the keyboard. 
- **note**- A string of text helping you find some sort of order in the chaotic dumpster fire we call our lives.


## Code Example
 
'''python
from display import Label_Screen, app  
# app must be imported or everything will fall apart

colors = ["white", "black", "pink"]  # Custom list of colors

# Initialize a Label_Screen object and start doubting your life decisions
screen = Label_Screen("God what are you doing", 4, 400, colors)

# Create the labels and build the screen, begin staring into the abyss
screen.create()  

# Make a function so our button can do something
def  testing_my_patience():
    screen.test_image()	

# Make a button so our function can do something
app.addButton(“testes uh i mean tester”, testing_my_patience)

# Starts the actual GUI, go see appJar documentation if you’re curious
app.go()

'''
Thanks to Jarvis for creating the actually useful library
[AppJar official documentation](appjar.info "A much better use of your time")