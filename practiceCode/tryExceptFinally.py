result = None
x = int(input("Number 1: "))
y = int(input("Number 2: "))
try: 
    result = x/y 
except Exception as e:
    print("I try so hard I got so far but in the end it does really matter:",e)
else : 
    print("inside else")
finally:
    print("Inside finally")
    print("--- New line ---")
print("result = ", result)
