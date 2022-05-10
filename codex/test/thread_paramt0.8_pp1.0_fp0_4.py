import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()
 
# Query the user to enter the amount of donations 
total = int(input("\nHow many donations do you wish to Enter: "))
 
# Starts the loop to enter user data
for i in range(0, total):
    # Query the user to enter donation amount and name
    # Note that I'm using float(input()) for numerical input
    # and input for strings
    amount = float(input("\nEnter the donation amount: "))
    name = input("Enter the donors first and last name: ")
 
    # Adds the amount to the donations list
    donations.append(amount)
 
    # Adds the name to the donors list
    donors.append(name)
 
    # Adds the donation to the list of lists by combining both lists
    # Note: I could have used the append method to create a list containing 
    # both amount and name and then append it to the donations_data list
    # This way is just more simple
    donations_data.append([amount, name])
 
# Display the table
