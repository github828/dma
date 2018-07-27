def main():
    print("Hello everyone")

    i = 2
    if i<3 and i%2==0:
        print("i is less than 3 and the remainder of i divided by 2 is 0")

    i=5
    print(type(i))
    i=str(i)
    print(type(i))


    n = 4
    if n==2+2:
        print("n equals to 2 plus 2")

    x = 20
    if x<20 and x>5:
        print("x is less than 20 and greater than 5")
    else:
        print("x is not less than 20 and greater than 5")


    z=11
    if z<20 or z>0:
        if z==12:
            print("z equals to 12")
        else:
            print("z is not equal to 12 but it is either greater than 0 or/and less than 20")

    z=13
    print(type(z))
    z=str(z)
    print(type(z))


    print("the value of z now is "+z)


    array=["hi","bye","hello"]
    print(array)
    print(array[2])
    for i in range(4):
        print(i)


    array=["0","1","2","3"]
    print(array)
    print(array[3])
    print(array[2])
    print(array[1])
    print(array[0])



    print("Bye")



main()

