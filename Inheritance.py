from re import X


class Car:
    brand=''
    model=''
    year=0
    speed=0
    mileage=0

    def __init__(self,brand:str,year:int,model:str):
        self.brand=brand
        self.year=year
        self.model=model

class ElectricCar(Car):
    battery_capacity=0
    def __init__(self,brand:str,model:str,year:int,battery_capacity:int):
        super().__init__(brand, model, year)


class CEngineCar(Car):
    engine_capacity=0

car=Car()
car.year=2020

electric_car=ElectricCar("Tesla","Model y",2020.2000)
electric_car.battery_capacity=2000

c_engine_car=CEngineCar()
c_engine_car.brand="Toyota"

print(f"CEngine car brand: {c_engine_car.brand}")

class Toyota(CEngineCar):
    pass
