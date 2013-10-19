from __future__ import unicode_literals

import subprocess
import pykka

from mopidy.core import CoreListener


class NotifierFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(NotifierFrontend, self).__init__()
        self.config = config
        self.core = core

    def on_start(self):
        subprocess.call(['terminal-notifier', '-title', 'Mopidy', '-message', 'Starting...', '-group', 'mopidy'])

    def track_playback_started(self, tl_track):
        track = tl_track.track
        song = track.name
        artists = ', '.join([a.name for a in track.artists])
        album = track.album.name
        message = artists + ' - ' + album
        subprocess.call(['terminal-notifier', '-title', song, '-message', message, '-group', 'mopidy'])