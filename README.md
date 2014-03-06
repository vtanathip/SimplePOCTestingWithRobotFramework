## Required package ##
1. Python 2.7.6 [Download link](http://www.python.org/ftp/python/2.7.6/python-2.7.6.msi)
1. wxPython 2.8.12.1 [Download link](http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/wxPython2.8-win32-unicode-2.8.12.1-py27.exe/download)
1. Robot Framework 2.8.3 [Download link](https://pypi.python.org/packages/any/r/robotframework/robotframework-2.8.4.win32.exe#md5=538a3fcd2b1f222b978b2f1cf2ae93ca)
1. PIP 1.5.4 Installer [Download link](http://www.lfd.uci.edu/~gohlke/pythonlibs/xyaoaydo/pip-1.5.4.win32-py2.7.exe)
1. Robot Framework IDE 1.2.3 [Download link](https://robotframework-ride.googlecode.com/files/robotframework-ride-1.2.3.win32.exe)

## Installation Step ##

1. First install python from download link and set system variables path `PYTHON_HOME` value is `[python path]` then set to path system variables
1. in system variables path add this `;%PYTHON_HOME%\Scripts;` too (this step telling window to find all scripts in here ex. robot framework)
1. install wxPython from .exe file
1. install Robot Framework from .exe file
1. install PIP installer .exe file
2. install Robot Framework IDE .exe file
1. in command line `pip install robotframework-selenium2library`


## How to run this test ##

if you follow instruction use this

`pybot Kapook_check_lotto.txt`

and wait for magic things.
