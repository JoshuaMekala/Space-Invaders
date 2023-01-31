import numpy as np
import matplotlib.pyplot as plt
import sys

command_line_arg = sys.argv[1]
#command_line_arg = "game1.txt"
#command_line_arg = "game2.txt" ### If you dont want to go into the command prompt
f1 = open(command_line_arg,"r") # Open whichever file was specified in command console
lines = f1.readlines()
red = np.loadtxt(command_line_arg, usecols=0)
blue = np.loadtxt(command_line_arg, usecols=1) 
green = np.loadtxt(command_line_arg, usecols=2)
mine = np.loadtxt(command_line_arg, usecols=3) # Read the text file and receive an array of alien kill values
x = np.loadtxt(command_line_arg)
max = np.max(x)
alien_list = []
for i in range(int(max)+1):
    alien_list.append(i) # List used to create the proper number on the y-axis
f1.close
plt.yticks(alien_list)
plt.plot(red,"^-r",blue,"^-b",green,"^-g", mine,"^-y")
plt.title(command_line_arg+"Statistics on Alien Killings")
plt.xlabel("Time Steps")
plt.ylabel("# Aliens Shot")
plt.legend(["red","blue","green","mine"])
plt.show() # Show the graph