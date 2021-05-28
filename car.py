class Car:
 car="prado"
 def __init__(self,made,register,color,mileage):
    self.made=made
    self.register=register
    self.color=color
    self.mileage=mileage

 def doings(self):
    return f"This car is made in {self.made} year of {self.register} is {self.color} have nice {self.mileage}"
 def acceleration(self):
     return f"this car has 20 in {self.made} year of {self.register} is {self.color} have nice {self.mileage} "