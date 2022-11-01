from turtle import left


class Car ():
    brand=''
    fuel_tank=0
    speed=0
    model=''
    color=''
    number_of_wheels= 0
    engine_size=0
    mileage=0

    def __init__(self,brand,model):
       self.brand=brand
       self.model=model

    #def method name()
#self is a keyword that helps you access the instance of the class
    def current_speed(self):
        print(f'Current_speed is {self.speed}')
    
    def navigation (self,direction):
     print(f"Turn {direction}")

car=Car()
car.brand= 'Tesla'
car.model= 'Model 5'
car.engine_size=396
car.number_of_wheels=4
car.mileage=0
car.speed=200
car.color='Wine Red'

print(f"Mary's car model: {car.model}")
car.current_speed()
car.navigation("left")
car.navigation(second_direction="left",direction="right")
