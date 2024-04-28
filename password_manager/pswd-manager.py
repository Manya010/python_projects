from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def save_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        key = generate_key()
        save_key(key)
    with open("key.key", "rb") as key_file:
        return key_file.read()

master_pwd = input("WHAT IS YOUR MASTER PASSWORD? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if not data:
                continue
            
            parts = data.split("|")
            if len(parts) == 2:
                user, pswd = parts
                try:
                    decrypted_password = fer.decrypt(pswd.encode()).decode()
                    print("User:", user, "| Password:", decrypted_password)
                except:
                    print("Error decrypting password for user:", user)
            else:
                print("Invalid format in password.txt:", data)

def add():
    name = input("Account name:")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open('password.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("WOULD YOU LIKE TO ADD A NEW PASSWORD OR VIEW EXISTING ONES (view or add), PRESS q TO QUIT ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("INVALID MODE.")
        continue

