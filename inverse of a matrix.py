#Program to find the inverse of a matrix.
#Developed by: SRIJITH R
#RegisterNumber: 21004191
import numpy as np
a=np.array([[2,1,1],[1,1,1,],[1,-1,2]])
values=np.linalg.inv(a)
print(values)