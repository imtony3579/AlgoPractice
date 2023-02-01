"""

Cyclic shift

A large binary number is represented by a string of size and comprises of and . You must perform a cyclic shift on this string. The cyclic shift operation is defined as follows:


- If the string A is [A0, A1, A2,...,An-1], then after performing one cyclic shift, the string becomes [A1, A2,..., An-1, A0] .


You performed the shift infinite number of times and each time you recorded the value of the binary number represented by the string. The maximum binary number formed after performing (possibly 0) the operation is B. Your task is to determine the number of cyclic shifts that can be performed such that the value represented by the string A will be equal to B for the Kth time.


"""


#Solution

# First try initial try is

# The solution fails for symmetric case

def binToDec(x):

    return int(x, 2)


for i in range(testCase):

    binaryLen, rotation = input().split()
    binary = input()

    count = 0

    hold = 0

    graterNoStep = binToDec(binary)

    for i in range(int(binaryLen)):

        binary = binary[1:]+binary[0]

        count += 1

        temp = binToDec(binary)

        if(temp>graterNoStep):

            graterNoStep = temp
            hold = count


    if(int(rotation)>0):

        hold = hold + (int(binaryLen) * (int(rotation)-1))
    print(hold)


# Second try
# Working for the basic case (but time limit exceeding) 


testCase = int(input())


def binToDec(x):

    dec = 0

    for i in range(len(x)):

        dec += int(x[len(x)-1-i])*(2**i)
    return dec


for i in range(testCase):

    binaryLen, rotation = input().split()
    binary = input()

    count = 0

    hold = 0

    repeat = 1

    steps = 0

    graterNoStep = binToDec(binary)

    for i in range(int(binaryLen)):

        binary = binary[1:]+binary[0]

        count += 1

        steps +=1

        temp = binToDec(binary)

        if(temp == graterNoStep):

            repeat += 1

            hold += steps

        if(temp > graterNoStep):

            graterNoStep = temp
            hold = count

            steps = 0

        if(repeat == int(rotation)):

            break


    if((int(rotation) > 0) and (repeat<int(rotation)) ):

        hold = hold + (int(binaryLen) * (int(rotation)-1))
    print(hold)

# Third try
# solution understood and got from net
for _ in range(int(input())):
    n, k = map(int, input().split())
    binary = input()
    graterBinary = ''
    p = -1
    for i in range(n):
        if (graterBinary < binary):
            graterBinary = binary
            d = i
        elif (graterBinary == binary):
            p = i - d
            break

        binary = binary[1:]+binary[0]
    if (p==-1):
        print(d + (k-1)*n)
    else:
        print(d + (k-1)*p)