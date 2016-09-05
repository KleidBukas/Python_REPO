import random

Squat = ['low bar', 'high bar', 'front squat', 'SSB', "hip squat"]
Bench = ['bench', 'slingshot', 'legs up']

select = random.randint(0,4)
SQ = Squat[select]


while True:
    try:
        data = input("Choose a lift: ")
    except ValueError:
        print('Wrong input.')
        continue
    else:
        break

if data == 'Squat':
    print(Squat[select])

elif data == 'Bench':
    print(Bench[select])

    #



