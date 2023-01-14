"""
Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.
"""

# 1st way to solve by fails in time 
test_case = input()
for i in range(int(test_case)):
    element, rotation = input().split()
    arr = [int(x) for x in input().split()]
    for j in range(int(rotation)):
        arr.insert(0,arr.pop())

    print(' '.join(str(x) for x in arr))

# 2nd solution minor upgrade
test_case = input()
for i in range(int(test_case)):
    elementRotation = [int(a) for a in input().split()]
    arr = [int(x) for x in input().split()]
    elementRotation[1]%=elementRotation[0] # upgraded part
    for j in range(int(elementRotation[1])):
        arr.insert(0,arr.pop())

    print(' '.join(str(x) for x in arr))

# 3rd Solution from internet and working
testCase  = int(input())
for _ in range(testCase):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    x = k%n
    print(*(l[n-x:]+l[:n-x]))
