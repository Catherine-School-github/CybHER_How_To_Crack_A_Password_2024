#NOTE: THIS IS OVERCOMMENTED DUE TO THE SENSITIVE NATURE OF ENTERING A PASSWORD. THOUGH NOTHING GETS LOGGED, IT IS IMPORTANT EVERYONE CAN KNOW EXACTLY WHAT IS HAPPENING AND WHY
#NOTE: probably delete most comments when giving to the campers otherwise it tooks 1000x more complicated
from hashlib import sha1 #uses hashlib to convert the password you type to sha1

hashfile = open("pwnedpasswordlist.txt", "r") #opens a read-only file full of millions and millions of hashes

password = input("Please enter your password to check: ") #asks user to enter their password. NOTHING IS STORED OR SENT VIA INTERNET

password = sha1(password.strip().encode()).hexdigest() #hashes the password in sha1 to check it against the millions and millions of hashes

checked_password = 0 #variable to keep track how many times in loop we are in, not needed but helps make sure program didn't crash and is still running

found_password = False #variable to tell if a password was found

for hibp_hash in hashfile: #for loop to go through all the millions of passwords to make sure we check every single one
	hibp_hash = hibp_hash[0:40].lower() #makes it so only the first 40 characters of the hash is checked checked from the hashfile, and makes all the letters lowercase so we can compare it to the hash of the user entered password
	
	checked_password += 1 #adds one to checked_password to help make sure the program didn't crash. 
	
	if (hibp_hash.strip() == password.strip()): #if the hash password is equal to the hash of the password the user entered
		found_password = True #sets the found_password variable equal to true, as we found the password
		break #break to end the loop early so we don't waste time when we already know the answer
	
	#NOTE: below 500000 is just a magic number I felt was good enough to make sure program was working, number was just arbitrairly chosen.
	if (checked_password % 500000 == 0): #periodic display to make sure that the program is still running while not costing to much to check and print
		print("Still working, just checked hash", hibp_hash.strip(), "with", password.strip()) #displays the current hash checking with the hash the user entered
		
	#NOTE: FOR BELOW TO WORK THE LIST MUST BE SORTED
	if (hibp_hash.strip() > password.strip()): #if the hash is "greater" than the hash of the password, we know the hash does not exist in the password file therefore we can leave early
		break	#break to end the loop early as we know that the password the user entered is not in the password list


if (found_password): #if the password was found in the millions and millions of hashed password
	print("YOUR PASSWORD WAS FOUND!!!! CHANGE YOUR PASSWORD IMMEDIETLY") #warns the user the password was found
	print("ANY ACCOUNT WITH THIS PASSWORD IS INSECURE, CHANGE THE PASSWORD TO ALL ACCOUNTS WITH THIS PASSWORD OTHERWISE YOU ARE AT RISK") #tells the user that their accounts are insecure and they really should change their passwords
	
else: #else the password was not found
	print("Your password was not found in the list") #tells the user the password was not found in the list
	print("That doesn't mean this password is secure, it just wasn't found in this list") #tells the user that it's not necessairly a secure password, but just wasn't found here
