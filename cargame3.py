command = ""
started = False
stopped = False
while command !="quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if stopped:
            print("Car is already stopped")
        else:
            stopped = True
            print("Car stopped...")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit      
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry. I don't understand that.")
        