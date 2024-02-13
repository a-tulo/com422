def calculate_bus_ticket(age, is_student):
    bus_price = 4
    if age <= 19 and is_student:
        return bus_price/2
    elif age <= 3 or age >= 65:
        return 0
    else:
        return bus_price

def calculate_speeding_ticket(speed, speed_limit):
    speed_differential = abs(speed-speed_limit)
    if speed > speed_limit and speed_differential > 10:
        return True, True
    elif speed > speed_limit:
        return True, False
    else:
        return  False, False

def calculate_delivery_price(distance,goods_value):
    if distance <= 10 and goods_value >= 100:
        return 0
    elif distance <= 10 and goods_value < 100:
        return 5
    elif distance >= 30:
        return 15 + (0.5 * (distance - 30))
    elif distance > 10 and distance <= 20:
        return 10
    elif distance > 20 and distance <= 30:
        return 15



