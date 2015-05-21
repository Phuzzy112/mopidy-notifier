from __future__ import unicode_literals

import subprocess
import pykka
import sys

from mopidy.core import CoreListener


class NotifierFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(NotifierFrontend, self).__init__()
        self.config = config
        self.core = core

    def notify(self, message, subtitle):
        if sys.platform.startswith('darwin'):
            call = ['terminal-notifier', '-title', 'Mopidy', '-subtitle', subtitle, '-message', message, '-group', 'mopidy']
        elif sys.platform.startswith('linux'):
            call = ['notify-send', 'Mopidy', message, '--icon=multimedia-player']
        else:
            # Unsupported system
            raise EnvironmentError((1, "This operating system is not supported."))
        subprocess.call(call)

    def on_start(self):
        self.notify('Starting...','')

    def on_stop(self):
        self.notify('Shutting down...','')

    def track_playback_started(self, tl_track):
        track = tl_track.track
        song = track.name
        artists = ', '.join([a.name for a in track.artists])
        if track.album:
            album = track.album.name
        else:
            album = ''
        if sys.platform.startswith('darwin'):
            subtitle = artists + ' - ' + album
            message = song
        elif sys.platform.startswith('linux'):
            subtitle = ''
            message = song + '\\n' + artists + ' - ' + album
        else:
            # Unsupported system
            raise EnvironmentError((1, "This operating system is not supported."))
        self.notify(message, subtitle)
