'''
n = int(input("enter number "))
count = 0
for x in range(1, 20):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")


for x in range(1, 11):
    for y in range(1, 11):
        print(x * y, end=" ")
    print()
'''


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(leap_year(1999))
