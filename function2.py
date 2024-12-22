def greet_user(name):   
    print(f'Hi {name}!')
    print('Welcome aboard')
    
    
print("Start")
greet_user("John")
greet_user("Mary")
print("Finish")
print("")


def greet_friends(identity):   
    print(f'Hello {identity}!')
    print('Welcome home')
    
    
print("Begin")
greet_friends("Tope")
greet_friends("Dupe")
print("Completed")
print("")

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "Smith")
greet_user("Mary", "Fisher")
print("Finish")
print("")

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("Smith", "John")
greet_user(last_name="Smith", first_name="John")
print("Finish")
print("")