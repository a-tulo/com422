class Carpark:

    @staticmethod
    def check_capacity(self):
        return True if len(self.reg_list) == 15 else False

    def __init__(self):
        self.capacity = 15
        self.reg_list = []
        self.access = True


    def add_car(self, reg):
        if self.check_capacity(self):
            self.access = False
            return f'Car park full. Access = {self.access}'
        else:
            self.reg_list.append(reg)

    def remove_car(self, reg):
        if reg not in self.reg_list:
            return 'Error, car reg not found'
        self.reg_list.remove(reg)
        self.access = True

    def list_cars(self):
        for car in self.reg_list:
            print(car)

    def print_spaces(self):
        spaces_left = self.capacity - len(self.reg_list)
        print(f'Spaces Taken: {len(self.reg_list)}\nSpaces Left: {spaces_left}')
