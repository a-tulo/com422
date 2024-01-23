import car_class


def make_car():
    # self, currentSpeed, maxSpeed, fuelLevel, weight, make
    currentSpeed = int(input('Current speed = '))
    maxSpeed = int(input('Max Speed = '))
    fuelLevel = input('Fuel Level = ')
    weight = int(input('Weight = '))
    make = input('Make = ')
    return car_class.Car(currentSpeed, maxSpeed, fuelLevel, weight, make)

def print_attributes(car):
    print(f'''
Current Speed = {car.currentSpeed}mph
Max Speed = {car.maxSpeed}mph
Fuel Level = {car.fuelLevel}%
Weight = {car.weight}kg
Make = {car.make}\n''')

if __name__ == '__main__':

    if input('Want to manually input car data? [Y/N]\n').upper() == 'Y':
        car_a = make_car()
        car_b = make_car()
    else:
        car_a = car_class.Car(30, 150, 70, 1300, 'BMW')
        car_b = car_class.Car(70, 200, 30, 1500, 'AUDI')

    print_attributes(car_a)
    print(f'The Car accelerates..')
    car_a.accelerate(10)
    print(f'Speed: \n{(car_a.currentSpeed)}mph\nFuel level: {car_a.fuelLevel}%')
    print(f'The driver puts his foot on the brake')
    car_a.brake(5)
    print(f'Speed: \n{(car_a.currentSpeed)}mph\nFuel level: {car_a.fuelLevel}%')
    print(f'Running low on fuel...\nLets refuel!\nCurrent fuel level: {car_a.fuelLevel}%')
    car_a.refuel(20)
    print(f'New fuel level: {car_a.fuelLevel}%')
