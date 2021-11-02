#Fizz Buzz----------------------------------------------------------------

def FizzBuzz():
    for i in range(1,101):

        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz ", end='')

        elif  i % 3 == 0:
            print("Fizz ", end='')

        elif i % 5 == 0:
            print("Buzz ", end='')

        else:
            print(i, " ", end='')

#--------------------------------------------------------------------------

#Leap Year-----------------------------------------------------------------

def Leap_Year():
    x = int(input("Year: "))
    while True:
        if x % 400 == 0:
            print("True")
        elif ((x % 400)% 100) != 0 and x % 4 == 0:
            print("True") 
        else:
            print("False")
        print("-------------------------------------------------------------------------------------")    
        i = input("Continue = Y or y Exit = N or n: ")
        if i == 'N' or i == 'n':
            break
        elif i == 'Y' or i == 'y':
            x = int(input("Year: "))
        else:
            i = input("Continue = Y or y Exit = N or n: ")

#-----------------------------------------------------------------------------

#print------------------------------------------------------------------------

def level_1():
    n = int(input("number: "))

    for i in range(0,n):
        for x in range(i):
            print("*", end='')
        print("*")

def level_2():
    n = int(input("number: "))

    for i in range(1,n+1):
        for x in range(n, 0, -1):
            if x > i:
                print(" ", end=' ')
            else:
                print("*", end=' ')
        print('')

def level_3():
    n = int(input("number: "))
    i = 1
    while i <= n:
        j = n
        while j > i:
            print(' ', end=' ')
            j -= 1
        print('*', end=' ')
        k = 1
        while k < 2 * (i - 1):
            print(' ', end=' ')
            k += 1
        if i == 1:
            print()
        else:
            print('*')
        i += 1

def level_5():
    n = int(input("number: "))
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
        
    k = n - 2

    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
#---------------------------------------------------------------------------------------------
n = int(input('Enter the value of n: '))

for i in range(1,2*n):
    for j in range(1,2*n):
        if i==j or i+j==2*n:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#PrimeNumber----------------------------------------------------------------------------------
def Prime_Number():
    n = int(input("number: "))
    for i in range(n+1):
        if isPrime(i):
            print(i)
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#--------------------------------------------------------------------------------------------

