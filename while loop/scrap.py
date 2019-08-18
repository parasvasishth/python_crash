 # TODO while loop with acrive flag

# pro = "\nTell me something, and i will repeat it back to you:"
# pro += "\nEnter 'quit' to end the program."
# active = True
#
# while active:
#     message = input(pro)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)



#  ToDO using break to exit a loop

# prompt = "\n Please enter the name of the city you have visted"
# prompt += "\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("i`d love to go to " + city.lower() + "!")
#
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I`d love to go to" + city)


# Todo using continue in a loop

# current_numver =  0
# while current_numver < 10:
#     current_numver += 1
#     if current_numver % 2 ==0:
#         continue
#
#     print(current_numver)
#
#


# todo Avoiding infinite loops
# x = 1
# while x <=5:
#     print(x)
#     x +=1


# Todo pizza toppings

# pro = "\n Please let us know what toppings you want:"
# req = "Please add more if you want or write 'quit' to quit "
# topping_list = []
# while True:
#     topping_l = input(pro)
#     if topping_l == 'quit':
#         break
#
#     else:
#         print("\nYou are just add " + topping_l.upper() + "! " + req )

# todo pizza toppings with Three exits 7-6
#
# pro = "\n Please let us Know what toppings you want:"
# req = "Please add more if you want or write 'quit' to quit "
# active = True
# while active:
#     tl1 = input(pro)
#     if tl1 == 'quit':
#         active = False
#     else:
#          print("\nYou are just add " + tl1.upper() + "! " + req )


 # todo Movie tickets


# promt = "Pleae enter Your age:"
# age = int(input(promt))
# while True:
#     if age <= 3:

#         print("The Ticket is free")
#         break
#     elif age >= 3 and age <= 12:
#         print("The Value of the ticket is $10")
#         break
#     else:
#         print("The Value of the ticket is $15")
#         break

# Todo infinity loop

# a = "Hello world"
# while True:
#     print(a)

# TODO confirmed_users one list to another

# uncon_user = ['paras','anmol','jatin']
# con_user = []
#
# while uncon_user:
#     current_user = uncon_user.pop()
#     print("Verifying user: " + current_user.title())
#     con_user.append(current_user)
#
# print("\n The following users have been confirmed:")
# for i in con_user:
#     print(i.title())

#todo Removing All Instances of Specific Values from a List

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
#
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

# Todo filling a disctionary with user input

# resp = {}
#
# poll = True
#
# while poll:
#     name = input("\n what is your name? ")
#     respo = input("Which mountain would you like to climb someday? ")
#
#     resp[name] = respo
#
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         poll =False
#
#
# print("\n -----------Poll Results------------")
# for name, resp in resp.items():
#     print(name + " would like to climb " + resp + ".")


# todo sandwich order

# sandwich_order = ['tuna sandwich', 'veg sandwich','non-veg sandwhich']
# sandwich_finished = []
#
# while sandwich_order:
#     making = sandwich_order.pop()
#     print(" I making your " + making)
#     sandwich_finished.append(making)
#
# for i in sandwich_finished:
#     print("\nThanks for ordering" "\nYour " +i+" has been made ")


# todo No Pastrami
# sandwich_order = ['tuna sandwich','pastrami','pastrami','pastrami', 'veg sandwich','non-veg sandwhich']
# sandwich_flag = True
# print(sandwich_order)
# print("\n deli is out of pastrami")
#
# while sandwich_flag:
#     remove = sandwich_order.remove('pastrami')
#     if 'pastrami' not in sandwich_order:
#         sandwich_flag = False
#
# print(sandwich_order)


