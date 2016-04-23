#!/usr/bin/env python

import os
import pyglet
from pyglet.window import key

pyglet.lib.load_library('avbin')
pyglet.have_avbin = True

SONGS_PATH = os.getcwd() + '\songs\\'

window = pyglet.window.Window()

player = pyglet.media.Player()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.P:
        player.play()
    elif symbol == key.N:
        player.next_source()    

for song in os.listdir(SONGS_PATH):
    if song.endswith('.ogg'):
        print song
        source = pyglet.media.load(SONGS_PATH + song)
        player.queue(source)

#player.play()

pyglet.app.run()
