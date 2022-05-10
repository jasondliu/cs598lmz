import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("")
cracker = threading.Thread(group=None, target=None, name="cracker", args=(), kwargs={}, verbose=None, daemon=None)

word_list = []

# read password list
with open("password.lst", 'r') as file:
    for line in file:
        word_list.append(line.strip())

def crack_pass(word_list, salt):
    #  loop through each word in the word list
    for word in word_list:
        crypt_pass = crypt.crypt(word, salt)
        if crypt_pass == passwd:
            print("[+] Found password: ", word)
            return 
    print("[-] Password not found\n")

def main():
    print("[+] Cracking Password for user: " + user)
    crack_pass(word_list, salt)

if __name__ == "__main__":
    main()
