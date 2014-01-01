## Simple testing with robot framework ##

**Test write in gherkin style** and completely fine with Windows 7.

Simple create test suite and keywords for check lotto in website `kapook.com` and also create own library for any purpose.

`FYI: this is prove of concept project`

###Required package ###

1. Python 2.7.3 [Download link](http://www.python.org/getit/)
2. wxPython 2.8.12.1  [Download link](http://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/)
3. Robot Framework 2.8.3  [Download link](http://robotframework.org/)

another version of this is fine but in this project it following this

### Shoulda this stuffs ###

- Python packages ( pip )

but you must install ez_setup for install pip so download this file [Download link](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py) and run with this command

`python ez_setup.py install`

then follow this 

1. `pip install robotframework`
2. `pip install robotframework-selenium2library`
3. `pip install robotframework-ride` or using installer from this [Download link](https://code.google.com/p/robotframework-ride/downloads/list)

### How to run this test ###

if you follow instruction use this

`pybot Kapook_check_lotto.txt`

and wait for magic things.
