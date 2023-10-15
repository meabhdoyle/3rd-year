#code adapted from 2 different articles from w3schools

# Python program to multiply two matrices 
import time
import random

# get the start time
st = time.time()
  
def mulMat(mat1, mat2, R1, R2, C1, C2): 
    # List to store matrix multiplication result 
    result = [[0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 0]] 
  
    for i in range(0, R1): 
        for j in range(0, C2): 
            for k in range(0, R2): 
                result[i][j] += mat1[i][k] * mat2[k][j] 
  
    print("Multiplication of given two matrices is:") 
    for i in range(0, R1): 
        for j in range(0, C2): 
            print(result[i][j], end=" ") 
        print("\n", end="") 
  
x = 0

# Driver code
while x <= 100:

    if __name__ == '__main__': 
        R1 = 2
        R2 = 2
        C1 = 2
        C2 = 2
        
        # First matrix
        mat1 = [[random.randint(1,10), random.randint(1,10)], 
            [random.randint(1,10), random.randint(1,10)],
            [random.randint(1,10), random.randint(1,10)]]
        
        
        # Second matrix
        mat2 = [[random.randint(1,10), random.randint(1,10)], 
            [random.randint(1,10), random.randint(1,10)],
            [random.randint(1,10), random.randint(1,10)]]
    
        if C1 != R2: 
            print("The number of columns in Matrix-1  must be equal to the number of rows in " + "Matrix-2", end='') 
            print("\n", end='') 
            print("Please update MACROs according to your array dimension in #define section", end='') 
            print("\n", end='') 
        else: 
            # Call matrix_multiplication function 
            mulMat(mat1, mat2, R1, R2, C1, C2)

        x+=1

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')