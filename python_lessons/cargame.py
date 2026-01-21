# write a program for a car game, when the program starts, if a user enters "help"
# user should get a prompt to enter "start - to start the car, stop - to stop the car, quit - to quit the game"
# if the user enters any other thing, user should get the response "I do not understand"
# if user enters start user should get the response "car started... ready to go!"
# if user enters stop, user should get the response "car stopped."
# if user enters quit, the program should terminate.


game = ">"
started = False
while game:
    instruction = input(">")
    if instruction.lower() == "help":
        print('''
start - to start
stop - to stop
quit - to quit

''')
    elif instruction.lower() == "start":
        if started:
            print("Already started")
        else:
            started = True
            print("Car started.... Ready to go!")
    elif instruction.lower() == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped.")
    elif instruction.lower() == "quit":
        break
    else:
        print("I don't understand that...")
