""" First 10 Fibonacci no 
name: Suman Nandi
Date: 06.11.2019"""

from math import *
s = [0,1]
for i in range(2,10):
    s.append(s[i-1] + s[i-2])
print ("First 10 Fibonacci no :",s)    
