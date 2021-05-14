class byte:
    def __init__(self, value: int):
        self.value = value
        self.bitnr = 0
        self.val = 0
        self.bitnr1 = 0
        self.bitnr2 = 0

    def set_bit(self, bitnr: int, val: bool):
        if val == True:
            return self.value | (1 << bitnr)
        if val == False:
            return self.value and ~(1 << bitnr)

    def is_set(self, bitnr: int):
        if (self.value and (1 << bitnr)):
            return True
        else:
            return False

    def swap_bit(self, bitnr1, bitnr2):
        pass


ka = byte(199)
#print(ka.is_set(3))
#print("Eingabe:", ka.value)
#print("Eingabe bit:", bin(ka.value)[2:].zfill(8))
#ka.set_bit(7, False)
#print("Ausagabe:", ka.value)
#print("Eingabe bit:", bin(ka.value)[2:].zfill(8))
##print(int(ka.value, 2))
#test


print("HI")