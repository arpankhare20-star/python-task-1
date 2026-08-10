def sum_two_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)


def odd_even():
    n = int(input("Enter number: "))
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


def factorial():
    n = int(input("Enter number: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)


def fibonacci():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def reverse_string():
    s = input("Enter string: ")
    print("Reversed:", s[::-1])


def palindrome():
    s = input("Enter string: ")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


def leap_year():
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")


def armstrong():
    n = int(input("Enter number: "))
    temp = n
    power = len(str(n))
    sum_ = 0

    while temp > 0:
        digit = temp % 10
        sum_ += digit ** power
        temp //= 10

    if sum_ == n:
        print("Armstrong Number")
    else:
        print("Not Armstrong")


# Menu
while True:
    print("\n--- MENU ---")
    print("1. Sum of Two Numbers")
    print("2. Odd or Even")
    print("3. Factorial")
    print("4. Fibonacci")
    print("5. Reverse String")
    print("6. Palindrome Check")
    print("7. Leap Year")
    print("8. Armstrong Number")
    print("9. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sum_two_numbers()
    elif choice == 2:
        odd_even()
    elif choice == 3:
        factorial()
    elif choice == 4:
        fibonacci()
    elif choice == 5:
        reverse_string()
    elif choice == 6:
        palindrome()
    elif choice == 7:
        leap_year()
    elif choice == 8:
        armstrong()
    elif choice == 9:
        break
    else:
        print("Invalid choice")