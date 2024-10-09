#Room data as a list of dictionaries
rooms = [
    {"name": "Single Room", "rate": 100, "booked": False, "guest_name": None},
    {"name": "Double Room", "rate": 150, "booked": False, "guest_name": None},
    {"name": "Suite", "rate": 250, "booked": False, "guest_name": None}
]

#Main program loop
while True:
    print("\nWelcome to SlyPy Hotel")
    print("1. Book a Room")
    print("2. Search Rooms by Guest Name")
    print("3. Complimentary Breakfast")
    print("4. View Booked Rooms")
    print("5. Payment Methods")
    print("6. Checkout")
    print("7. Display Room Details")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
        
        #Display Room Details
        if choice == 7:
            for room in rooms:
                print(f"Room Name: {room['name']}, Rate: ${room['rate']}, Is Booked: {'Yes' if room['booked'] else 'No'}")

        #Book a Room
        elif choice == 1:
            print("\nAvailable Rooms:")
            available_rooms = [i for i, room in enumerate(rooms) if not room["booked"]]
            for i in available_rooms:
                print(f"{i + 1}. {rooms[i]['name']} - ${rooms[i]['rate']}")
            if not available_rooms:
                print("No rooms are available for booking.")
                continue
            
            room_choice = int(input("Enter the room number you want to book: ")) - 1
            if room_choice in available_rooms:
                guest_name = input("Enter your name: ").strip()
                rooms[room_choice]["booked"] = True
                rooms[room_choice]["guest_name"] = guest_name
                print(f"Room {rooms[room_choice]['name']} has been booked by {guest_name}.")
            else:
                print("Invalid room choice.")

        #Search Rooms by Guest Name
        elif choice == 2:
            guest_name = input("\nEnter the guest's name to search: ").strip().lower()
            found = False
            for room in rooms:
                if room["guest_name"] and room["guest_name"].lower() == guest_name:
                    print(f"{guest_name.capitalize()} has booked the {room['name']}.")
                    found = True
            if not found:
                print(f"No rooms found under the name {guest_name}.")

        #Complimentary Breakfast
        elif choice == 3:
            breakfast_options = ("Continental", "American", "Vegan")
            print("\nComplimentary Breakfast Menu:")
            for i, option in enumerate(breakfast_options):
                print(f"{i + 1}. {option}")
            choice = int(input("Please select your breakfast option (1-3): "))
            if 1 <= choice <= 3:
                print(f"You have selected the {breakfast_options[choice - 1]} Breakfast.")
            else:
                print("Invalid option.")

        #View Booked Rooms
        elif choice == 4:
            booked_rooms = [room for room in rooms if room["booked"]]
            if booked_rooms:
                for room in booked_rooms:
                    print(f"{room['name']} booked by {room['guest_name']}")
            else:
                print("No rooms are booked.")

        # Payment Methods
        elif choice == 5:
            payment_options = {1: "UPI", 2: "Net Banking", 3: "Cash"}
            print("\nPayment Methods:")
            for key, value in payment_options.items():
                print(f"{key}. {value}")
            method = int(input("Select your payment method (1-3): "))
            if method in payment_options:
                print(f"Payment successful via {payment_options[method]}.")
            else:
                print("Invalid payment method.")

        #Checkout
        elif choice == 6:
            guest_name = input("Enter your name for checkout: ")
            room_choice = int(input("Enter the room number you are checking out from: ")) - 1
            if 0 <= room_choice < len(rooms) and rooms[room_choice]["booked"]:
                print(f"{guest_name} has checked out of {rooms[room_choice]['name']}.")
                rooms[room_choice]["booked"] = False
                rooms[room_choice]["guest_name"] = None
            else:
                print("Invalid room choice or room not booked.")

        elif choice == 8:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")
