### Inhertance -> bir clasdan bowqa class olish bu inhertance deb ataladi 

# Super class -> ota class
# Sup class -> bola class 

class Animals:  #-> Super classs
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
        
    def run(self):
        print(f"{self.name}- is running.")
            
class Cat(Animals):   #-> bolla classs
    
    # Polymorphism ->  ota clasdagi metodni bola class qayta yozishi polymorphism va overriding deyiladi
    
    def run(self):
        pass
    
    def meow(self):
        print(f"{self.name} weoww")
        
        
class Dog(Animals): #-> bolla classs
    def wof(self):
        print(f"{self.name} wof-wof")
        
     
an = Dog("petbull",12)
cat = Cat("mishka",45)

an.run()
an.wof()

cat.run()
cat.meow()


        
    