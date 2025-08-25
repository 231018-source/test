#task1
# name = input("Enter name: ")
# age = input("Enter age: ")
# boot_camp_name = input("Enter boot camp name: ")
# with open("file.txt", "w") as f:
#     f.write(name + "\n")
#     f.write(age + "\n")
#     f.write(boot_camp_name + "\n")
#     print("done saved notes")
#     with open("file.txt","r") as f:
#      reads = f.read()
#      print(reads)
  
  
  
  
  
  
  
  
# # task2     
# username = input(" enter a username :")
# password = input(" enter a password :")

# username_fixed = username.lower()
# username_fixed = username_fixed.replace(" ", "_")
# password_length = len(password)
# print("\n--- Print all results---")
# print(f" Username after modification :{username_fixed}")
# print("\n--- -Use Boolean expressions to check:--")
# print(" password length is greater than or equal to 8 : ", password_length >= 8)
# print("username is admin : ", username_fixed == "admin")
# print(" password is 1234 :", password == "1234")
# print("default account :", username_fixed == "admin" and password == "1234")

# print(f"\n heloo {username_fixed}، password length{password_length} ")

     
     
     

     
#task3     
# #1
# fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry"]
# print( fruits)
# #2
# print( fruits[0])
# print( fruits[-1])
# #3
# fruits[1] = "Mango"
# print( fruits)
# #4
# fruits.insert(2, "Watermelon")
# print( fruits)
# #5
# fruit = input("enter name fruits")
# print(fruits.count(fruit) != 0)
# #6
# fruits.sort()
# print(fruits)
 



#task4
fruit_prices = {
    "apple": 2.5,
    "banana": 1.2,
    "orange": 1.8,
    "mango": 3.0,
    "grape": 2.0
}
fruit_name = input("Enter the name of a fruit: ").lower()
if fruit_name in fruit_prices:
    print(f"The price of {fruit_name} is ${fruit_prices[fruit_name]}")
else:
    print("Sorry, this fruit is not available.")














