from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started: bool = False
    weight: int = 910
    fuel: int = 30
    #? непонятно... расход каких-то условных единицах вычисляется...
    fuel_consumption: int = 5

    def __init__(self, weight: int, fuel: int, fuel_consumption: int) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """
        Если ещё не состояние started, проверяет, что топлива больше нуля,
        и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: float):
        """
        Проверяет, что достаточно топлива для преодоления переданной дистанции,
        и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel
        """
        wasted_fuel = distance * self.fuel_consumption
        if self.fuel - wasted_fuel < 0:
            raise NotEnoughFuel
        self.fuel -= wasted_fuel
        return True
