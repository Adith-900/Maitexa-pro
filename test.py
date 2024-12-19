# Try to input either integer or float
try:
    a = input("Enter a number: ")
    
    # Check if input is a valid integer
    if '.' not in a:
        a = int(a)
    else:
        a = float(a)
        
    if a < 0:
        print("Number is negative")
    elif a == 0:
        print("Number is zero")
    else:
        print("Number is positive")
        
except ValueError:
    print("Invalid input! Please enter a valid number.")
