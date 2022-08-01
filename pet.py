from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name, color, breed):
        self.__name = name
        self.__color = color
        self.__breed = breed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @property
    def breed(self):
        return self.__breed

    @abstractmethod
    def make_noise(self):
        pass

    @abstractmethod
    def do_yo_thang(self, **kwargs):
        pass