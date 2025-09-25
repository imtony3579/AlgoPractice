"""

Minimum AND xor OR

Given an array A of N integers. Find out the minimum value of the following expression for all valid i, j.

(Ai and Aj) xor (Ai or Aj), where i != j.

"""

# first Solution 
# partially accepted (exceeding time limit)

def operation(x, y):
    return (x&y)^(x|y)

for _ in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    oldValue = operation(A[0], A[-1])
    for i in range(n-1):
        for j in range(i+1, n):
            newValue = operation(A[i], A[j])
            if(newValue < oldValue):
                oldValue = newValue
    
    print(oldValue)

# Second Solution 
# found on web and understood 
for _ in range(int(input())):
    n = int(input())
    A = sorted( [int(x) for x in input().split()])
    oldValue = float('inf')
    for i in range(len(A)-1):
        oldValue = min(oldValue, A[i]^A[i+1])
    
    print(oldValue)