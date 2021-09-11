import random
import string
import clipboard
from time import sleep


def store_password():
  	# username
	username = str(input("Your username: "))
  	# website
	website = str(input("Website: "))
  	# generate random password
	gen_or_man = str(input("Do you want to make your password, or have it generated? (manual or generated)"))
	if gen_or_man == "generated":
		digit = int(input("How many digits do you want? (integer only) "))
		password = ""
		for i in range(digit):
			char = random.choice(string.ascii_letters)
			password += char
	else:
		manual = str(input("What do you want your password to be? "))
		password = ""
		password += manual

	# store the password into a file
	f = open("password.txt", "a")
	f.write(f"{username}-{website}-{str(password)}\n")
	f.close()

	print(f"Here's your password: {password}")
	sleep(60)


#######

def search():
	username_or_website = str(input("Do you want to search for username or website? "))
	value = str(input("What value? "))
	f = open("password.txt", "r")
	for line in f:
		info = line.split("-")
		if username_or_website == "username":
			if value == info[0]:
				return info[2]
			# search by username
		else:
			# search by website
			if value == info[1]:
				return info[2]

def pass_choice():
  choice = str(input("Do you want to 'search' or 'create' a password? "))
  if choice == "search":            
    result = search()
    if result == None:
      print("No result found")
      sleep(60)
    else:
        clipboard.copy(result)
        print(f"{result}PASSWORD COPIED TO CLIPBOARD")
        sleep(60)
  else:
    if choice == "create":
      store_password()
pass_choice()
