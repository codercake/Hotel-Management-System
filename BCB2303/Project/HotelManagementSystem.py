rooms = [
    {"name": "Single Room", "rate": 100, "booked": False, "guest_name": None},
    {"name": "Double Room", "rate": 150, "booked": False, "guest_name": None},
    {"name": "Suite", "rate": 250, "booked": False, "guest_name": None}
]

# Function to display the main menu
def display_menu():
    print("\nWelcome to Wanderlust Hotel")
    print("1. Book a Room")
    print("2. Search Rooms by Name")
    print("3. Complimentary Breakfast")
    print("4. View Booked Rooms")
    print("5. Advanced Payment Methods")
    print("6. Checkout")
    print("7. Exit")

#Function to book a room
def book_room():
    print("\nAvailable Rooms:")
    for i, room in enumerate(rooms):
        if not room["booked"]:
            print(f"{i+1}. {room['name']} - ${room['rate']} per night")
    
    room_choice = int(input("Enter the room number you want to book: ")) - 1
    guest_name = input("Enter your name: ")
    
    if not rooms[room_choice]["booked"]:
        rooms[room_choice]["booked"] = True
        rooms[room_choice]["guest_name"] = guest_name
        print(f"Room {rooms[room_choice]['name']} has been booked successfully for {guest_name}!")
    else:
        print("Sorry, the selected room is already booked.")

#Function to search rooms by guest name
def search_room_by_name():
    guest_name = input("\nEnter the guest's name to search for their room: ")
    found = False
    for room in rooms:
        if room["guest_name"] == guest_name:
            print(f"{guest_name} has booked the {room['name']}.")
            found = True
            break
    if not found:
        print(f"No rooms booked under the name {guest_name}.")

#Function to view the complimentary breakfast menu
def complimentary_breakfast():
    print("\nComplimentary Breakfast Menu:")
    print("1. Continental Breakfast")
    print("2. American Breakfast")
    print("3. Vegan Breakfast")
    choice = int(input("Please select your breakfast option (1-3): "))
    breakfast_menu = ["Continental", "American", "Vegan"]
    print(f"You have selected the {breakfast_menu[choice-1]} Breakfast.")

#Function to view all booked rooms
def view_booked_rooms():
    print("\nBooked Rooms:")
    booked_rooms = [room for room in rooms if room["booked"]]
    if booked_rooms:
        for room in booked_rooms:
            print(f"{room['name']} booked by {room['guest_name']}")
    else:
        print("No rooms are currently booked.")

#Function to handle payment methods
def payment_methods():
    print("\nAdvanced Payment Methods")
    print("1. UPI")
    print("2. Net Banking")
    print("3. Cash")
    method = int(input("Select your payment method (1-3): "))
    if method == 1:
        print("Payment successful via UPI.")
    elif method == 2:
        print("Payment successful via Net Banking.")
    elif method == 3:
        print("Payment successful via Cash.")
    else:
        print("Invalid payment method selected.")

#Function to handle checkout
def checkout():
    guest_name = input("\nEnter your name for checkout: ")
    for room in rooms:
        if room["guest_name"] == guest_name:
            room["booked"] = False
            room["guest_name"] = None
            print(f"{guest_name}, you have successfully checked out from the {room['name']}.")
            print("Please leave a review and rating on Google!")
            break
    else:
        print(f"No booking found under the name {guest_name}.")

#Loop to allow multiple operations
while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_room()
    elif choice == 2:
        search_room_by_name()
    elif choice == 3:
        complimentary_breakfast()
    elif choice == 4:
        view_booked_rooms()
    elif choice == 5:
        payment_methods()
    elif choice == 6:
        checkout()
    elif choice == 7:
        print("Exiting Wanderlust Hotel. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
