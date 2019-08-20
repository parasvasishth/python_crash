# todo class with method and instance
# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + " is now sitting..")
#
#     def roll_over(self):
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('jimmy',14)
# your_dog = Dog('lucy', 10)
#
# print("\nMy dog name is " + my_dog.name)
# print("My dog age is "+ str(my_dog.age))
# my_dog.sit()
#
# print("\nYour dog name is "+your_dog.name)
# print("Your dog age is " +str(your_dog.age))
# your_dog.roll_over()

# todo try it 9-1.
# class Restaurant():
#     def __init__(self, restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print("The Restaurant name is "+self.restaurant_name)
#         print("\tHere is the cuisine " + self.cuisine_type)
#
#     def open_restaurant(self):
#         print(self.restaurant_name+" IS OPEN NOW")
#
#
#
#
# restaurant = Restaurant("res_name",'new')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# todo try it 9-2
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def des_rest(self):
#         print("The Restaurant name is " + self.restaurant_name)
#         print("\tHere is the cuisine " + self.cuisine_type)
#
#     def open_rest(self):
#         print(self.restaurant_name+" IS Open Now")
#
#
#
# rest1= Restaurant("restaurant1","cuisine1")
# rest2= Restaurant("restaurant2","cuisine2")
# rest3= Restaurant("restaurant3","cuisine3")
#
# rest1.des_rest()
# rest2.des_rest()
# rest3.des_rest()


# todo try it 9-3
class User():
    def __init__(self,first_name,last_name,location,mobile):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.mobile=mobile
        self.full_name = first_name.title() + " " +last_name.title()

    def describe_user(self):
        print("Hello "+self.full_name+" you are from "+ self.location+" your mobile no. is " + self.mobile)



user = User("paras","sharma","ludhiana","189")
print(user.full_name)
user.describe_user()

# todo working with classes and instances

# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()
#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cant roll back an odometer")
#
# my_car = Car('audi','a4',2018)
# print(my_car.get_descriptive_name())
# my_car.update_odometer(22)
# new = my_car.update_odometer(20)
# print(my_car.odometer_reading)


# todo try it 9-4

# class Restaurant():
#     def __init__(self, restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print("The Restaurant name is "+self.restaurant_name)
#         print("\tHere is the cuisine " + self.cuisine_type)
#         print("Here are the number of customer served by the restaurant " + str(self.number_served))
#     def open_restaurant(self):
#         print(self.restaurant_name+" IS OPEN NOW")
#
#     def update_served_customer(self,customer):
#         if self.number_served >= customer :
#             self.number_served += customer
#             print(self.number_served)
#
#         else:
#             print("You can`t rest the value")
#
#     def increment_served_customer(self,customer):
#         new = self.number_served + customer
#         print("Your daily customers are " + str(new))
#
#
#
# restaurant = Restaurant("res_name",'new')
# # print(restaurant.restaurant_name)
# # print(restaurant.cuisine_type)
# # print(restaurant.number_served)
# # restaurant.update_served_customer(29)
# # print(restaurant.number_served)
# # restaurant.update_served_customer(2)
# # print(restaurant.number_served)
# restaurant.update_served_customer(1)
# restaurant.increment_served_customer(29)
# restaurant.update_served_customer(12)


# todo try it 9-5
# class User():
#     def __init__(self,first_name,last_name,location,mobile):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.location=location
#         self.mobile=mobile
#         self.full_name = first_name.title() + " " +last_name.title()
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("Hello "+self.full_name+" you are from "+ self.location+" your mobile no. is " + self.mobile)
#
#     def increment_login_attempts(self,ad):
#         self.login_attempts += ad
#
#     def reset_login_attempts(self):
#              self.login_attempts = 0
#
# user = User("paras","sharma","ludhiana","189")
# # print(user.full_name)
# # user.describe_user()
# print(user.login_attempts)
# user.increment_login_attempts(2)
# user.increment_login_attempts(2)
# user.increment_login_attempts(2)
# user.increment_login_attempts(2)
# user.increment_login_attempts(2)
# print(user.login_attempts)
# user.reset_login_attempts()
# print(user.login_attempts)

