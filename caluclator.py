print("simple caluclator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: ))

print("Choose operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
  print("Result:", a + b)
elif choice == "2":
  print("Result:", a - b)
elif choice == "3":
  print("Result:", a * b)
elif choice == "4":
  print("Result:", a / b)
else:
  print("Invalid choice")
