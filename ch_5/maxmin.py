biggest = None
smallest = None

while True:
    value = input('enter a number\n')
    if value == "done":
        break
    #else:
    try:
        value = float(value)
        if biggest is None or value > biggest:
            biggest = value
        if smallest is None or value < smallest:
            smallest = value
    except:
        print('bad input')

print(biggest, smallest)
