import pikepdf  #py -m pip install pikepdf
import time


def cracking_pdf (passwordFile):

    print("Things are running in the background!\n")

    password_attempts = 1
    
    for currentGuess in passwordFile:

        print("Trying out the password ", currentGuess.strip())

        try:
            pdf = pikepdf.open("Cats.pdf", password = currentGuess.strip())

            print("It took ", password_attempts, " to guess the password")
            pdf.save("Cracked_PDF.pdf")
            pdf.close()
            
            return currentGuess
     
        except (pikepdf._core.PasswordError):
            password_attempts += 1
            pass
     
        except (FileNotFoundError):
            print("ERROR: PDF File Not Found")
            exit(1)

        except Exception as e:
            print(e)

            exit(1)

    print("We checked ", password_attempts, " different passwords, but wasn't able to get this one :(")
    return 



try: 
    passwordFile = open("password_list_3.txt", 'r')

except(FileNotFoundError):
    print("ERROR: Password File not Found");
    exit(1)


timeStart = time.time()
password = cracking_pdf(passwordFile)
timeEnd  = time.time() 

totalTime = timeEnd - timeStart


if (password):
    print("The password was found!!!")
    print(password.strip(), " was the password")
    print("It took", totalTime," seconds to crack the password")

else:  
    print("The password was not found :(")
    print("It took", totalTime,"to check all the passwords")
