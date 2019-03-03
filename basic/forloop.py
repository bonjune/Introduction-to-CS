'''
For-loops are range-based, which means it is suitable to solve problems where a range exists.
'''

print("Say hello to for-loops...")
for i in range(3):
    print("Hello for-loops!")
print("-" * 20)

print("What does range(3) contain?")
for i in range(3):
    print(i)
print("-" * 20)

my_list = ["How", "It", "Works", "?"]
print("What does my_list contain?")
for i, item in enumerate(my_list):
    print(i, item, len(item))
print("-" * 20)


# Tips
# You can also make a list with range(n)

l = list(range(10))
print(l)
print("-" * 20)

# Example 1.
s = "Apple"
for c in s:
    if c == "e":
        print(s + " contains 'e'")

print("-" * 20)

# Example 2.
list_of_tuples = [(1,1), (2,4), (3,9)]
for (first, second) in list_of_tuples:
    print(first)
    print(second)

print("-" * 20)

# Example 3.
print("How to compute average?")
target = list(range(1, 101))
total = 0
for number in target:
    total += number
print(total / len(target))