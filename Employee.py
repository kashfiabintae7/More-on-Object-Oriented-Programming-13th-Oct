class Employee:
    
    
    def __init__(self):
        print("Employee Created.")
        
        
    def __del__(self):
        print("Destructor Called.")
        
def Create_obj():
    print("Making an object....")
    objfunc = Employee()
    print("Function end....")
    return objfunc


print("Calling Create_obj() function....")
obj = Create_obj()
print("Program End....")