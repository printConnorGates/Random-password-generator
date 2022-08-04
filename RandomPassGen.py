# This script will create a secure randomly generated password for you.
import secrets
import string 

def password_generate(password_length):
    
    characters = string.ascii_letters + string.digits
    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))
    
    return secure_password

def main():

    user_password_length = int(input("Input number of digits for password: "))
   
    print("Your randomly generated password is: ", password_generate(user_password_length))

main()

