## Check the number and tell whether it is prime or not.

n = 10

for num in range (2, n):
    if ((n % num) == 0):
        print (f"{n} is not prime!")
        break
else:
    print (f"{n} is prime!")
