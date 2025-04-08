#Assignment1 -Python Programming - Darshit Damania - Hero Vired DevOps_B11

#Q1 This is program is to check the password strength entered by the user
import time
import re
check_password_strength =input ("Enter the Password")
confirm_password = input ("Confirm the Password")
print ("Checking passwords entered")
time.sleep(3) # delay of 2 seconds
if check_password_strength !=confirm_password:
    print ("The password do not match, Please retry")
    exit()
else:
     print("The password entered is ",check_password_strength, "Checking Password Parameters......")

# Password Length check start
password_length = len(check_password_strength)
time.sleep(3)
if password_length <8:
    print ("Password Length Check Failed: The length of the password entered is ",password_length,"which is less than 8. Please retry")
    exit()
else:
    print("Password Length Check Confirmed..")
# Password Length check end

# Password Upper/Lower check start
time.sleep(3)
if any(char.islower() for char in check_password_strength): #Lower Case Check
    print("Lowercase Check Confirmed..")
else:
    print("Lowercase Check Failed: No lowercase letters found.Please retry")
    exit()
time.sleep(3)
if any(char.isupper() for char in check_password_strength): #Upper Case Check
    print("Uppercase Check Confirmed..")
else:
    print("Upper Case Check Failed: No uppercase letters found.Please retry")
    exit()
# Password Upper/Lower check End
# Password Number check start
time.sleep(3)
if not re.search(r"\d", check_password_strength):
        print("Number Check Failed: Password must contain at least one digit.")
        exit()
else:
    print("Number check Confirmed...")
# Password Number check End
# Password special character check Start
time.sleep(3)
if not re.search(r"[!@#$%^&*()\-_=+{};:'\",.<>?/|]", check_password_strength):
        print("Special Character Check Failed: Password must contain at least one special character.")
        exit()
else:
    print("Special Character Check Confirmed")
# Password special character check End
time.sleep(3)
print(check_password_strength,"is a great Password")
#
#
#
# Q2
#
#
#
#
#

