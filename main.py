try:
    sequence = [4, 8, 15, 16, 23, 42]
    formatted_output = " ".join([f"{num}" for num in sequence])
    print(formatted_output)
except Exception as e:
    print(f"An error occurred: {e}")    

try:
    sequence = [4, 8, 15, 16, 23, 42]
    for num in sequence:
        print(f"{num}")
except Exception as e:
    print(f"An error occurred: {e}")


try:
    num = int(input("Enter a number: "))
    print(f"{num}\n{num + 1}\n{num + 2}")
except Exception as e:
    print(f"An error occurred: {e}")

    
try:
    a = int(input())
    b = int(input())
    c = int(input())
    print(a + b + c)
except Exception as e:
    print(f"An error occurred: {e}")


try:
    edge = int(input())
    volume = edge ** 3
    surface_area = 6 * (edge ** 2)
    print(f"Volume = {volume}\nTotal surface area = {surface_area}")
except Exception as e:
    print(f"An error occurred: {e}")


try:
    n = int(input())
    k = int(input())
    per_student = k // n
    remainder = k % n
    print(per_student)
    print(remainder)
except Exception as e:
    print(f"An error occurred: {e}")


try:
    number = int(input())
    if 999 < number < 10000:
        print(f"The digit in the thousands position is {number // 1000}")
        print(f"The number in the hundreds position is {(number % 1000) // 100}")
        print(f"The digit in the tens position is {(number % 100) // 10}")
        print(f"The digit in the position of units is {number % 10}")
    else:
        print("Please enter a four-digit number.")
except Exception as e:
    print(f"An error occurred: {e}")


try:
    population = int(input())
    survivors = (population + 1) // 2
    print(survivors)
except Exception as e:
    print(f"An error occurred: {e}")


try:
    num = int(input())
    shifted_num = num << 1
    if shifted_num == 0:
        print("The result is zero.")
    else:
        print(f"The result of << is {shifted_num}")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    operation = input("Please choose the operation (+, -, *, /) : ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        result = num1 / num2
    else:
        print("Invalid operation chosen.")
        raise ValueError
    print(f"{num1} {operation} {num2} = {result}")
except Exception as e:
    print(f"An error occurred: {e}")

