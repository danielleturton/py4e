biggest = None
smallest = None
while True:
    try:
        num = input('enter a number\n')
        if value == "done":
            break
        value = int(num)
        if biggest < value :
            biggest = value
        if smallest == None or smallest > n :smallest = n

    except:
            print('bad input')

print(biggest, smallest)
