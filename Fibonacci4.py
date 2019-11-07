""" First 10 Fibonacci no using lambda function 
name: Suman Nandi
Date: 06.11.2019"""

from math import *
s = [0,1]
a=lambda n:s[n] if n<2 else a(n-1)+a(n-2)
print ("First 10 Fibonacci no :")
for n in range(10):
 print (a(n))

