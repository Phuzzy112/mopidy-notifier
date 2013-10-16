#mopidy-terminal-notifier
===
[![Downloads](https://pypip.in/v/PYPI_PKG_NAME/badge.png)](https://crate.io/package/PYPI_PGK_NAME)
[![Downloads](https://pypip.in/d/PYPI_PKG_NAME/badge.png)](https://crate.io/package/PYPI_PGK_NAME)

[Mopidy](http://www.mopidy.com "http://www.mopidy.com") extension for displaying the Trackinfo (Song, Artist and Album) in the Notification Center of Mac OS X 10.8 and higher. It uses the command-line tool [terminal-notifier](https://github.com/alloy/terminal-notifier "https://github.com/alloy/terminal-notifier").

##Installation
First install [terminal-notifier](https://github.com/alloy/terminal-notifier "https://github.com/alloy/terminal-notifier") via Homebrew, or see the page for other ways.
    
    $ brew install terminal-notifier
    
Install mopidy-terminal-notifier by running:

    $ pip install mopidy-terminal-notifier

##Configuration

Before starting Mopidy, you must add configuration for
mopidy-terminal-notifier to your Mopidy configuration file:

    [notifier]
    enable = ture