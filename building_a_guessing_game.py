secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess:'))
    guess_count +=1
    if guess == secret_number:
        print('You won!')
        break
else:
        print("Sorry it's incorrect")
    
    
    
    
answer = '''
start - to start the car
stop - to stop the car
quit - to exit 
'''
    
    
    
if guess == ">help":
    print(answer)
elif guess == ">start":
    print ("Car started...Ready to go!")
elif guess == ">stop":
    print("Car Stopped.")
elif guess == ">quit":
    print()
else:
    print ("I don't understand that...")
    
    
    
    
guess = (">" + input(''))
print(guess)