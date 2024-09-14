#Basic data for rooms, bookings, and rates
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
    print("7. View Booking History")
    print("8. Exit")

#Room booking function
def book_room():
    print("Select Room Type:")
    print("1. Single")
    print("2. Double")
    print("3. Suite")
    
    room_choice = int(input("Enter your choice (1, 2, or 3): "))
    room_types = {1: "single", 2: "double", 3: "suite"}
    
    if room_choice in room_types:
        room_type = room_types[room_choice]
        if rooms[room_type]["available"] > 0:
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
            print("Room booked successfully for {0} from {1} to {2}.".format(name, check_in, check_out))
        else:
            print("Room type unavailable or fully booked.")
    else:
        print("Invalid room type selected.")

#Check room availability
def search_room_by_name():
    print("Room Availability:")
    for room_type, details in rooms.items():
        print("{0} rooms available: {1}".format(room_type.title(), details["available"]))

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
            print("Name: {0}, Room: {1}, Check-in: {2}, Check-out: {3}".format(
                booking['name'],
                booking['room_type'].title(),
                booking['check_in'],
                booking['check_out']
            ))
    else:
        print("No rooms are currently booked.")

#Display payment methods
def payment_methods():
    print("Available Payment Methods:")
    print("1. UPI")
    print("2. Netbanking")
    print("3. Cash")

#handle checkout process
def checkout():
    name = input("Enter guest name for checkout: ")
    found_booking = None

    for booking in bookings:
        if booking["name"] == name:
            found_booking = booking
            break

    if found_booking:
        room_type = found_booking["room_type"]
        print("Checking out {0}. Room type: {1}".format(name, room_type.title()))
        payment_methods()
        payment_option = input("Choose a payment option (1, 2, 3): ")

        if payment_option in ["1", "2", "3"]:
            if payment_option == "1":  # UPI
                upi_id = input("Enter UPI ID (must contain '@'): ")
                if '@' in upi_id:
                    payment_details = upi_id
                else:
                    print("Invalid UPI ID. Payment failed.")
                    return
            else:
                payment_details = input("Enter payment details (e.g., Netbanking details, or Cash amount): ")
                
            print("Payment of {0} received. {1} checked out.".format(rooms[room_type]['rate'], name))
            rooms[room_type]["available"] += 1
            bookings.remove(found_booking)
        else:
            print("Invalid payment option.")
    else:
        print("Guest not found.")

#View booking history
def view_booking_history():
    if bookings:
        print("Booking History:")
        for booking in bookings:
            print("Name: {0}, Room: {1}, Check-in: {2}, Check-out: {3}".format(
                booking['name'],
                booking['room_type'].title(),
                booking['check_in'],
                booking['check_out']
            ))
    else:
        print("No booking history available.")

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
        view_booking_history()
    elif choice == 8:
        print("Exiting SlyPy Hotel. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
