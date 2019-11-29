# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

class Car:
    def __init__(self, make, model, year, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel
        self.odometr = 0
        self.fuel = 70

    def drive(self):
        if self.odometr = 0
            self.drive = True


        drive.distance km 1 litr per 10 km
        
        

        "Let's drive!"
        "Need more fuel, please, fill more"


def fly(self):
        if self.odometr > 0:
            self.is_flying = True
            print('')
        else:
            self.odometr = 0
            self.is_flying = False
            print('')


__add_distance 

__subtract_fuel