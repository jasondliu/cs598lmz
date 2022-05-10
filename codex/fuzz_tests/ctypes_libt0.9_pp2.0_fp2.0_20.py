import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Name Changer")

def clear():
    os.system('cls')

def main():
    clear()
    print("""Welcome to "Nickname Generator"! (´−‿•)≡★
----------------------------------------------
Here you can find your own nickname.

1. That's what my mom calls me;
2. Luckiest nickname in the World;
3. Your name had a Party;
4. 6 letter nickname;
5. Hard to pronounce nickname;
6. I'm light, look at me;
7. A liquid in your name;
8. Translate your name;
9. Choose 1 number and symbol;
10. Everything but the Kitchen Sink

I will write all yours nicknames down.\n""")
    try:
        chose = int(input("Choose 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10: "))
        if chose == 1:
            clear()
            mother(input("What's is your name? "))
        elif chose == 2:
            clear()
            lucky(
