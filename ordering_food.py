#Code that provides the user with the process of their meal
def provide_order():
    print("Order up!!")

def cook():
    print("Chopping onions, washing utensils, heating up oil")

def serve():
    print("Here you go!")

#Main procedure
def make_meal():
    provide_order()
    cook()
    serve()

#User is asked to order from a list of options
print("Hello! What would you like to order today?")
print("1. Fried Rice & Roasted Chicken")
print("2. Jollof Rice & Fried Fish")
print("3. Groundnut Soup & Rice Balls")
print("4. Fufu w/ Light Soup & Beef")

operation = input()

if operation == "1":
    print("Enjoy your fried rice and roasted chicken")

elif operation == "2":
    print("Enjoy your jollof rice and fried fish")

elif operation == "3":
    print("Enjoy your groundnut soup and rice balls")

elif operation == "4":
    print("Enjoy your fufu with light soup and beef")

else:
    print("Please order or get out!")

make_meal()





