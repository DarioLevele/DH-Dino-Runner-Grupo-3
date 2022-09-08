from dino_runner.components.obstacles.osbtacle import Obstacle
from dino_runner.utils.constants import BIRD

import random

class Birds(Obstacle):
    step_index = 0
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 150

class Birds_down(Obstacle):
    step_index = 0
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 270

    
    