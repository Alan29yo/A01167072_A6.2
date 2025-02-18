"""
Test Reservation module
"""

import unittest
import datetime as dt
from src.main.classes.Reservation import Reservation
from src.main.classes.Customer import Customer
from src.main.classes.Hotel import Hotel

class TestReservationMethods(unittest.TestCase):
    """
    Test Reservation class
    """
    def setUp(self):
        self.hotel = Hotel("Grand Hotel", "52 Park Avenue", 100)
        self.customer = Customer("Alan Cortés", 31, 33004422, "alan_cortes@mail.com")
        date = str(dt.datetime(2025, 5, 22))
        self.reservation = Reservation(1, self.customer, self.hotel, date)

    def test_create_reservation(self):
        """
        Test create reservation
        """
        self.assertIsInstance(self.reservation, Reservation)

    def test_get_reservation_info(self):
        """
        Test get reservation info
        """
        reservation_info_expected = {
            "Reservation ID": 1,
            "Customer name": "Alan Cortés",
            "Hotel": "Grand Hotel",
            "Room number": "Room 0",
            "Reservation date": "2025-05-22 00:00:00",
            "Reservation status": "Active"
        }
        reservation_info_actual = self.reservation.get_reservation_info()
        self.assertEqual(reservation_info_expected, reservation_info_actual)

    def test_cancel_reservation(self):
        """
        Test cancel reservation
        """
        self.reservation.cancel_reservation()
        self.assertEqual("Cancelled", self.reservation.reservation_status)

if __name__ == '__main__':
    unittest.main()
