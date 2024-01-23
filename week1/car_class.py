class Car:

    def __init__(self, currentSpeed, maxSpeed, fuelLevel, weight, make):
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel
        self.weight = weight
        self.make = make

    def accelerate(self, multiplier):
        if self.fuelLevel != 0:
            self.currentSpeed += (3 * multiplier)
            self.fuelLevel -= (1.5 * multiplier)
            if self.currentSpeed > self.maxSpeed: self.currentSpeed = self.maxSpeed
        else:
            self.currentSpeed = 0
            print('Out of fuel, cannot accelerate!')

    def brake(self, multiplier):
        self.currentSpeed -= (3 * multiplier)
        if self.currentSpeed < 0: self.currentSpeed = 0

    def refuel(self, amount):
        self.fuelLevel += amount
        if self.fuelLevel > 100: self.fuelLevel = 100

