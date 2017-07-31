
for x in range(2, 100):
    if x > 1:

        for i in range(2, x):
            if (x % i) == 0:
                print(x, "is not a prime number")

                break
        else:
            print(x, "is a prime number")

