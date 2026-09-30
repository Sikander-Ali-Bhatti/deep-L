import numpy as np
 
x=np.array([1,2,3,4,5,])
y=x[:]
print(np.shares_memory(x,y))
z=x.copy()
print(np.shares_memory(x,z))