"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo:int = 13489
    max_cargo:int = 21000
    
    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo:int) -> None:
        self.__init_cargo = self.cargo
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, weigth: int):
        if (self.cargo + weigth) > self.max_cargo:
            raise CargoOverload
        self.cargo = self.cargo + weigth
    
    def remove_all_cargo(self):
        self.cargo = self.__init_cargo
