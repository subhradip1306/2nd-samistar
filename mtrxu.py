'''
You're given a 3x3 matrix
Find it's inverse
'''



'''
We're given a 3x3 matrix
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

# We only operate on the 2nd row if the it's 1st element is not 0
# Otherwise we are done

while MATRIX[1][0] != 0:
    
    if MATRIX[0][0] != 0:
# The if statement is necessary since we won't be able to find n if MATRIX[0][0] is 0
        
        n=MATRIX[1][0]/MATRIX[0][0]

        MATRIX[1]=c(a(MATRIX[1])-n*a(MATRIX[0]))
        
# We'll switch out the rows in case the 1st row's 1st element is zero
# to avoid the unnecessary (in this case) operation above 

    else:
        MATRIX[0]=l(a(MATRIX[0])-a(MATRIX[1]))
        MATRIX[1]=l(a(MATRIX[1])+a(MATRIX[0]))
        MATRIX[0]=l(a(MATRIX[1])-a(MATRIX[0]))
        
print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')

# Similarly for the 2nd row...
if MATRIX[2][0] != 0:
    
    if MATRIX[0][0] != 0:

        n=MATRIX[2][0]/MATRIX[0][0]

        MATRIX[2]=c(a(MATRIX[2])-n*a(MATRIX[0]))
        
        
    else: 
        MATRIX[0]=l(a(MATRIX[0])-a(MATRIX[2]))
        MATRIX[2]=l(a(MATRIX[2])+a(MATRIX[0]))
        MATRIX[0]=l(a(MATRIX[2])-a(MATRIX[0]))
        
print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')


if MATRIX[2][1] != 0:
    
    if MATRIX[1][1] != 0:

        n=MATRIX[2][1]/MATRIX[1][1]

        MATRIX[2]=c(a(MATRIX[2])-n*a(MATRIX[1]))
        

    else: 
        MATRIX[1]=l(a(MATRIX[1])-a(MATRIX[2]))
        MATRIX[2]=l(a(MATRIX[2])+a(MATRIX[1]))
        MATRIX[1]=l(a(MATRIX[2])-a(MATRIX[1]))
        
print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')
