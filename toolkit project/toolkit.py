import sys as s
import func
import crusher as c
import os

y = 0
x = str(s.argv[1])
print('Adam ofer - python [Version 1.5.2004]                                           '
      'Copyright (c) 2019.  All rights reserved.')
print('')

if x == '-h':
    print('usage: [encrypt/powme/multicalc/crusher/fib/palindrome/power/squereme/trinum] -r       ')
    x = input()
    if x == 'encrypt -r':
        func.encrypter()
        exit(0)
    if x == 'powme -r':
        y = int(input('choose a number to power by himself:  '))
        func.powme(y)
        exit(0)
    if x == 'multicalc -r':
        func.multicalc()
        exit(0)
    if x == 'crusher -r':
        c.crusher()
        exit(0)
    if x == 'fib -r':
        func.fib()
        exit(0)
    if x == 'palindrome -r':
        y = int(input('enter a board:  '))
        func.palindrome(y)
        exit(0)
    if x == 'power -r':
        func.power()
        exit(0)
    if x == 'squereme -r':
        func.squereme()
        exit(0)
    if x == 'trinum -r':
        y=int(input('how many triangular number you want:'))
        print(func.trinum(y))
        exit(0)

if x == '-i':
    print('')
    print('-toolkit born in the name pyhelp and it began writing on 28.1.2019 by Adam Ofer.'
          'The purpose of the script is to use other function that can'
          ' solve               problems, encryption and complex math calculations.')
    print('')
    print('-The script was written in Pycharm and it combines two other scripts written by Adam Ofer and combines additional modules')
    print('')
    print('Run instructions:')
    print('    r: run the program functions (run).')
    print('    i: show this text (information)')
    print('    h: show the functions and how to run them (help).')
    print('    ?: show the functions and how to run them (help).')
    print('    p: print a text (print).')
    print('    s: open shutdown dialog.')
    print('    c: show code source (code source)')
    print('')
    print('functions:')
    print('    encrypt: slove and encrypt sentenses and words')
    print('')
    print('    powme: power a number by himself. y=x**x')
    print('')
    print('    multicalc: a calculator containing all the operations of the account is         rooting for the numbers entered'
          '  and showing the abbreviated multiplication     formulas.')
    print('')
    print('    crusher: force the user to shutdown/restart the computer.')
    print('')
    print('    fib: print all Fibonacci numbers up to z.')
    print('')
    print('    palindrome: print all the palindrome numbers up to x.')
    print('')
    print('    power: power number with another one.')
    print('')
    print('    squereme: print and sum all to squere numbers up to x + the digit lenght.')
    print('')
    print('    trinum: return list of all the triangle numbers up to x.')
    print('')

    exit(0)
if x == '-?':
    print('usage: [encrypt/powme/multicalc/crusher/fib/palindrome/power/squereme] -r       ')
    x=int(input())
    if x == 'encrypt -r':
        func.encrypter()
        exit(0)
    if x == 'powme -r':
        y = int(input('choose a number to power by himself:  '))
        func.powme(y)
        exit(0)
    if x == 'multicalc -r':
        func.multicalc()
        exit(0)
    if x == 'crusher -r':
        c.crusher()
        exit(0)
    if x == 'fib -r':
        func.fib()
        exit(0)
    if x == 'palindrome -r':
        y = int(input('enter a board:  '))
        func.palindrome(y)
        exit(0)
    if x == 'power -r':
        func.power()
        exit(0)
    if x == 'squereme -r':
        func.squereme()
        exit(0)

if x=='-p':
    print('usage: <text> -r')
    x=input()
    if x[-2]+x[-1]=='-r':
        print('"'+x[0:-3]+'"')
        exit(0)
    else:
        print('forgot: "-r"')
        exit(0)
if x=='-s':
    y=os.system('shutdown.bat')
    exit(0)
if x=='-ip':
    y=os.system('ipfind.bat')
    print('')
    print('search for " IPv4 Address" to find your ip')
    exit(0)
if x=='-c':
    y=os.system('source.bat')
    exit(0)
else:
        print('try: toolkit.py [-i/-h/-p/-s/-ip/-c/-?]  ')