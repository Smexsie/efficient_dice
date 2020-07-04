from random import randint

def d4():
    times = int(input('How many times?  '))
    index = []
    while times > 0:
        index.append(randint(1,4))
        times -= 1
        if times == 0:
            index.sort(reverse=True)
            print(index)
            print(sum(index))
            print('\n')
def d6():
    times = int(input('How many times?  '))
    index = []
    while times > 0:
        index.append(randint(1,6))
        times -= 1
        if times == 0:
            index.sort(reverse=True)
            print(index)
            print(sum(index))
            print('\n')
def d8():
    times = int(input('How many times?  '))
    index = []
    while times > 0:
        index.append(randint(1,8))
        times -= 1
        if times == 0:
            index.sort(reverse=True)
            print(index)
            print(sum(index))
            print('\n')
def d10():
    times = int(input('How many times?  '))
    index = []
    while times > 0:
        index.append(randint(1,10))
        times -= 1
        if times == 0:
            index.sort(reverse=True)
            print(index)
            print(sum(index))
            print('\n')
def d12():
    times = int(input('How many times?  '))
    index = []
    while times > 0:
        index.append(randint(1,12))
        times -= 1
        if times == 0:
            index.sort(reverse=True)
            print(index)
            print(sum(index))
            print('\n')
def d20():
    times = int(input('How many times?  '))
    index = []
    while times > 0:
        index.append(randint(1,20))
        times -= 1
        if times == 0:
            index.sort(reverse=True)
            print(index)
            print(sum(index))
            print('\n')   
def d100():
    times = int(input('How many times?  '))
    index = []
    while times > 0:
        index.append(randint(1,100)) #this prints the numbers on the horizon
        times -= 1
        if times == 0:
            index.sort(reverse=True)
            print(index)
            print(sum(index))
            print('\n')
def roll():  #this is asked first. will bring you to the appropriate die
    while True:
        die = str(input('What sided die will you roll?  '))
        if die == '4':
            d4()
        elif die == '6':
            d6()
        elif die == '8':
            d8()
        elif die == '10':
            d10()
        elif die == '12':
            d12()
        elif die == '20':
            d20()
        elif die == '100':
            d100()
        elif die != '4' or '6' or '8' or '10' or '12' or '20' or '100':
            print('NO')
        else:
            print('NO')

roll()
              
