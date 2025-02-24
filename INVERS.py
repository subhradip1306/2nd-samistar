'''
INVERSINATOR
'''
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

def e(A,i,n,j):
    return c(a(MATRIX[i])-n*a(MATRIX[j]))

def p(A,i,j):
    A[i]=l(a(A[i])-a(A[j]))
    A[j]=l(a(A[j])+a(A[i]))
    A[i]=l(a(A[j])-a(A[i]))
    
    return (A[i],A[j])
    
'''
Now we generate a random matrix
and define the identity matrix
'''

MATRIX=[[r(),r(),r()], [r(),r(),r()], [r(),r(),r()]]
I=[[1,0,0],[0,1,0],[0,0,1]]

print(MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')


'''
We get to upper triangulating it
'''

# We only operate on the 2nd row if the it's 1st element is not 0
# Otherwise we are done

while MATRIX[1][0] != 0:
    
    if MATRIX[0][0] != 0:
# The if statement is necessary since we won't be able to find n if MATRIX[0][0] is 0
        
        n=MATRIX[1][0]/MATRIX[0][0]

        MATRIX[1]=e(MATRIX,1,n,0)
        I[1]=e(I,1,n,0)
        
# We'll switch out the rows in case the 1st row's 1st element is zero
# to avoid the unnecessary (in this case) operation above 

    else:
        (MATRIX[0],MATRIX[1])=p(MATRIX,0,1)
        (I[0],I[1])=p(I,0,1)


# Similarly for the 2nd row...
if MATRIX[2][0] != 0:
    
    if MATRIX[0][0] != 0:

        n=MATRIX[2][0]/MATRIX[0][0]

        MATRIX[2]=e(MATRIX,2,n,0)
        I[2]=e(I,2,n,0)
        
        
    else: 
        (MATRIX[0],MATRIX[2])=p(MATRIX,0,2)
        (I[0],I[2])=p(I,0,2)


if MATRIX[2][1] != 0:
    
    if MATRIX[1][1] != 0:

        n=MATRIX[2][1]/MATRIX[1][1]

        MATRIX[2]=e(MATRIX,2,n,1)
        I[2]=e(I,2,n,1)
        

    else: 
        (MATRIX[1],MATRIX[2])=p(MATRIX,1,2)
        (I[1],I[2])=p(I,1,2)
        
print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')





'''
We have an upper triangular matrix
Operate upon it to turn it into the identity matrix
'''


# We define a variable that stores whether there exists a 0 in the diagonal or not
# This is to check whether the matrix is even invertible or not

check=0

for i in range(len(MATRIX)):
    
    if MATRIX[i][i]==0:
        check=1

if check==1:
    print("The matrix is not invertible")
    
else:
    
    for j in range(len(MATRIX)):
        MATRIX[j]=c(a(MATRIX[j])/MATRIX[j][j])
        I[j]=c(a(I[j])/MATRIX[j][j])
    
    if MATRIX[1][2] != 0:
            
            m=MATRIX[1][2]
            MATRIX[1]=e(MATRIX,1,m,2)
            I[1]=e(I,1,m,2)
            
    if MATRIX[0][2] != 0:

            m=MATRIX[0][2]
            MATRIX[0]=e(MATRIX,0,m,2)
            I[0]=e(I,0,m,2)
            
    if MATRIX[0][1] != 0:

            m=MATRIX[0][1]
            MATRIX[0]=e(MATRIX,0,m,1)
            I[0]=e(I,0,m,1)
            

print('\n' ,MATRIX[0], MATRIX[1], MATRIX[2], sep='\n')
print('\n', I[0], I[1], I[2], sep='\n')
