class byte:
    def __init__(self, value: int):
        self.value = bin(value)[2:].zfill(8)
        self.bitnr = 0
        self.val = 0
        self.bitnr1 = 0
        self.bitnr2 = 0

    def set_bit(self, bitnr: int, val: bool):
        if val == True:
            self.value = "1" + self.value[bitnr:]
        if val == False:
            self.value = "0" + self.value[bitnr:]

    def is_set(bitnr: int):
        pass

    def swap_bit(self, bitnr1, bitnr2):
        pass


ka = byte(243)
print(ka.value)

ka.set_bit(1, False)
print(ka.value)

print(int(ka.value, 2))
