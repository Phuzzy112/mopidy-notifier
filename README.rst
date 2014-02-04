***************
Mopidy-Notifier
***************

.. image:: https://pypip.in/v/Mopidy-Notifier/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-Notifier/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/Mopidy-Notifier/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-Notifier/
    :alt: Number of PyPI downloads


`Mopidy <http://www.mopidy.com>`_ extension for displaying the Trackinfo (Song,
Artist and Album) in the Notification Center of Mac OS X 10.8 and higher.  It
uses the command-line tool `terminal-notifier
<https://github.com/alloy/terminal-notifier>`_ .


Installation
============

First install `terminal-notifier <https://github.com/alloy/terminal-notifier>`_
via Homebrew::

    brew install terminal-notifier

Then install mopidy-notifier by running::

    pip install mopidy-notifier

Now you should be all set up!


Configuration
=============

No configuration is needed. The extension is enabled by default when it is
installed. To disable it, add the following to your Mopidy config file::

    [notifier]
    enabled = false


Project resources
=================

- `Source code <https://github.com/sauberfred/mopidy-notifier>`_
- `Issue tracker <https://github.com/sauberfred/mopidy-notifier/issues>`_
- `Download development snapshot <https://github.com/sauberfred/mopidy-notifier/tarball/master#egg=Mopidy-Notifier-dev>`_


Changelog
=========

v0.3.0 (2014-02-04)
-------------------

- Require Mopidy >= 0.18.


v0.2.0 (2013-10-20)
-------------------

- Initial release.
