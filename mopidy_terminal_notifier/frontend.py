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
        command = 'terminal-notifier -title Mopidy \
                                     -message Starting... \
                                     -group mopidy'
        os.system(command)

    def track_playback_started(self, tl_track):
        track = tl_track.track
        song = track.name
        artists = ', '.join([a.name for a in track.artists])
        album = track.album.name
        command = 'terminal-notifier -title {} \
                                     -message {}\ -\ {} \
                                     -group mopidy'.format(song, artists, album)
        os.system(command)
