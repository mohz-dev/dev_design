# loops allow us to repeat code multiples times without having to write the code over again
# While loops runs until a set condition is false

# while loop
# while condition:
# .   run code
'''
count = 1

while count <= 3:
    print(count)
    count += 1

print("End of loop")


# write a program to guess a secret number, the user should be allowed to 3 attempts at guessing the number,
# if the user enters a wrong number after the 3rd attempt, user should get a message "you lost", and the program should terminate
# if the user enters the correct number, user should get the message "Correct", and the program should terminate

secret_number = 6
guess_attempt = 0
guess_count = 3

while guess_attempt < guess_count:
    guess = int(input("Enter number: "))
    guess_attempt += 1
    if guess == secret_number:
        print("Correct")
        break
else:
    print("you lost")


'''
print("############# For Loops ############")
# For loops is used when you want to go through an item a number of times
# but with a condition that would either determine if you need to stop or keep going

# for item in iterable:
# .   run code

name = input("Enter name: ")
times = input("no of times: ")

if times.isnumeric():
    for no in range(int(times)):
        print(f"Merry Xmas {name}")
else:
    print("please enter a valid number")
