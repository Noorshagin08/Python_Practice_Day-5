# 1) create a class called student , create a variable name , register number using constructor.
#create a function called display which would display the name and register number of student

class student:
    def __init__(self):
        self.name="Ravi"
        self.register_number="9115"
    def display(self):
        print("Name:",self.name)
        print("Register no:",self.register_number) 

s=student()


s.display()

# 2)create a class called fruit using __init__ method,create a object called apple 
  # "pass the colour variable as a parameter through object "
  
class fruit:
    def __init__(self,col): #self=apple
        self.colour=col
        

apple=fruit("red")  # fruit(apple,red)
print(apple.colour)

# 3)create a class called teacher ,create a variable name,register no using constructor 
# create a function called display which should display name and register no of student 
# create t1,t2 object and pass the name and reg no value through object

class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.register_number=reg
    def display(self):
        print("Name:",self.name)
        print("Register no:",self.register_number) 

t1=teacher("raja","1")
t2=teacher("rani","2")


t1.display()
t2.display()

#4) create a class called calculator ,create 2 variable a and b , create a function called add,sub,mul,div 
#function should take 2 variable as parameter ,pass the a and b value through object()

class calculator:
    def add(self,a,b):
        print("add",a+b)
    def sub(self,a,b):
        print("sub",a-b)
    def mul(self,a,b):
        print("mul",a*b)
    def div(self,a,b):
        print("div",a/b)            


o1=calculator()


o1.add(10,2)
o1.sub(20,10)
o1.mul(20,2)
o1.div(200,10)

