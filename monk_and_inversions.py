"""
Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size N x N for his birthday. Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array. Now, Micro has asked Monk to find out the number of inversion in the matrix M. Number of inversions, in a matrix is defined as the number of unordered pairs of cells {(i,j), (p,q)} such that M[i][j]>M[p][q] & i<=p & j <= q.
Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.
"""
#Solution 
test = input()  


for i in range(int(test)):
    matrix_size = int(input())
    temp =[0]*matrix_size
    count = 0
    for j in range(matrix_size):
        temp[j] = [int(x) for x in input().split()]
    
    for j in range(matrix_size):
        for k in range(matrix_size):
            for p in range(j, matrix_size):
                for q in range(k, matrix_size):
                    if temp[j][k] > temp[p][q]:
                        count +=1

    print(count)  