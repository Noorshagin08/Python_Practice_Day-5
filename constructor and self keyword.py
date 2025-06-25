#constructor- when object is created ,it call class automatically
# self keyword-used to refer object
# class laptop:
#     def __init__(self):   #self=hp
#         print("demo")
#     def display(self):
#         print("display")

# hp=laptop()   #object created
# hp.display()     

# to initialize or assign value to data member of that class

class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)  
         
hp=laptop()
dell=laptop() 

hp.ram="8gb" 
hp.processor="i5"


dell.ram="6gb"
dell.processor="i7"

hp.display()
dell.display()

