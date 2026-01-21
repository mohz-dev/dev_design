# password checker
password = input("Enter your password: ")
min_length = len(password) >= 8
has_lowercase = password.upper() != password
has_uppercase = password.lower() != password

if min_length and has_lowercase and has_uppercase:
    message = "Welcome to dev and design"
else:
    message = "Wrong format"

print(message)

score = input("Enter your score: ")

if score.isnumeric():  # isnumeric is a function that is used to check if a number was entered
    score = int(score)
    print(score)
    if score >= 85 and score <= 100:
        print("A")
