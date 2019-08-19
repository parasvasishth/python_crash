# todo greet_user()
#
# def greet_user():
#     print('Hello!')
#
# greet_user()
#
# todo greet user by name
# def greet_user_name(username):
#     print("Hello! "+username.upper())
#
#
# greet_user_name('paras')
#
# todo T-shirt  function
#
# def make_shirt(size,text_message):
#     print("The size of the T-shirt " + size + " here is the message on the t-shirt " + text_message)
#
#
#
# make_shirt("L","Backchod billi hu mai")
# make_shirt(size="M",text_message="hello world!")
#
#
#
# todo T-shirt with default value
#
# def make_shirt(size="Large",message="i love python "):
#     print("Your size is " + size+ " your message is " + message)
#
#
# make_shirt()
# make_shirt(size="medium")
# make_shirt(size="medium",message="I love Java")
#
#
# todo cities
#
#
# def describe_city(name,country="India"):
#     print(name.title()+" is in " + country)
#
#
#
# describe_city(name="delhi")
# describe_city(name="ludhian")
# describe_city(name="lahor",country="pakistan")
#
#
#
# todo return values
#
#
# def get_full_name(first_name,last_name):
#     full_name = first_name + " " + last_name
#     return full_name
#
# print( get_full_name("anmol","sharma"))
# print(mv)
#
#
# todo using funcation with while loop
#
# def get_name(first_name,last_name):
#     full_name = first_name + " " + last_name
#     return full_name.title()
#
# while True:
#     print("\n Please enter your name")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First Name: ")
#     if f_name =='q':
#         break
#     l_name = input("Last Name: ")
#     if l_name == 'q':
#         break
#     form_name = get_name(f_name,l_name)
#     print("\n Hello," +form_name)
#
#
# todo Passing a List
# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
# usernames = ['paras', 'anmol','jatin','ty']
# greet_users(usernames)
#
#
# todo Modifying a List in a Function
# def print_models(unp_de,comp_models):
#     while unp_de:
#         current_design = unp_de.pop()
#         print("Printing Stuff: " + current_design)
#         comp_models.append(current_design)
# def show_completed_models(comp_models):
#     print("\nThe following models have been printed:")
#     for com in comp_models:
#         print(com)
#
#
# unp_de = ['iphone','robot','doc']
# comp_models = []
# print_models(unp_de[:],comp_models)
# show_completed_models(comp_models)
# print(unp_de)
#
#
# todo show magicians
#
# def show_mess(list_mess):
#     for list in list_mess:
#         print("Hello "+list.title()+" !")
#
#
# def make_great(magicians):
#     great_magicians=[]
#
#     while magicians:
#         magician = magicians.pop()
#         great_magician = magician + ' The great'
#         great_magicians.append(great_magician)
#
#
#     for great_magician in great_magicians:
#         magicians.append(great_magician)
#
#
# magicians = ['paras','anmol','jatin']
#
# show_mess(magicians)
# print("\n")
# make_great(magicians)
# show_mess(magicians)
#


# todo unchanged magicians
#
# def show_magicians(magicians):
#
#     for magician in magicians:
#         print(magician)
#
#
# def make_great(magicians):
#     great_magicins = []
#     while magicians:
#         magician = magicians.pop()
#         great_magicin = magician + "The great"
#         great_magicins.append(great_magicin)
#
#     for great_magicin in great_magicins:
#         magicians.append(great_magicin)


# todo Arbitrary Number of Arguments
#
# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza('tomato','patato','mushrooms')


# todo Using Arbitrary Keyword Arguments

# def build_profile(first,last,**user_info):
#     profile = {}
#
#     profile['first_name']= first
#     profile['last_name']= last
#     for key , value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('paras','sharma',location='ludhiana',field='information ')
#
# print(user_profile)