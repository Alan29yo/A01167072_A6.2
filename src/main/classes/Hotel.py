"""
Hotel module
"""

class Hotel:
    """
    Hotel class
    """
    rating = None           # Average customer rating
    reservations = {}       # Includes customer name
    available_rooms = int   # Rooms with status 'Available'
    rooms = {}              # Room number, status, pairs

    def __init__(self, name: str, address: str, total_rooms: int):
        self.name = name
        self.address = address
        self.total_rooms = total_rooms
        self.set_rooms(total_rooms)

    def set_rooms(self, total_rooms):
        """
        Set hotel rooms
        """
        self.rooms = {"Room " + str(num): 'Available' for num in range(total_rooms)}
        self.available_rooms = total_rooms

    def display_info(self):
        """
        Display hotel info
        """
        for key, val in self.get_hotel_info().items():
            print(f"{key}: {val}")

    def get_hotel_info(self):
        """
        Get hotel info
        """
        hotel_info = {
            "Name": self.name,
            "Address": self.address,
            "Total rooms": self.total_rooms,
            "Rating": self.rating,
            "Available rooms": self.available_rooms
        }
        return hotel_info

    def modify_hotel_info(self, attr, value):
        """
        Modify hotel info
        """
        if hasattr(self, attr):
            setattr(self, attr, value)
            return f"Hotel info has been updated for attribute '{attr}'"
        return f"ERROR: Hotel has no attribute '{attr}'"

    def reserve_rooms(self, qty):
        """
        Reserve hotel rooms
        """
        if self.available_rooms >= qty:
            reservation_list = []
            for _ in range(qty):
                room = self.find_first_available_room()
                self.rooms[room] = 'Reserved'
                self.available_rooms -= 1
                reservation_list.append(room)
            print(f"{qty} rooms have been reserved: {reservation_list}")
            return reservation_list
        return ("Unfortunately there are not enough available rooms. "
                    "Available rooms: ") + str(self.available_rooms)

    def find_first_available_room(self):
        """
        Find first available room
        """
        for key, val in self.rooms.items():
            if self.rooms[key] == val:
                return key
        return "Couldn't find any available room"

    def remove_reservation(self, room_number):
        """
        Remove room reservation
        """
        if self.rooms[room_number] == 'Reserved':
            self.rooms[room_number] = 'Available'
            self.available_rooms += 1
            print(f"Reservation for {room_number} has been removed")
            return f"Reservation for {room_number} has been removed"
        return f"Couldn't remove reservation for {room_number}. Room already available"
