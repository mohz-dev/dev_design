# Pseudocode
# input for number of student
# for loop working with input
# Enter student name
# Enter student score
# append student name and score to a list
# check if score is valid between 0 and 100
# if score is invalid, while loop to ensure a valid score is entered
# calculate average score
# store average score
# if score greater than or equal to 60 student passed
# store students that passed in a list
# if score less than 60 student failed
# store students that failed in a list
# print class average
# print the highest score
# print the lowest score
# print list of students that passed
# Print list of students that failed

no_of_students = int(input("Enter no of students: "))
students = []
passed_students = []
failed_students = []
scores = []

for student in range(no_of_students):
    student_name = input("Enter Student name: ")
    student_score = int(input("Enter Student score: "))
    while student_score not in range(0, 101):
        student_score = int(input("Enter Student score: "))

    scores.append(student_score)
    student_info = [student_name, student_score]

    if student_score < 60:
        failed_students.append(student_info)
    else:
        passed_students.append(student_info)

    students.append(student_info)


total_scores = sum(scores)
average_score = total_scores/len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print("")
print(f"These students failed {failed_students}")
print("")
print(f"These students passed {passed_students}")
print("")
print(f"The average score is {average_score}")
print("")
print(f"The highest score is {highest_score}")
print("")
print(f"The lowest score is {lowest_score}")
