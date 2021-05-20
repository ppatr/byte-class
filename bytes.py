class byte:
    def __init__(self, value: int):
        self.value = value

    def set_bit(self, bitnr: int, val: bool):
        if val == True:
            return self.value | (1 << bitnr)
        if val == False:
            return self.value & ~(1 << bitnr)

    def is_set(self, bitnr: int):
        if (self.value & (1 << bitnr)):
            return True
        else:
            return False

    def swap_bit(self, bitnr1, bitnr2): 
        #Quelle : https://www.geeksforgeeks.org/swap-bits-in-a-given-number/
        set1 = (self.value >> bitnr1) & ((1 << 1) -1)
        set2 = (self.value >> bitnr2) & ((1 << 1) -1)
        mask = (set1 ^ set2)
        mask = (mask << bitnr1) | (mask << bitnr2)
        result = self.value ^ mask 
        return result 


ka = byte(199)

print(bin(199))
print(bin(ka.swap_bit(4,1)))
#print(ka.is_set(3))
#print("Eingabe:", ka.value)
#print("Eingabe bit:", bin(ka.value)[2:].zfill(8))
#ka.set_bit(7, False)
#print("Ausagabe:", ka.value)
#print("Eingabe bit:", bin(ka.value)[2:].zfill(8))
##print(int(ka.value, 2))