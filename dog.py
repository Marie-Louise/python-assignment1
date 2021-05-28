class Dog:
 origin="Africa"
 def __init__(self,size,name,color):
        self.size=size
        self.name=name
        self.color=color

 def move(self):
    return f"My dog is small in {self.size} called {self.name} and is {self.color}." 