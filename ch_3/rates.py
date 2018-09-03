hours = input('enter hours worked\n')
rate = input('enter rate of pay\n')
bonushours = float(hours)%40
pay = (float(hours) - bonushours) * float(rate)
bonuspay = bonushours*1.5*float(rate)
finalpay = pay + bonuspay

if float(hours) <= 40:
    print(pay)
else:
    print(finalpay)
