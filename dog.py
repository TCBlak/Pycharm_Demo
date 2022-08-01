from pet import Pet


class Dog(Pet):

    def __init__(self, color='Brown', breed='Beagle', weight=32.6, name='Reilly'):
        super().__init__(name, color, breed)
        self.__weight = weight

    def __bark(self):
        print('Woof, woof')

    def __fetch(self, other):
        print(f'I got the {other}')

    def make_noise(self):
        self.__bark()

    def do_yo_thang(self, **kwargs):
        if 'item' in kwargs.keys():
            self.__fetch(kwargs['item'])
        else:
            print('Huh??')

    def __str__(self):
        return f'{self.name} a {self.color} {self.breed} that weighs {self.__weight} pounds'

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False

        if (self.color == other.color and
                self.breed == other.breed):
            return True
        else:
            return False

    def __add__(self, other):
        if not isinstance(other, Dog):
            raise AttributeError
        new_weight = self.__weight + other.__weight
        return Dog(self.color, self.breed, new_weight)
