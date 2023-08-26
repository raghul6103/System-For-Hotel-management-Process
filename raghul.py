class Room:
    def __init__(self, room_number, capacity, price):
        self.room_number = room_number
        self.capacity = capacity
        self.price = price
        self.is_available = True
        self.guest = None

class HotelManagementSystem:
    def __init__(self):
        self.rooms = []
        self.guests = []

    def add_room(self, room_number, capacity, price):
        room = Room(room_number, capacity, price)
        self.rooms.append(room)

    def check_in(self, guest_name, guests_count):
        available_rooms = [room for room in self.rooms if room.is_available and room.capacity >= guests_count]
        if available_rooms:
            selected_room = available_rooms[0]
            selected_room.is_available = False
            selected_room.guest = guest_name
            self.guests.append((guest_name, selected_room))
            print(f"{guest_name} checked into room {selected_room.room_number}")
        else:
            print("No available rooms matching the capacity")

    def check_out(self, guest_name):
        room_to_checkout = None
        for guest, room in self.guests:
            if guest == guest_name:
                room_to_checkout = room
                break
        if room_to_checkout:
            room_to_checkout.is_available = True
            room_to_checkout.guest = None
            self.guests.remove((guest_name, room_to_checkout))
            print(f"{guest_name} checked out from room {room_to_checkout.room_number}")
        else:
            print(f"{guest_name} not found in the hotel")

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms if room.is_available]
        if available_rooms:
            print("Available rooms:")
            for room in available_rooms:
                print(f"Room {room.room_number} - Capacity: {room.capacity} - Price: ${room.price}")
        else:
            print("No available rooms")

if __name__ == "__main__":
    hotel = HotelManagementSystem()
    hotel.add_room(101, 2, 100)
    hotel.add_room(102, 4, 150)
    hotel.add_room(103, 2, 120)

    while True:
        print("\nHotel Management System Menu:")
        print("1. Check-in")
        print("2. Check-out")
        print("3. Display Available Rooms")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            guest_name = input("Enter guest name: ")
            guests_count = int(input("Enter number of guests: "))
            hotel.check_in(guest_name, guests_count)
        elif choice == 2:
            guest_name = input("Enter guest name: ")
            hotel.check_out(guest_name)
        elif choice == 3:
            hotel.display_available_rooms()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")
