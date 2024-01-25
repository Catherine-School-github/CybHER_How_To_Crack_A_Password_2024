import pikepdf  #py -m pip install pikepdf
import time


def cracking_pdf (passwordFile):

    print("Don't worry! Things are being done in the background even if you can't see anything. It might take a few minutes so sit back and relax!!\n")
    
    for currentGuess in passwordFile:

        print("Trying out the password ", currentGuess.strip())

        try:
            #pdf = "open PDF here"
            
            pdf.close()

            #return password
     
        except (pikepdf._core.PasswordError):

            pass
     
        except (FileNotFoundError):
            print("ERROR: PDF File Not Found")
            exit(1)

        except Exception as e:
            print(e)

            exit(1)


    return 



try: 
    passwordFile = open("password_list.txt", 'r')

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
