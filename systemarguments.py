import sys

command=sys.argv[1]
number1=(sys.argv[2])
number1a=int(number1)
number2=(sys.argv[3])
number2a=int(number2)

if command=="add":
    print(number1a+number2a)

if command=="subtract":
    print(number1a-number2a)

if command=="multiply":
    print(number1a*number2a)




