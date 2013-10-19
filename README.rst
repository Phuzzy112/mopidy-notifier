****************************
mopidy-notifier
****************************

.. image:: https://pypip.in/v/mopidy-notifier/badge.png
    :target: https://crate.io/packages/mopidy-notifier/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/mopidy-notifier/badge.png
    :target: https://crate.io/packages/mopidy-notifier/
    :alt: Number of PyPI downloads

.. _Mopidy: http://www.mopidy.com extension for displaying the Trackinfo (Song, Artist and Album) in the Notification Center of Mac OS X 10.8 and higher.
It uses the command-line tool .. _terminal-notifier: https://github.com/alloy/terminal-notifier .


Installation
============

First install terminal-notifier_ via Homebrew:

    $ brew install terminal-notifier

Install mopidy-notifier by running:

    $ pip install mopidy-notifier


Configuration
=============

Before starting Mopidy, you must add configuration for
mopidy-terminal-notifier to your Mopidy configuration file:

    [notifier]
    enable = ture