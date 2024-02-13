import  pytest, ticket

def test_calculate_bus_ticket():
    # Test default price of ticket
    assert ticket.calculate_bus_ticket(20, False) == 4
    # Test infants/children under 3 years old should travel free
    assert ticket.calculate_bus_ticket(2, False) == 0
    # Students who are under 19 pay half price, note STUDENTS
    assert ticket.calculate_bus_ticket(18, False) == 4
    assert ticket.calculate_bus_ticket(18, True) == 2
    # People who are aged over 65 and over travel for free
    assert ticket.calculate_bus_ticket(66, False) == 0
    assert ticket.calculate_bus_ticket(68, True) == 0


def test_calculate_speeding_ticket():
    # Test if the user is exceeding by 10mph
    assert  ticket.calculate_speeding_ticket(61, 50) == (True, True)
    # Test if the user is speeding by 10mph or less
    assert ticket.calculate_speeding_ticket(55,50) == (True, False)
    # Test if ticket is issued/court summon if user isnt speeding
    assert ticket.calculate_speeding_ticket(50,50) == (False, False)


def test_calculate_delivery_price():
    # Test if free delivery up to 10 miles and goods > £100
    assert ticket.calculate_delivery_price(10, 200) == 0
    # Test delivery price if up to 10 miles and goods < £100
    assert ticket.calculate_delivery_price(10, 99) == 5
    # Test delivery price for over 10 miles
    assert ticket.calculate_delivery_price(12, 100) == 10
    # Test delivery price for over 20 miles
    assert ticket.calculate_delivery_price(25,100) == 15
    # Test delivery price for over 30 miles
    # £15 post 30miles
    # 50p extra mile past 30 so 36miles should give £22
    assert ticket.calculate_delivery_price(36,100) == 18