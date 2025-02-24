'''
You're given a 3x3 matrix
Operate on it to make it upper triangular
'''

import random as rn
import numpy as np

'''
Just about all the operations we'll need
'''

def r():
    return rn.randint(0,9)

def a(x):
    return np.array(x)

def l(x):
    return list(x)

def c(x):
    return [int(x[0]), int(x[1]), int(x[2])]
    
    
'''
Now we generate a random matrix
'''
MATRIX=[[r(),r(),r()], [r(),r(),r()], [r(),r(),r()]]

print(MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')

'''
We get to actually upper triangulating it
'''


while MATRIX[1][0] != 0:
    
    if MATRIX[0][0] != 0:

        n=MATRIX[1][0]/MATRIX[0][0]

        MATRIX[1]=c(a(MATRIX[1])-n*a(MATRIX[0]))
        
        

        
# We'll switch out the rows
# since the first element of the first row is already zero  

    else: 
        MATRIX[0]=l(a(MATRIX[0])-a(MATRIX[1]))
        MATRIX[1]=l(a(MATRIX[1])+a(MATRIX[0]))
        MATRIX[0]=l(a(MATRIX[1])-a(MATRIX[0]))
        
print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')


if MATRIX[2][0] != 0:
    
    if MATRIX[0][0] != 0:

        n=MATRIX[2][0]/MATRIX[0][0]

        MATRIX[2]=c(a(MATRIX[2])-n*a(MATRIX[0]))
        
        

        
# We'll switch out the rows
# since the first element of the first row is already zero  

    else: 
        MATRIX[0]=l(a(MATRIX[0])-a(MATRIX[2]))
        MATRIX[2]=l(a(MATRIX[2])+a(MATRIX[0]))
        MATRIX[0]=l(a(MATRIX[2])-a(MATRIX[0]))
        
print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')


if MATRIX[2][1] != 0:
    
    if MATRIX[1][1] != 0:

        n=MATRIX[2][1]/MATRIX[1][1]

        MATRIX[2]=c(a(MATRIX[2])-n*a(MATRIX[1]))
        
        

        
# We'll switch out the rows
# since the first element of the first row is already zero  

    else: 
        MATRIX[1]=l(a(MATRIX[1])-a(MATRIX[2]))
        MATRIX[2]=l(a(MATRIX[2])+a(MATRIX[1]))
        MATRIX[1]=l(a(MATRIX[2])-a(MATRIX[1]))
        
print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')