import random 

print("PasswordGenerator by Htc")

chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!£$%&^*@?'
num_char = len(input("how long should be your password?"))
new_num_char = int(num_char)
print("Your password has" + new_num_char + "characters.")

password = ''
for i in range(num_char):
    password += random.choice(chars)

print(password)
print("Your password is done!")
