score = input('what score did you get, sonny?\n')

try:
    score = float(score)
    if score < 1:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score < 0.6:
            print('F')
    else :
        print('you foolclown, only digits between 1 and 0 are valid here')
except:
    print('enter a number dumbass')
