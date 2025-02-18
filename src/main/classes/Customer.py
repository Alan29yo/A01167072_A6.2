"""
Customer module
"""

class Customer:
    """
    Customer class
    """
    def __init__(self, name, age, phone_number, email):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email

    def display_info(self):
        """
        Display customer info
        """
        for key, val in self.get_customer_info().items():
            print(f"{key}: {val}")

    def get_customer_info(self):
        """
        Get customer info
        """
        customer_info = {
            "Name": self.name,
            "Age": self.age,
            "Phone number": self.phone_number,
            "E-mail": self.email,
        }
        return customer_info

    def modify_customer_info(self, attr, value):
        """
        Modify customer info
        """
        if hasattr(self, attr):
            setattr(self, attr, value)
            return f"Customer info has been updated for attribute '{attr}'"
        return f"ERROR: Customer has no attribute '{attr}'"
