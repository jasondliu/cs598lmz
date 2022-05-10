import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

def main():
    # Set up some test data
    dictionary = {"first_name": "Colin", "last_name": "Williams", "address": "123 Main Street"}

    # Run the function and get the resulting dictionary
    dictionary = create_dict(dictionary)

    # Print the resulting dictionary to the console
    print(dictionary)

def create_dict(dictionary):
    # Create a new dictionary to populate
    new_dict = {}

    # Iterate over the original dictionary and create new key, value pairs
    for key, value in dictionary.items():
        new_key = key.replace("_", " ").title()
        new_dict[new_key] = value

    # Return the new dictionary
    return new_dict

if __name__ == "__main__":
    main()
</code>

