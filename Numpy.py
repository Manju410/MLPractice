#Numpy - Numerical Python

import numpy as np

a = [3,5,9]
print(a)
type(a)

a = np.array([3.5,5,9])
print(a)
type(a) # N-Dimensional Array

# one dimension array
a = np.array([3,5,9])
print(a)
print("Dimension :",a.ndim) # dimension of array
print("Dtype :",a.dtype)# datatype of array
print("Size :",a.size) # size of array
print("Shape :",a.shape) # elements in each Dimension

# 2-D array is collection of 1-D arrays
a = np.array([ [3,5,9,4] , [4,6,4,7], [4,5,7,3] ] )
print(a)
print("Dimension :",a.ndim)
print("Dtype :",a.dtype)
print("Size :",a.size)
print("Shape :",a.shape) # elements in each Dimension


# 3-D array is collection of 2-D arrays
a = np.array([
             [[3,5,9,4],[4,6,4,7],[4,5,7,3]],
             [[8,3,2,1],[6,6,8,7],[3,8,3,6]]
             ])
print(a)
print("Dimension :",a.ndim)
print("Dtype :",a.dtype)
print("Size :",a.size)
print("Shape :",a.shape) # elements in each Dimension


a[1][0][2] # [1] - 3D index, [0] - 2-D index..




# np.arange( )
#Generates a sequencial array


np.arange(10) # Generates sequencial array of 10 numbers
np.arange(10,20) # Generates Sequencial array of between 10 to 20
np.arange(10,20,2) # Generates Sequencial array of between 10 to 20 with 2 step size


# reshape( )
# Reshaping the array
a = np.arange(24)
a.reshape(4,6) # reshaping 24 elements array into 4X6 matrics

# ravel( )
# undoing back to original matrics
a.ravel()

# np.random.random()
# selecting random numbers from array
np.random.random()

int(35 + (100-35)*np.random.random())
np.random.randint(35,100,10)
marks = np.random.randint(35,100,100).reshape(20,5)

np.floor(4.7) # round of to below number
np.ceil(4.3) # round of to above number
np.round(4.3) # round of to .5 
