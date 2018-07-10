from random import randint
import pyautogui
import time
import math
import sys


def random_coordinate(x_lower,y_lower,x_range,y_range):
	"""Move cursor to a random location above the object to click"""
	x=randint(x_lower,x_lower+x_range)
	y=randint(y_lower,y_lower+y_range)
	
	return pyautogui.moveTo(x,y,0)


def random_wait_time(z_lower,z_range):
	z=randint(z_lower,z_lower+z_range)
	"""returns a random int"""
	time.sleep(z)
	
	return z

num=input("Enter number of clicks:")
num=int(num)
xcoord=int(input("Enter X coord:"))
ycoord=int(input("Enter Y coord:"))
rang=int(input("Enter Randomness:"))

x=0

while x<=num:
        random_coordinate(xcoord,ycoord,rang,rang)
        pyautogui.click(xcoord,ycoord)
        random_wait_time(1,2)
        x+=1
input('Press ENTER to exit')
