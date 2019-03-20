def my_a():
    global a
    print(a)
    return 1

def my_function(a, b):
    return 1

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print(is_leap_year(2018))

current_year = 2019
year_list = []
for year in range(current_year, current_year + 300):
    year_list.append(is_leap_year(year))

for year, true_or_false in enumerate(year_list):
    if true_or_false == True:
        print(current_year + year, true_or_false)
        break

def divide(number):
    return (number/2, number/2)

t = divide(5)
a, b = t
print(a, b)
print(t)