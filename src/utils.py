def add(a,b):
    try:
        print(a+b)
    except ValueError:
        print("Invalid number")
    
def subtract(a,b):
    try:
        print(a-b)
    except ValueError:
        print("Invalid number")
    
def multiply(a,b):
    try: 
        print(a*b)
    except ValueError:
        print("Invalid number")