count = 0
total = 0
print('before', count, total)
while True:
    value = input('enter a number\n')
    if value == "done":
            break
    else:
        try:
            value = float(value)
            count = count + 1
            total = total + float(value)
        except:
            print('bad input')

if count == 0: #in case user never puts a number in
    print('bad input, cant compute')
else:
    print('count:', count, 'total:', total, 'mean:', total/count)
