import random 

print("PasswordGenerator by Htc")

chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!£$%&^*@?'

while True:
    try:
        num_char = int(input("how long should be your password?"))
    except ValueError:
        print("please enter a number")
    else:
        break
    
print("Your password has %d characters." % num_char)

password = ''
for i in range(num_char):
    password += random.choice(chars)

print(password)
print("Your password is done!")
