"""
Test Customer module
"""

import unittest
from src.main.classes.Customer import Customer

class TestCustomerMethods(unittest.TestCase):
    """
    Test Customer class
    """
    def setUp(self):
        self.customer = Customer("Alan Cortés", 31, 33004422, "alan_cortes@mail.com")

    def test_create_customer(self):
        """
        Test create customer
        """
        self.assertIsInstance(self.customer, Customer)

    def test_get_customer_info(self):
        """
        Test get customer info
        """
        cust_info_expected = {
            "Name": "Alan Cortés",
            "Age": 31,
            "Phone number": 33004422,
            "E-mail": "alan_cortes@mail.com",
        }
        cust_info_actual = self.customer.get_customer_info()

        self.assertEqual(cust_info_expected, cust_info_actual)

    def test_modify_customer_info(self):
        """
        Test modify customer info
        """
        self.customer.modify_customer_info("phone_number", 584883004)
        self.assertEqual(584883004, self.customer.phone_number)

if __name__ == '__main__':
    unittest.main()
