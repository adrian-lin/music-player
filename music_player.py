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
    elif symbol == key.U:
        player.pause()
    
    display_current_song()

def display_current_song():
    song_label = pyglet.text.Label('Playing: ' + player.source.title + '\n' + 'Play: P, Pause: U, Next: N',
                        font_name = 'Calibri',
                 	font_size = 14,
			x = window.width // 2, y = window.height // 2,
			width = 550,
			anchor_x = 'center', anchor_y = 'center',
			multiline = True)

    window.clear()
    song_label.draw() 

def add_songs_to_player():
    for song in os.listdir(SONGS_PATH):
        if song.endswith('.ogg'):
            print song
            songsource = pyglet.media.load(SONGS_PATH + song)
	    songsource.title = song[0:-4]
	    #print songsource.title
            player.queue(songsource)

add_songs_to_player()

pyglet.app.run()
