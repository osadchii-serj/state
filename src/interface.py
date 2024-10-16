from abc import ABC, abstractmethod


class ITrafficLightState(ABC):

    @abstractmethod
    def change_light(self):
        raise NotImplementedError()
