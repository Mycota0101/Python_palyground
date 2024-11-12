import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock,paper,scissors]
x = random.randint(0,2)
y = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if x == y:
    print(rps[y]+"\ncomputer chose\n"+rps[x]+"\nit's draw !!!")
elif x == 0:
    if y == 1:
        print(rps[y]+"\ncomputer chose\n"+rps[x]+"\nYou Win!!")
    elif y == 2:
        print(rps[y] + "\ncomputer chose\n" + rps[x]+"\nYou Lose!!")
elif x == 1:
    if y == 0:
        print(rps[y] + "\ncomputer chose\n" + rps[x]+"\nYou Lose!!")
    elif y == 2:
        print(rps[y] + "\ncomputer chose\n" + rps[x]+"\nYou Win!!")
elif x == 2:
    if y == 0:
        print(rps[y] + "\ncomputer chose\n" + rps[x]+"\nYou Win!!")
    elif y == 1:
        print(rps[y] + "\ncomputer chose\n" + rps[x]+"\nYou Lose!!")
else:
    print("input not valid")
