import math as m
import sys as s
import decimal as d


# my moduls #


def power():  ###############################   1. power number with another one.
    y = int(input('enter a number for power '))
    z = int(input('enter a number for power with it '))
    a = y ** z
    print(a)
    return a
    power(y, z)


def powme(x):  #########################   2. power a number by himself. y=x**x
    print(x, '**', x, '=', x ** x)
    return x


def squereme():  ###########################  3. print and sum all to squere numbers up to x
    # +  print the digit lenght.

    x = 0
    r = 0
    z = ''
    y = int(input('enter a border  '))
    for i in range(1, y + 1):
        y = i ** i
        r += 1
        print(r, '.', y)
        x += y
    print('sum:', x)
    z = len(str(x))
    print('digit lenght:', z)


def palindrome(x):  ############################## 4. print all the palindrome numbers up to 'x'.
    y = ''
    r = 0
    for n in range(10, x + 1):
        y = str(n)
        if y == y[:: -1]:
            r += 1
            print(r, '. ', n)


# palindrome(10000)


def encrypter():  ##################### 5. slove and encrypt sentenses and words
    s = ""
    o = ""
    z = input('write sentese for encrypt ') + '   '
    y = 0
    # y=int(input('Select a number to move the letters and encrypt it '))
    for y in range(26):
        for x in z:
            if ord(x) >= ord('a') and ord(x) <= ord('z'):
                o += chr((ord(x) + y - ord('a')) % 26 + ord('a'))
            else:
                o += x
    print(o)
    print('   ')


def trinum(x):  ########################## 6. return list of all the triangle numbers up to x
    y = 0
    z = []
    for n in range(1, x + 1):
            y += n
            z.append(y)
            # print('..')
            # print(z)
    return z


#def powsum():  ###########################  6.5 . print and sum all the numbers in power of 2 up to x
    # +  print the digit lenght.

#    x = 0
#    r = 0
 #   z = ''
 #   y = int(input('enter a border  '))
   # for i in range(1, y + 1):
 #       y = i ** 2
 #       r += 1
 #       print(r, '.', y)
 #       x += y
  #  print('sum:', x)
 #   z = len(str(x))
#   print('digit lenght:', z)

 #   return x


def multicalc():  ######################### 7. A calculator containing all the operations of the account is rooting for the numbers entered
    #######################################   and showing the abbreviated multiplication formulas.
    x = int(input('enter a number as x '))
    y = int(input('enter another number as y '))
    print('x =', x)
    print('y =', y)
    if y < 0 and x < 0:
        pass
    elif y < 0 or x < 0:
        if y < 0:
            print('root x=', m.sqrt(x))
        if x < 0:
            print('root y=', m.sqrt(y))
    else:
        print('root x=', m.sqrt(x))
        print('root y=', m.sqrt(y))

    print(' ')
    print(x, '+', y, '=', x + y)
    print(x, '-', y, '=', x - y)
    print(x, 'x', y, '=', x * y)
    print(x, ':', y, '=', x / y)
    print('(x+y)(x-y):'), print('x*x-y*y =', x, '*', x, '-', y, '*', y, '=', x * x - y * y)
    print(' ')
    print('(x+y)**2:'), print('x*x+2xy+y*y =', x, '*', x, '+', 2, '*', x, '*', y, '+', y, '*', y, '=', (x + y) ** 2)
    print(' ')
    print('(x-y)**2:'), print('x*x-2xy+y*y =', x, '*', x, '-', 2, '*', x, '*', y, '+', y, '*', y, '=', (x - y) ** 2)


def fib():  ##################8. print all Fibonacci numbers up to z.
    x, y, r = 0, 1, 0
    z = int(input('enter a number:  '))
    z = z - 1
    while r <= z:
        x, y = y, y + x
        r = r + 1
        print(r, '.', x)
        print('')
    print('')
    print(x)
