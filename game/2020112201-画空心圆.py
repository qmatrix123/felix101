import pgzrun
from pgzero.screen import Screen

screen: Screen


def draw():
    screen.draw.circle((400, 300), 100, 'white')


pgzrun.go()
