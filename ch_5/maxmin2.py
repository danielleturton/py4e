biggest = None
smallest = None

while True:
    try:
        value = input('enter a number: ')
        if value =='done':
            break
        print(value)
        value = float(value)
        if biggest is None or value > biggest:
            biggest = value
        elif smallest is None or value < smallest:
            smallest = value
    except:
        print('bad input')
        continue

print(smallest, biggest)
