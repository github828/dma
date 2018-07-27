def main():
    for i in range(10):
        print(i)
        for j in range(5):
            print("value of i" + str(j))
            print("value of j" + str(i))

def printingi():
    i = 7

    while i < 12:
       i = i+i
       print(i)

for i in range(100):
    printingi()
