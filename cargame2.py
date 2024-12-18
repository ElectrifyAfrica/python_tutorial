answer = '''
start - to start the car
stop - to stop the car
quit - to exit 
'''

guess = input("> ")

if guess == "help":
    print(answer)
elif guess == "start":
    print ("Car started...Ready to go!")
elif guess == "stop":
    print("Car Stopped.")
elif guess == "quit":
    print()
else:
    print ("I don't understand that...")