numberr = float(input("Enter a number: "))
if numberr < 0:
    print("square root of a negative number cannot be found.")
else:
    if numberr == 0:
        result = 0
    else:
        no = numberr / 2
        while True:
            nextno = (no + numberr / no) / 2
            if abs(nextno - no) < 10**-9:
                result = nextno
                break
            no = nextno
    print("The square root is =", result)
