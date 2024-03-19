from hashlib import sha1
import time

breachInfo = open("breached_system.txt", "r")

passwordList = open("rainbowTable.txt", "r")

cracked_list = open ("cracked_information.txt", "w") #stores cracked info (email + username + plaintext password)

line_tracker = 0

pwned_accounts = 0;

total_accounts = 0 #maybe bonus points

start_time = time.time() #DELETE WITH FINAL. THIS IS JUST FOR TESTING
for users in breachInfo:
	
	
	if(line_tracker % 3 == 0): #email is found on every 3rd line starting at line 0
		total_accounts += 1 #maybe bonus points
		print("\nEmail:", users.strip())
		email = (users.strip())
	
	elif(line_tracker % 3 == 1): #username is found on every 3rd line starting at 1
		print("Username:", users.strip())
		username = users.strip()
	
	else:	#hashed password is found on every 3rd line starting at 2. else statement and not elif as it's the only option possitble after email and username check
		print("Hashed Password:", users.strip())
		hashed_password = users.strip()
	
		#print("\nCracking the password to", email)
		for current_guess in passwordList: #cracking the hashed password with an nested for loop
			
			if(current_guess.strip() == hashed_password): #if the hexes match
				print("PASSWORD FOUND!!")
				found_password = passwordList.readline() #gets the next line of the file that contains the plaintext file to print it out
				print("The password belonging to", email, " is:", found_password)
				pwned_accounts += 1
				
				#DEBUGGING: writing cracked info to a textfile for debugging, maybe challenge
				cracked_list.write(email + "\n")
				cracked_list.write(username + "\n")
				cracked_list.write(found_password + "\n")
				
				break #break makes things so much faster as we are reducing the amount of time wasted going through the file if we already know the password (break = half runtime)

			passwordList.readline() #skips the next line of the rainbowTable as that is the plaintext password matching the above hash in the file
				
		passwordList.seek(0,0) #resets the read pointer of passwordList to the start of the rainbowtable file
			
	line_tracker += 1

end_time = time.time() #DELETE WITH FINAL, THIS IS JUST FOR TESTING

total_time = end_time - start_time #DELETE WITH FINAL, THIS IS JUST FOR TESTING
	
print("You pwned a total of ", pwned_accounts, " accounts out of ", total_accounts, " accounts, good job!") #bonus points if they get the total number of accounts they are hacking
print("It took a total of ", total_time, " to go through this database!") #DELETE WITH FINAL, THIS IS JUST FOR TESTING
	
