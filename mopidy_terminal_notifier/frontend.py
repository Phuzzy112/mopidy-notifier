from __future__ import unicode_literals

import os

import pykka

from mopidy.core import CoreListener


class TerminalNotifierFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(TerminalNotifierFrontend, self).__init__()
        self.config = config
        self.core = core

    def on_start(self):
        command = 'terminal-notifier -title mopidy \
                                     -message Upandrunning \
                                     -group mopidy'
        os.system(command)

    def track_playback_started(self, tl_track):
        track = tl_track.track
        song = 'test'
        artists = 'test'
        album = 'test'
        command = 'terminal-notifier -title mopidy \
                                     -subtitle {} \
                                     -message {}\ -\ {} \
                                     -group mopidy'.format(song, artists, album)
        os.system(command)
