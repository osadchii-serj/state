from dataclasses import dataclass

from states import RedLight


@dataclass
class TrafficLight:

    state = RedLight()

    def change_light(self):
        self.state = self.state.change_light()
