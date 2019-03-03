def fibo(n):
    # Exception Handling
    if n < 1:
        print("n must be larger or equal to 1")
        return

    if n == 1:
        res = [0, ]
    elif n == 2:
        res = [0, 1]
    else:
        for i in range(n - 2):

            # Declare a variable and assign a value for next element
            # Then append it to list res

            ##############################
            ##############################
            ########Your Code Here########
            ##############################
            ##############################
            pass
    
    return res

def main():
    n = int(input("Enter a postive integer:"))
    res = fibo(n)

    for i, number in enumerate(res):
        print(i+1, number)


if __name__ == "__main__":
    main()