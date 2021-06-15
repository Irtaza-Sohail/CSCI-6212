#!/usr/bin/env python
# coding: utf-8

# In[19]:


from decimal import *
from timeit import default_timer as timer

getcontext().prec = 20 #Modify this to set precision as high or low as you want
getcontext().Emax = 9999999999999 


# Implementation of nth power of a complex number
  
 
 # Function to return the product of two numbers
def mult(sq1, sq2):
  
    ans = sq1*sq2
  
    return ans
  
# Function to return the complex number in polar form raised to the power n
def power(magn, n):
  
    if (n == 0):
        magn = 1
        return magn
      
#base case for z=1
    if (n == 1):
        return magn
  
    # Recursive call for n/2
    sq = power(magn, n // 2)
    if (n % 2 == 0):
        return mult(sq, sq)
    return mult(magn, mult(sq, sq))
  
def main():
  
    # Magnitude of the complex number in polar form
    #magn = Decimal(5)
  
    # Angle of the complex number in polar form
    #angle = Decimal(45)
    n_times = []
    n_values = [10,100,1000,2000,5000,10000,100000,1000000,10000000] #modify to test for different values of n
    #power
    for n in n_values:
        
        
        magn = Decimal(5)
        angle = Decimal(45)
        n = Decimal(n)
        
        start = timer()
        
        z = Decimal(power(magn, n))
        #print(round(z,5), " <Angle> ( ", round(n*angle,5), " )°")
        
        end = timer()
        e_time = end - start
        n_times.append(e_time)
    
    #n = Decimal(10000000000000)
    for i in range(len(n_times)):
        print("Value of n = ", n_values[i], ", Execution Time = ", n_times[i], "seconds")

main()



# In[ ]:




