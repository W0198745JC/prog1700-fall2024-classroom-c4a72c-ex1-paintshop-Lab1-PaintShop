# LAB 1 - THE PAINT SHOP
# Code a Python program that calculates the amount of paint you need to cover the walls in your family room. 
# The salesperson at the home improvement store told you to buy 1 gallon of paint for every 150 square feet of 
# wall you need to paint.

# Assuming that the room is rectangular in shape, the program should take in as input the width of your 
# two sets of walls and the height of the room.

# The program should output the number of gallons required to paint the room. 
# Paint is sold only by the gallon.

#Purpose/Concepts: Input and output to screen, string concatentation, datatype casting, simple math operations

print("Welcome to the Paint Shop Calculator")
# how wide is the longer wall
Wall1= input("what is the width of your long wall in ft?")
#how wide is the shorter wall
Wall2= input("what is the width of your short wall in ft?")
#what is the height of the room
Height = input("what is the height of your wall in ft?")
#footage of wall 1
Size1 = int(Wall1)*int(Height)
#footage of wall 2
Size2 = int(Wall2)*int(Height)
# get the square footage of the room
size = Size1*2 + Size2*2
#divide by 150 and round to the nearest 1
gallons=round(size/150)
#print the needed amount
print(("You will need to buy ")+str(gallons)+(" gallon(s) to paint your room"))