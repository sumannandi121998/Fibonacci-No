""" Module of n Fibonacci no 
name: Suman Nandi
Date: 06.11.2019"""

from math import *
def f(n):
 s = [0,1]
 for i in range(2,n):
  s.append(s[i-1] + s[i-2])
 return s   
    

