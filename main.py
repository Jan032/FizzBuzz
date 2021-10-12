
import time

print("Welcome to FizzBuzz")

end = int(input("Select a number between 1 and 100: "))


for x in range(1, end+1):

    if end > 100:
        print("your number is too high dear sir.")
        break

    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        time.sleep(0.3)

    elif x % 3 == 0 and x % 5 != 0:
        print("Fizz")
        time.sleep(0.3)

    elif x % 3 != 0 and x % 5 == 0:
        print("Buzz")
        time.sleep(0.3)

    else:
        print(x)
        time.sleep(0.3)