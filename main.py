# Random Password generator.

# import random module.
import random

# Ask user for the acquired length of the password.
Password_length = int(input("Enter the Length of the password: "))

# data including alphabets, digits and symbols to use in the password.
password_data = 'qwertyuiopasdfghjklzxcvbnm123456789;,.!@#$%^&*'

# random.sample() to collect random data & using .join() to join the list elements to form a string.
Password = "".join(random.sample(password_data, Password_length))

# Print the password generated.
print("Here is the generated password: ", Password)
