Name:SIBO CYUBAHIRO Evrard Kenny
Registration Number:221024471
Department:Computer Science
  
  
import random 
num = int(input("Enter the number of friends joining (including you):\n"))
guest = {}

if num > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num):
        name = input()
        guest.update({name: 0})
    
    print("Enter the total bill value:")
    bill = int(input())
    for_each = bill / num
    for key,value  in guest.items():
        guest[key] = round(for_each, 2)

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: \n")
    choice = input()
    if choice == "Yes":
        lucky_one = random.choice(list(guest))
        print(lucky_one, " is the lucky one!")

        for_remaining = bill / (num - 1)

        for key,value  in guest.items():
            if key == lucky_one:
                guest[lucky_one] = 0
            else:
                guest[key] = round(for_remaining, 2)
        print(guest)
    else:
        print("No one is going to be lucky")
        print(guest)
else:
    print("No one is joining for the party")
