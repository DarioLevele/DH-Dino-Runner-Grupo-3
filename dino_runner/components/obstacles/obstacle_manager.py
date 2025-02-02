import random
from turtle import Screen
import pygame

from dino_runner.components.obstacles.cactus_large import LargeCactus
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Birds, Birds_down
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles= []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.type = random.randint(0, 3)
            if self.type == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.type == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif  self.type == 2:
                self.obstacles.append(Birds(BIRD))
            else:
                self.obstacles.append(Birds_down(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []