
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model =model
        self.year = year
        self.odometr = 0

    def car_description(self):
        print(f"Car info:{self.make},{self.model}, {self.year}")  

    def read_odometr(self):
        print(f"your odometr shows: {self.odometr}")

    def set_odometr(self, miles):
        if miles > self.odometr:
            self.odometr = miles
        else:
            print(f"You can not set the odometr of less of {self.odometr}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery =75):
        super().__init__(make, model, year)
        self.battery = battery

    def car_description(self):
         msg = f"Car info:{self.make}, {self.model}, {self.year}, \n"
         msg +=f"battery capacity: {self.battery} -kWh." 
         print(msg)
    
    def get_range(self): 
        if self.battery > 100:
            msg = "This car has range of 320 miles fully charged battery."
        elif self.battery <80:
            msg = f"This ca has range of 250 miles with full charge."
        else:
            msg = f"THis car has range of around 290 miles with full charge."    
        print(msg)                    
