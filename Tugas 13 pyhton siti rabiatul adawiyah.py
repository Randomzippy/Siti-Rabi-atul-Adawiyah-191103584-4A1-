#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Inheritance
class person: 
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def name(self):
        return self.firstname + " " + self.lastname
    
class employee(person):
    def __init__(self, first, last, staffnum):
        person.__init__(self, first, last)
        self.staffnumber = staffnum
        
    def getemployee(self):
        return self.name() + ", " + self.staffnumber
    
x = person("marge", "simpsone")
y = employee("homer", "simpson", "1007")

print(x.name())
print(y.getemployee())


# In[4]:


#Encapsulation
class car:
    
    __maxspeed = 0
    __name =""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
        
    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))
        
    def setmaxspeed(self, speed):
        self.__maxspeed = speed
        
redcar = car()
redcar.drive()
redcar.setmaxspeed(320)
redcar.drive()


# In[6]:


#Polymorphism
class shark:
    def swim(self):
        print("Hiu sedang berenang.")
        
    def swim_backwards(self):
        print("Hiu tidak bisa berenang mundur, tetapi bisa tenggelam ke belakang.")
        
    def skeleton(self):
        print("Kerangka hiu terbuat dari tulang rawan.")
        
class clownfish():
    def swim(self):
        print("Ikan badut sedang berenang.")
    def swim_backwards(self):
        print("Ikan badut tidak bisa berenang mundur.")
        
    def skeleton(self):
        print("Kerangka ikan badut itu terbuat dari tulang.")
        
sammy = shark()
sammy.skeleton()

casey = clownfish()
casey.skeleton

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton


# In[5]:


class Polygon: 
    def _init_(self, jumlah_sisi): 
        self.n = no_of_sides 
        self.sides = [0 for i in range(jumlah_sisi)] 
        
    def inputSides(self):
        self.sides = [float(input("Masukkan sisi "+str(i+1)+" : ")) for i in range(self.n)] 
    
    def dispSides(self): 
        for i in range(self.n): 
            print("sisi",i+1,"adalah",self.sides[i]) 
        
class Triangle(Polygon): 
    def _init_(self): 
        Polygon._init_(self,3) 

    def findArea(self): 
        a, b, c = self.sides 
        # Hitung KeLiLing 
        s = (a + b + c) / 2 
        area = (s*(s-a)(s-b)(s-c)) ** 0.5 
        print('Luas Segitiga adalah %0.2f' %area) 
    
t = Triangle() 
t.inputSides()
t.findArea()


# In[ ]:




