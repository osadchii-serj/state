from interface import ITrafficLightState

from dataclasses import dataclass


@dataclass
class RedLight(ITrafficLightState):

    def change_light(self):
        print("Переключаюсь на зеленый свет.")
        return GreenLight()


@dataclass
class YellowLight(ITrafficLightState):

    def change_light(self):
        print("Переключаюсь на красный свет.")
        return RedLight()


@dataclass
class GreenLight(ITrafficLightState):

    def change_light(self):
        print("Переключаюсь на желтый свет.")
        return YellowLight()
