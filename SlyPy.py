rooms = {
    "single": {"rate": 1000, "available": 5},
    "double": {"rate": 2000, "available": 3},
    "suite": {"rate": 5000, "available": 2}
}

bookings = []

#Function to display the menu
def display_menu():
    print("\n--- Welcome to SlyPy Hotel ---")
    print("1. Book a Room")
    print("2. Check Room Availability")
    print("3. View Breakfast Menu")
    print("4. View Booked Rooms")
    print("5. Payment Methods")
    print("6. Checkout")
    print("7. Exit")

#Room booking function
def book_room():
    print("Available Room Types: Single, Double, Suite")
    room_type = input("Enter the room type you want to book: ").lower()

    if room_type in rooms and rooms[room_type]["available"] > 0:
        name = input("Enter guest name: ")
        check_in = input("Enter check-in date (DD-MM-YYYY): ")
        check_out = input("Enter check-out date (DD-MM-YYYY): ")

        rooms[room_type]["available"] -= 1
        bookings.append({
            "name": name,
            "room_type": room_type,
            "check_in": check_in,
            "check_out": check_out
        })
        print(f"Room booked successfully for {name} from {check_in} to {check_out}.")
    else:
        print("Room type unavailable or fully booked.")

#Search room availability by type
def search_room_by_name():
    print("Room Availability:")
    for room_type, details in rooms.items():
        print(f"{room_type.title()} rooms available: {details['available']}")

#View breakfast menu
def complimentary_breakfast():
    breakfast_menu = [
        "1. Pancakes",
        "2. Poha",
        "3. Cereal",
        "4. Fruit Salad",
        "5. Paratha"
    ]
    print("Breakfast Menu:")
    for item in breakfast_menu:
        print(item)

#View booked rooms
def view_booked_rooms():
    if bookings:
        print("Currently Booked Rooms:")
        for booking in bookings:
            print(f"Name: {booking['name']}, Room: {booking['room_type'].title()}, Check-in: {booking['check_in']}, Check-out: {booking['check_out']}")
    else:
        print("No rooms are currently booked.")

#Display payment methods
def payment_methods():
    print("Available Payment Methods: UPI, Netbanking, Cash")

#Checkout process
def checkout():
    name = input("Enter guest name for checkout: ")
    found_booking = None

    for booking in bookings:
        if booking["name"] == name:
            found_booking = booking
            break

    if found_booking:
        room_type = found_booking["room_type"]
        print(f"Checking out {name}. Room type: {room_type.title()}")
        print("Payment Options: 1. UPI 2. Netbanking 3. Cash")
        payment_option = input("Choose a payment option: ")

        if payment_option in ["1", "2", "3"]:
            print(f"Payment successful. {name} checked out.")
            rooms[room_type]["available"] += 1
            bookings.remove(found_booking)
        else:
            print("Invalid payment option.")
    else:
        print("Guest not found.")

#Main loop to allow multiple operations
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
        print("Exiting SlyPy Hotel. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
