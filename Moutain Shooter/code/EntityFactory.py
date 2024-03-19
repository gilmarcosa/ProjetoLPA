#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Const import WIN_WIDTH, WIN_HEIGHT
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1':
                return Player('player1',(10, WIN_HEIGHT / 2 - 30))
            case 'player2':
                return Player('player2', (10, WIN_HEIGHT / 2 + 30))
            case 'enemy1':
                return Enemy('enemy1', (WIN_WIDTH + 10, random.randint(0+40, WIN_HEIGHT)))
            case 'enemy2':
                return Enemy('enemy2', (WIN_WIDTH + 10, random.randint(0+40, WIN_HEIGHT)))
