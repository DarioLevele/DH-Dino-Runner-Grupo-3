from dino_runner.components.obstacles.osbtacle import Obstacle
from dino_runner.utils.constants import BIRD

import random

class Birds(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 150
    
    def aleteo(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.dino_rect = self.image.get_rect()
        self.step_index += 1