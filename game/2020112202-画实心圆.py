import pgzrun
from pgzero.screen import Screen

screen: Screen


def draw():
    screen.draw.filled_circle((400, 300), 100, 'white')


pgzrun.go()
