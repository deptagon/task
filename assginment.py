def find_greatest_of_three():
    """Prompt for three integers and print the greatest."""
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    greatest = num1
    if num2 > greatest:
        greatest = num2
    if num3 > greatest:
        greatest = num3
    print(f"{greatest} is the greatest number.")


def month_name_from_number():
    """Prompt for month number and print month name."""
    month_number = int(input("Enter a month number (1-12): "))
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    if 1 <= month_number <= 12:
        print("Month:", months[month_number - 1])
    else:
        print("Invalid month number!")


def swap_two_numbers():
    """Prompt for two numbers and swap them."""
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    print("Before swapping: a =", a, ", b =", b)
    a, b = b, a
    print("After swapping:  a =", a, ", b =", b)


def movie_ticket_price():
    """Calculate ticket price based on age and membership."""
    age = int(input("Enter your age: "))
    member = input("Do you have a membership card? (yes/no): ").strip().lower()
    if age < 12:
        price = 0
    elif 12 <= age <= 60:
        price = 150 if member == "yes" else 200
    else:
        price = 100
    print("Ticket Price:", "Rs.", price if price else "FREE")


def electricity_bill_calculator():
    """Compute electricity bill based on units used."""
    units = int(input("Enter electricity usage in units: "))
    if units < 100:
        cost = units * 5
    elif units <= 300:
        cost = 100 * 5 + (units - 100) * 8
    else:
        cost = 100 * 5 + 200 * 8 + (units - 300) * 10
    print("Total Electricity Bill: Rs", cost)


def even_odd_positive_check():
    """Check if a number is positive, then even or odd."""
    num = int(input("Enter a number: "))
    if num > 0:
        if num % 2 == 0:
            print("The number is EVEN.")
        else:
            print("The number is ODD.")
    else:
        print("The number is NOT positive.")


def compare_two_numbers_and_sign():
    """Compare two floats; if equal, also determine sign (positive/negative/zero)."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if a > b:
        print(a, "is greater.")
    elif b > a:
        print(b, "is greater.")
    else:
        print("Both numbers are equal.")
        if a > 0:
            print("The number is positive.")
        elif a < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")


def fizz_buzz():
    """Simple FizzBuzz: print Fizz if divisible by 3, Buzz if by 5, Fizz Buzz if both, else number."""
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


def discount_calculator():
    """Apply discount based on total amount and membership status."""
    total_amount = float(input("Enter total purchase amount: Rs "))
    is_member_input = input("Are you a member? (True/False): ").strip()
    is_member = True if is_member_input.lower() == "true" else False

    if total_amount > 1000 and is_member:
        discount_rate = 0.20
    elif total_amount > 1000 and not is_member:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    final_amount = total_amount * (1 - discount_rate)
    print("Final amount to pay: Rs", final_amount)


def main_menu():
    """Display menu of all programs and let user choose which one to run."""
    options = {
        "1": ("Find greatest of three numbers", find_greatest_of_three),
        "2": ("Get month name from number", month_name_from_number),
        "3": ("Swap two values", swap_two_numbers),
        "4": ("Movie ticket price calculator", movie_ticket_price),
        "5": ("Electricity bill calculator", electricity_bill_calculator),
        "6": ("Even/Odd and positive check", even_odd_positive_check),
        "7": ("Compare two numbers and check sign", compare_two_numbers_and_sign),
        "8": ("FizzBuzz", fizz_buzz),
        "9": ("Discount calculator", discount_calculator),
        "0": ("Exit", None)
    }

    while True:
        print("\nChoose a program to run:")
        for key, (desc, _) in sorted(options.items()):
            print(f"  {key}. {desc}")
        choice = input("Enter option number: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice in options:
            _, func = options[choice]
            func()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
