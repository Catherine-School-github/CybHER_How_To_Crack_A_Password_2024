import random
import time 

def cracking (pin_code):
    
    #code brute force here


pinCode = random.randint(0, 9999) 

pinCode = ("{:04d}".format(pinCode))
startTime = time.time() 

crackedPin = cracking(pinCode)
endTime = time.time() 

totalTime = endTime - startTime 

print("The pin", crackedPin, "was cracked")
print("It took", "%2f" % totalTime,  "seconds to crack the code")

