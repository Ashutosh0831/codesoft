import random
import string


def generate_password(length=len, use_digits=True, use_specials=True):
    characters = string.ascii_letters  # a-z + A-Z

    if use_digits:
        characters += string.digits     # 0-9
    if use_specials:
        characters += string.punctuation  # !@#$%^&*()_+ etc.

    if not characters:
        raise ValueError("No characters available to generate a password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
	while True:
		print("*************************")
		print("1 --> To generate_password \n2 --> To generate another password \n3 --> To exit")
		ch = int(input("Enter your choice::"))
		if ch == 1:
			len = int(input("Enter the lenght of the password::"))
			k = generate_password(len)
			print("Generated-Password :: ", k)
		elif ch == 2:
			len = int(input("Enter the lenght of the password::"))
			g = generate_password(len)
			print("Generated-Password :: ", g)
		elif ch == 3:
			print("Thank you !")
			exit()
		else:
			print("Invalid choice!")

main()
