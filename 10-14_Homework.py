#HomeWork1

d_list = []

while True :
    want = input("Enter a dinner ingredient: ")
    if want == 'quit' :
        break
    
    d_list.append(want)
    d_list.sort()
    
    for i, value in enumerate(d_list) :
        print(i + 1, value)


#HomeWork2

c_list = ['seoul', 'tokyo', 'moskoba', 'toronto', 'queensland', 'bdiging', 'rome']
word = []
lenth = []

for i in c_list :
    if len(i) > 5:
        word.append(i)
        lenth.append(len(i))
print('satisfy word: ', word)
print('satisfy lenth: ', lenth)


#HomeWork3

voted = {'John':True, 'Alice':False, 'Rosa':True}

print(voted)

while True:
    name = input("Enter your name: ")
    if name == '':
        break
    elif voted.get(name) == True :
        print(name, ", You already voted")
    elif voted.get(name) == False :
        print( name, ", Please vote.")
        voted.update(Alice = True)
    else :
        print(name, ", You have no right.")

print(voted)

#HomeWork4

anum = int(input("1. Please enter a number: "))
bnum = int(input("2. Please enter a number: "))

aset = set()
bset = set()

for i in range(1,anum+1) :
    if anum % i == 0 :
        aset.add(i)
    
for i in range(1,bnum+1) :
    if bnum % i == 0 :
        bset.add(i)
    
print(aset)
print(bset)

common_factor = aset & bset

print("Common factor:", common_factor)

#HomeWork5

import random

rps = ['rock', 'paper', 'scissors']
result = {('rock','paper'):False, ('rock', 'scissors'): True, ('paper', 'rock'):True, ('paper', 'scissors'):False, ('scissors', 'rock'):False, ('scissors', 'paper'):True}

while True :
    player = input('rock/paper/scissors :')
    if player == '' :
        break
    print('player -->', player)
    computer = random.choice(rps)
    print('computer -->', computer)

    if (player, computer) in result :
        if result[(player, computer)] == True:
            print('You won! :)')
        else :
            print('You lost! :(')
    else :
        print("It's a tie!")