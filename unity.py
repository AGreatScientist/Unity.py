from figures.cube import Cube
from figures.pyramid import Pyramid
from object_3d import *
from camera import *
from projection import *
from asyncio import Event
import pygame as pg

class Unity:
    def __init__(self):
        pg.init()
        self._RES = self._WIDTH, self._HEIGHT = 1600, 900
        self._event: Event = Event()
        self._H_WIDTH, self._H_HEIGHT = self._WIDTH // 2, self._HEIGHT // 2
        self._FPS = 60
        self._screen = pg.display.set_mode(self._RES)
        self._clock = pg.time.Clock()

    def draw_cube(self, x, y, z):
        self._camera = Camera(self, [x, y, z])
        self._projection = Projection(self)
        self._object = Cube(self)

    def draw_pyramid(self, x, y, z):
        self._camera = Camera(self, [x, y, z])
        self._projection = Projection(self)
        self._object = Pyramid(self)

    def draw_file(self, file):
        vertexes, faces = [], []
        if not file.endswith('.obj'):
            print(f'Error: File {file} does not exists.')
            exit()
        else:
            with open(file) as f:
                for line in f:
                    if line.startswith('v '):
                        vertexes.append([float(i) for i in line.split()[1:]] + [1])
                    elif line.startswith('f'):
                        faces_ = line.split()[1:]
                        faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
                return Object3D(self, vertexes, faces)

    def begin(self):
        def is_ready():
            return self._event.is_set()

        def draw():
            font = pg.font.SysFont('Arial', 30, bold=True)
            text = font.render(f'{int(self.clock.get_fps())}', True, pg.Color('white'))
            self._screen.fill(pg.Color('darkslategray'))
            self._screen.blit(text, (self.WIDTH - 100, 50))
            self._object.draw()
        
        while not is_ready():
            draw()
            self._camera.control()
            pg.display.flip()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self._clock.tick(self._FPS)