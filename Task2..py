class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying = False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying

    def take_off(self):
        self.is_flying = True

 
    def fly(self, distance):
        self.odometer += distance
        print('The new value of odometer is ' + str(self.odometer))

    def land(self):
        self.is_flying = False

new_Airplane = Airplane('Airbus', 900, 2000, 890, 0)
new_Airplane.fly(1700)