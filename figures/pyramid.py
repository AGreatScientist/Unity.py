from matrix_functions import *
import pygame as pg
from object_3d import Object3D

class Pyramid(Object3D):
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 0, 1, 1), (1, 0, 1, 1), (1, 1, 1, 2)])

        self.faces = np.array([(0, 1, 2, 3), (3, 0, 1, 3), (0, 4, 2, 2), (0, 3, 4, 1)])

        self.translate([0.0001, 0.0001, 0.0001])
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.movement_flag, self.draw_vertexes = True, True
        self.label = ''
    
    def draw(self):
        return super().draw()

    def movement(self, move=True):
        if move:
            return super().movement()

    def rotate_x(self, angle):
        return super().rotate_x(angle)

    def rotate_y(self, angle):
        return super().rotate_y(angle)

    def rotate_z(self, angle):
        return super().rotate_z(angle)

    def scale(self, scale_to):
        return super().scale(scale_to)

    def translate(self, pos):
        return super().translate(pos)
