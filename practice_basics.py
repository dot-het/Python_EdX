# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:14:18 2020

@author: dhet
"""
#fill in the #blank# to ensure this prints 10.

def increment(n):
    n += 1
    print(10)
    
##
    class Mylist(list):
        def remove_min(self):
            self.remove(min(self))
        def remove_max(self):
            self.remove(max(self))
##
x1 = NewList([1,2,3])
while max(x1) < 10:
    x1.remove_max()
    x1.append_sum()
print(x1)
##
x = 20
not np.any([x%i == 0 for i in range(2, x)])
#x%i == 0 tests if x has a remainder when divided by i. If this is not true for 
#all values strictly between 1 and x, it must be prime!

# =============================================================================
# 
# =============================================================================
import random
import numpy as np
import matplotlib.pyplot as plt
rolls = []
for k in range(1000000):
    rolls.append(random.choice([1,2,3,4,5,6]))
plt.hist(rolls, bins = np.linspace(0.5,6.5,7))
 
##
import time
start = time.clock()
ys = []
for rep in range(1000000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
end = time.clock()
print(end - start)    
plt.hist(ys)

##

X = np.random.randint(1,7,(1,10))
Y = np.sum(X, axis = 1)
plt.hist(Y);

##
X_0 = np.array([[0],[0]])
delta_X = np.random.normal(0,1,(2,20000))
X = np.concatenate((X_0, np.cumsum(delta_X, axis = 1)), axis=1)
plt.plot(delta_X[0], delta_X[1], 'ro-')
#plt.savefig('rw2.pdf')

X
