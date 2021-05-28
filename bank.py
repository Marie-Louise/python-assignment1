class Bank:
 def __init__(self,Id,Nationality,age):
    self.Id=Id
    self.Nationality=Nationality
    self.age=age

 def behavious(self):
    return f"My bank details are {self.Id},{self.Nationality} and {self.age}" 
 def deposit(self):
    return f"I have deposited 20000 shillings on {self.Id},{self.Nationality} and {self.age}"
