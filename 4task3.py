class Car:
    def __init__(self, make, model, year):
        self.adometer = 0
        self.fuel = 70

    
    def drive(self, km):
        if km < (self.fuel * 10):
            print("let's drive")
            self.__add_distance(km)
            self.__subtract_fuel(km)

        else:
            print("Need more fuel")

    def __add_distance(self, km):
        self.odometer = self.adometer + km
    

    def __subtract_fuel(self, km):
        self.fuel = self.fuel - km / 10



car1 = Car('Subaru', 'Impreze', '2004')
print(car1.fuel)
car1.drive()
print(car1.fuel)


