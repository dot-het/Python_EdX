# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:44:11 2020

@author: dhet
"""


import string
alphabet = string.ascii_letters

#Create a dictionary count_letters with keys consisting of each unique letter 
#in the sentence and values consisting of the number of times each letter is used
#in this sentence. Count upper case and lower case letters separately in the dictionary.
# =============================================================================
def int(a,b):
    letters = str()
    for x in a:
        if x in b:
            letters = letters + x
    return letters

for i in range(len(com)):
    print(sent.count(com[i]),com[i], i)
    
# =============================================================================
#     counter function / giving an input and comparing the elements of the sentence
    # to the alphabet
# =============================================================================
def counter(inputs):
    #input_string = input('Please enter a string:\n')
    d = int(inputs, alphabet)
    for i in range(len(d)):
        print(inputs.count(d[i]),d[i],'ordernumber:', i)
# =============================================================================
# second counter for address 
# =============================================================================
  def counting(inputs):
    #input_string = input('Please enter a string:\n')
    d = int(inputs, alphabet)
        for i in range(len(d)):
            elements = (inputs.count(d[i]),d[i])      
            print(elements)
        
# =============================================================================
# 
# =============================================================================
import random

random.seed(1) # Fixes the seed of the random number generator.

def rand():
    #random.seed(1)
    return random.choice([1,2])

# =============================================================================
# Write a function distance(x, y) 
# that takes two vectors as its input and outputs the distance between them.
# Use your function to find the distance between  x=(0,0)  and  y=(1,1) .
# =============================================================================
#my code1
def distance1(x1,y1):
    d1 = math.sqrt(((x1-y1)**2)+((y1-x1)**2))
    #d2 = math.sqrt(((x2-y2)**2)+((y2-x2)**2))
    return d1

##mycode2
def distance(x, y):
        square_differences = [(x[i] - y[i])**2 for i in range(len(x))]
        return math.sqrt(sum(square_differences))
# =============================================================================
#Use your function to determine whether the point (1,1) lies 
#within the unit circle centered at (0,0):
    

def in_circle(x, origin = [0,0]):
    if distance(x, origin) < 1:
        return True
    else:
        return 
    print(in_circle((1,1)))
    False
    

# =============================================================================
# 
# =============================================================================
# Create a list inside of R=10000 booleans that determines whether or not a point 
#falls within the unit circle centered at (0,0).
inside = list(range(1,10001))
for i in range(10000): R.append(rand(-1,1))

#Set the seed to 1 using random.seed(1).
random.seed(1)
#Use the rand function from Exercise 2b to generate R randomly located points.
x = rand(1,10000)
z = 0
in_circle(x,z)

# =============================================================================
# 
# =============================================================================
#What is the proportion of points within the unit circle?
   def coordinate():
       return (rand(), rand())

for i in x: inside.append(in_circle(i, origin=(0, 0)))

random.seed(1) 

inside = []
R = 10000
for i in range(R):
    point = [rand(), rand()]
    inside.append(in_circle(point))
    
    
# =============================================================================
#A function moving_window_average(x, n_neighbors) that takes a list x and 
#the number of neighbors n_neighbors on either side of a given member of the list 
#to consider.
# =============================================================================
def moving_window_average(x, n_neighbors):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    n1 = len(x)
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values 
    #i from 0 to n-1.
    y =[x[i] for i in range(n1)]
    mean_x = [(x[i-1]+x[i]+x[i+1])/width for i in range(1,n1-1)]
    return mean_x, sum(mean_x)
x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))

#version 2
def moving_window_avg(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i:(i+width)]) / width for i in range(n)]