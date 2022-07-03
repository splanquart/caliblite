# Caliblite

Caliblite is a simple application to control calibration lamp for Star'Ex projet and other Spectroscopy projet.

In fact it communcate with relay board with CH340 chip who convert USB signal to Serial.

## Installation

In console

```
pip install -r requirements.txt
```

## Run

```
python ./src/caliblite.py
```

## Troubleshots

### tk-inter not found

If when you run caliblite you take this error:

```
Traceback (most recent call last):
  File "/Users/steph/Documents/caliblite/./src/caliblite.py", line 1, in <module>
    import PySimpleGUI as sg
  File "/Users/steph/Envs/caliblite/lib/python3.9/site-packages/PySimpleGUI/__init__.py", line 2, in <module>
    from .PySimpleGUI import *
  File "/Users/steph/Envs/caliblite/lib/python3.9/site-packages/PySimpleGUI/PySimpleGUI.py", line 130, in <module>
    import tkinter as tk
  File "/usr/local/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 37, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter'
```

It because your system don't have tkinter already install.
You need to install `python-tk`.

On MacOsx you can do it by :

```
brew install python-tk
```
On Windows, I never experimente this bug

On Linux you can do it by :

```
apt install python-tk
```
