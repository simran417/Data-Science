class car:
    total_car=0
    def __init__(self,brand,model):
        # self.brand=brand
        # to make private datamembers:
        self.__brand=brand
        self.__model=model
        car.total_car +=1

    # to access private member we use getter method:
    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.brand} {self.model}"

    # polymorphism:
    def fuel_type(self):
        return "petrol"
    
    # static method:
    @staticmethod
    def car_des():
        return "car is good"

    # property decorator:
    @property
    def model(self):
        return self.__model

    
# inheritance:
class Ecar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(model,brand)
        self.battery_size=battery_size

    def fuel_type(self):
        return "electric charge"

c1=car("toyota","corolla")
# print(c1.brand)
# print(c1.full_name())
# print(c1.fuel_type())
c2=Ecar("a","b",5)
# print(c2.battery_size)
# print(c2.model)
# print(c2.fuel_type())
# print(c2.brand)
# print(c1.get_brand())
# print(car.total_car)
# print(car.car_des())
# c1.model="abc"
# print(c1.model)
# to check instance of which class:
# print(isinstance(c1,car))

class battery:
    def Binfo(self):
        return "battery"

class engine:
    def Einfo(self):
        return "engine"

class EcarT(battery, engine, car):
    pass

c3=EcarT("a", "b")
print(c3.Einfo())

