EntNum = int(input("Enter a Number: "))

n = 0

for n in range(
        EntNum,
        EntNum + 10,
):
    if (EntNum % 2 == 1):
        EntNum = EntNum + 2
        print(EntNum)
        n = n + 1

    elif (EntNum % 2 == 0):
        EntNum = EntNum - 1
        EntNum = EntNum + 2
        print(EntNum)
        n = n + 1