class TeaException(Exception):
    def __init__(self, arg):
        self.mgs = arg
        
class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature
        
    def drink_tea(self):
        if self.__temperature > 85:
            #print("Hot to drink.")
            raise TeaException("Tea to hot to drink")
        elif self.__temperature < 65:
            print("Cold to drink.")
            raise TeaException("Tea to cold to drink")
        else:
            print('Tea OK to Drink')

cup = Tea(int(input("temp of tea: ")))
cup.drink_tea()
