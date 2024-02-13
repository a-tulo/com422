
class BookingInformation:
    def __init__(self, name, number_of_guests, is_outside):
        self.name = name
        self.number_of_guests = number_of_guests
        self.is_outside = is_outside
class Restaurant(BookingInformation):

    def __init__(self, name, number_of_guests, is_outside):
        super().__init__(name, number_of_guests, is_outside)

        self.tables = {
            'table_number': [],
            'assigned_booking': [],
            'num_of_seats': [],
            'is_inside': []
        }

    def add_table(self, table_num, assigned_booking, num_of_seats, is_inside):
        self.tables['table_number'].append(table_num)
        self.tables['assigned_booking'].append(assigned_booking)
        self.tables['num_of_seats'].append(num_of_seats)
        self.tables['is_inside'].append(is_inside)
        print(self.tables['table_number'])
    def book_table(self, bookingInformation):
        pass


if __name__ == '__main__':
    table = Restaurant('John Doe', 5, False)
    table.add_table(1,'',30,True)
    table.add_table(2,'',3,False)