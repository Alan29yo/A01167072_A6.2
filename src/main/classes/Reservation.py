"""
Reservation module
"""
class Reservation:
    """
    Reservation class
    """
    def __init__(self, reservation_id, customer, hotel, reservation_date):
        self.reservation_id = reservation_id
        self.customer = customer
        self.hotel = hotel
        self.room_number = hotel.reserve_rooms(1)[0]    # Reserve 1 room, then get room number
        self.reservation_date = reservation_date
        self.reservation_status = "Active"

    def display_info(self):
        """
        Display reservation info
        """
        for key, val in self.get_reservation_info().items():
            print(f"{key}: {val}")

    def get_reservation_info(self):
        """
        Get reservation info
        """
        reservation_info = {
            "Reservation ID": self.reservation_id,
            "Customer name": self.customer.name,
            "Hotel": self.hotel.name,
            "Room number": self.room_number,
            "Reservation date": self.reservation_date,
            "Reservation status": self.reservation_status
        }
        return reservation_info

    def cancel_reservation(self):
        """
        Cancel reservation
        """
        self.hotel.remove_reservation(self.room_number)
        self.reservation_status = "Cancelled"
        return "Your reservation has been cancelled"
