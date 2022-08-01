from pet import Pet


class Cat(Pet):

    def __init__(self, color='White', breed='Calico', hairball_freq=3, name='Garfield'):
        super().__init__(name, color, breed)
        self.__hairball_freq = hairball_freq

    def __meow(self):
        print('Meow, meow')

    def __pur(self):
        print(f'{self.name} goes PUURRRRRRRRR!')

    def chase(self):
        print(f'{self.name} chases the red light. What a dumbie!')

    def make_noise(self):
        self.__meow()

    def do_yo_thang(self, **kwargs):
        self.__pur()

    def __str__(self):
        return f'{self.name} a {self.color} {self.breed} that has {self.__hairball_freq} hairballs'

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return False

        if (self.color == other.color and
                self.breed == other.breed):
            return True
        else:
            return False

    def __add__(self, other):
        if not isinstance(other, Cat):
            raise AttributeError
        new_hairball_freq = self.__hairball_freq + other.__hairball_freq
        return Cat(self.color, self.breed, new_hairball_freq)
