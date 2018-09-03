hours = input('enter hours worked\n')

try:
    hours = int(hours)
except:
    print('use a number you idiot, Im a calculator')
    quit()

rate = input('enter rate of pay\n')
try:
    rate = int(rate)
except:
    print('you fool, you gotta use numbers')
    quit()

basicpay = float(hours) * float(rate)
bonushours = float(hours) - 40
bonuspay = bonushours*1.5*float(rate)
finalpay = 40*float(rate) + bonuspay

if float(hours) <= 40:
    print(basicpay)
else:
    print(finalpay)
