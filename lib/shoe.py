class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("shoe size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("These shoes are New!")
        self.condition = "New"

