import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)


def send_message_to_user(user, message):
    ctypes.windll.user32.MessageBoxW(0, message, user, 1)


if __name__ == "__main__":
    send_message_to_user("User", "Hello")
