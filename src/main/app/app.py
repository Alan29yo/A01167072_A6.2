from src.main.classes.Hotel import Hotel
from src.main.classes.Customer import Customer
from src.main.classes.Reservation import Reservation
import datetime as dt

if __name__ == '__main__':
    # Create hotel
    hotel1 = Hotel("Grand Hotel", "52 Park Avenue", 100)
    hotel2 = Hotel("Premium Hotel", "13 Royal Street", 150)
    print(f"Hotel '{hotel1.name}' created")
    print(f"Hotel '{hotel2.name}' created")

    # Delete hotel
    hotel2_name = hotel2.name
    del hotel2
    print(f"Hotel '{hotel2_name}' deleted")

    # Display hotel info
    print(f"\n{hotel1.name} info:")
    hotel1.display_info()
    print()

    # Modify Hotel Info
    message1 = hotel1.modify_hotel_info("name", "New Grand Hotel")
    print(message1)
    print(f"Hotel name changed to: {hotel1.name}")

    # Reserve a room (from Hotel method)
    room = hotel1.reserve_rooms(1)[0]   # Reserve 1 room, then get room number

    # Cancel reservation (from Hotel method)
    message = hotel1.remove_reservation(room)
    print(message)
    print("\n")


    # Create customer
    cust1 = Customer("Alan Cortés", 31, 33004422, "alan_cortes@mail.com")
    cust2 = Customer("Omar Zamora", 23, 54435566, "omar_zamora@mail.com")
    print(f"Customer '{cust1.name}' created")
    print(f"Customer '{cust2.name}' created")

    # Delete customer
    cust2_name = cust2.name
    del cust2
    print(f"Customer '{cust2_name}' deleted")

    # Display customer info
    print(f"\n{cust1.name} info:")
    cust1.display_info()
    print()

    # Modify customer info
    message2 = cust1.modify_customer_info("phone_number", 584883004)
    print(message2)
    print(f"Phone number changed to: {cust1.phone_number}")
    print("\n")


    # Create reservation (from reservation method)
    date = dt.datetime(2025, 5, 22)
    res1 = Reservation(1, cust1, hotel1, date)

    # Display reservation info
    print(f"\nReservation '{res1.reservation_id}' info:")
    res1.display_info()
    print()

    # Cancel reservation (from reservation method)
    message = res1.cancel_reservation()
    print(message)
