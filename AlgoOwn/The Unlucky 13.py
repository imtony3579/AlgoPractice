"""
Write a program to calculate the total number of strings that are made of exactly N characters.None of the strings can have "13" as a substring.
The strings may contain any integer from 0-9, repeated any number of times
"""

# solution 1
# Time limit exceeding and answer is wrong for greater than 3 digits
for _ in range(int(input())):
    n = int(input())
    if(n == 0):
        print(0)
    print(int(10**n - ((n-1)*(10**(n-2)))))

# Solution 2
# Time limit exceeds 
for _ in range(int(input())):
    n = int(input())
    z = 10**(n%1000000009)
    count = z
    for i in range(z):
        if(str(i).__contains__('13')):
            count-=1
    print(count)

# solution 3
