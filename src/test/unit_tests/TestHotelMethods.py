"""
Test Hotel module
"""

import unittest
from src.main.classes.Hotel import Hotel

class TestHotelMethods(unittest.TestCase):
    """
    Test Hotel class
    """
    def setUp(self):
        self.hotel = Hotel("Grand Hotel", "52 Park Avenue", 100)

    def test_create_hotel(self):
        """
        Test create hotel
        """
        self.assertIsInstance(self.hotel, Hotel)

    def test_get_hotel_info(self):
        """
        Test get hotel info
        """
        hotel_info_expected = {
            "Name": "Grand Hotel",
            "Address": "52 Park Avenue",
            "Total rooms": 100,
            "Rating": None,
            "Available rooms": 100
        }
        hotel_info_actual = self.hotel.get_hotel_info()

        self.assertEqual(hotel_info_expected, hotel_info_actual)

    def test_modify_hotel_info(self):
        """
        Test modify hotel info
        """
        self.hotel.modify_hotel_info("name", "New Grand Hotel")
        self.assertEqual("New Grand Hotel", self.hotel.name)

    def test_reserve_rooms(self):
        """
        Test reserve rooms
        """
        room = self.hotel.reserve_rooms(1)[0]   # Reserve 1 room
        self.assertEqual("Reserved", self.hotel.rooms[room])

    def test_remove_reservation(self):
        """
        Test remove reservation
        """
        room = self.hotel.reserve_rooms(1)[0]   # Reserve 1 room
        self.hotel.remove_reservation(room)
        self.assertEqual("Available", self.hotel.rooms[room])

if __name__ == '__main__':
    unittest.main()
