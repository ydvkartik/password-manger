from cryptography.fernet import Fernet
'''
def write_key():
    key =Fernet.generate_key()
    with open("key.key",'wb') as keyfile:
        keyfile.write(key)

write_key()'''

def load_key():
    file=open("key.key","rb")
    key = file.read()
    file.close()
    return key


master_pwd= input("What is the master Passward? ")
key= load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("would you like to add nnew password or view the password (view, add)? ").lower()

    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid input")
        continue
