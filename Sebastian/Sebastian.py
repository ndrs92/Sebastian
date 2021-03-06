#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Sebastian is a configurable Butler meant to be sitting next to the door informing users what is inside. """

"""
Copyright (C) 2016  Andrés Vieira Vázquez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Andrés Vieira"
__copyright__ = "Copyright 2016, Andrés Vieira"
__credits__ = ["Andrés Vieira", "Samuel Rodríguez Borines"]
__license__ = "GNU GPLv3"
__version__ = "v0.1 BETA"
__maintainer__ = "Andrés Vieira"
__email__ = "anvieiravazquez@gmail.com"
__status__ = "Development"

import sys
import os
from os.path import expanduser
from PySide import QtGui, QtCore, QtWebKit

_defaultfiletowatch_ = "./default_watch_file.txt"
_currentfiletowatch_ = ""
_debug_active_ = False
_preferences_file_ = expanduser("~") + "/.sebastian.conf"
_app_ = QtGui.QApplication(sys.argv)



def dprint(string):
    ''' Prints a debug string '''
    if _debug_active_:
        print ">>>Debug: " + str(string)

def on_file_change():
    ''' Defines what happens when watched file changes. '''
    global _web_view, _currentfiletowatch_, _defaultfiletowatch_

    with open(_currentfiletowatch_, "rb") as f:
        to_view = f.read()
    try:
        #Finds the first site:http://someweb.com/ and represents it in Sebastian.
        to_view = to_view.split("site:")[1].split("\n")[0].replace(" ", "").rstrip()
        dprint(to_view)
    except Exception as e:
        #Whatever happens just not try to refresh
        return
    _web_view.load(QtCore.QUrl(to_view))

def on_start():
    ''' Sets up the QFileSystemWatcher and starts a
    fullscreen window with the contents '''
    global _currentfiletowatch_, _defaultfiletowatch_, _app_
    
    #User does not have selected a file
    if _currentfiletowatch_ == "":
        _currentfiletowatch_ = _defaultfiletowatch_

    #Cleans filesystemwatcher
    for path in filewatcher.files():
        filewatcher.removePath(path)
    #Add new path to watch
    filewatcher.addPath(_currentfiletowatch_)
    #Refresh for the first time
    on_file_change()
    #Show Sebastian fullscreen window
    _app_.setOverrideCursor(QtCore.Qt.BlankCursor)
    sebastian_window.show()

def on_config():
    ''' Lets the user select a file to watch '''
    file_path, _ = QtGui.QFileDialog.getOpenFileName(w, "Select File to watch", expanduser("~"), "Text files (*.txt)")
    if len(file_path) > 2:
        #File selected
        global _currentfiletowatch_
        _currentfiletowatch_ = file_path
    else:
        #File not selected, ignoring
        pass

def on_about():
    about_window.show()

def on_show_on_start():
    filetosave = open(_preferences_file_, "wb")
    if show_on_start_chk.isChecked():
        filetosave.write("run_on_start: true\n")
        filetosave.write("file_to_watch: " + _currentfiletowatch_ + "\n")
    else:
        filetosave.write("run_on_start: false")
    filetosave.close()

''' Resources creation '''
QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName('UTF-8'))
# region Main window definition
w = QtGui.QDialog()
w.setFixedSize(420, 180)
w.setWindowFlags(QtCore.Qt.Dialog)
w.setWindowTitle('Sebastian Control Panel ' + str(__version__))
main_layout = QtGui.QVBoxLayout()
main_groupbox = QtGui.QGroupBox("Sebastian Control Panel")
gp_layout = QtGui.QVBoxLayout()
first_row_layout = QtGui.QHBoxLayout()
second_row_layout = QtGui.QHBoxLayout()

start_button = QtGui.QPushButton("Start Sebastian")
start_button.clicked.connect(on_start)
config_button = QtGui.QPushButton("File to check")
config_button.clicked.connect(on_config)
show_on_start_chk = QtGui.QCheckBox("Run on startup")
show_on_start_chk.stateChanged.connect(on_show_on_start)
about_button = QtGui.QPushButton("About this")
about_button.clicked.connect(on_about)

first_row_layout.addWidget(start_button)
first_row_layout.addWidget(config_button)

second_row_layout.addWidget(show_on_start_chk)
second_row_layout.addWidget(about_button)
    
gp_layout.addLayout(first_row_layout)
gp_layout.addLayout(second_row_layout)
main_groupbox.setLayout(gp_layout)
main_layout.addWidget(main_groupbox)
w.setLayout(main_layout)
w.show()
# endregion Main window definition

# region Sebastian fullscreen window
sebastian_window = QtGui.QDialog()
main_layout = QtGui.QHBoxLayout()
main_layout.setContentsMargins(0,0,0,0)
_web_view = QtWebKit.QWebView()
_web_view.load(QtCore.QUrl(""))
_web_view.page().mainFrame().setScrollBarPolicy(QtCore.Qt.Orientation.Vertical, QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
filewatcher = QtCore.QFileSystemWatcher()
filewatcher.fileChanged.connect(on_file_change)
main_layout.addWidget(_web_view)
sebastian_window.setWindowState(QtCore.Qt.WindowFullScreen)
sebastian_window.setLayout(main_layout)
# endregion Sebastian fullscreen window

# region About window
about_window = QtGui.QDialog()
about_window.setFixedSize(420, 180)
about_window.setWindowFlags(QtCore.Qt.Dialog)
about_window.setWindowTitle('About Sebastian')
about_window_layout = QtGui.QVBoxLayout()
name_label = QtGui.QLabel("Software Name: Sebastian")
version_label = QtGui.QLabel("Software Version: " + __version__)
credits_label = QtGui.QLabel("Software Credits: " + ", ".join(__credits__))
license_label = QtGui.QLabel("License: " + __license__)
separator = QtGui.QFrame()
separator.setFrameShape(QtGui.QFrame.HLine)
separator.setFrameShadow(QtGui.QFrame.Sunken)

button_layout = QtGui.QHBoxLayout()
about_ok_button = QtGui.QPushButton("Cool")
about_ok_button.clicked.connect(lambda : about_window.hide())
button_layout.addStretch(1)
button_layout.addWidget(about_ok_button)

about_window_layout.addWidget(name_label)
about_window_layout.addWidget(version_label)
about_window_layout.addWidget(credits_label)
about_window_layout.addWidget(license_label)
about_window_layout.addWidget(separator)
about_window_layout.addStretch(1)
about_window_layout.addLayout(button_layout)

about_window.setLayout(about_window_layout)
# endregion About window

#Watch if it has to show sebastian by default
run_on_startup = False
filetowatch = ""
try:
    if(os.path.isfile(_preferences_file_)):
        preferences = open(_preferences_file_, "rb").read()
        run_on_startup = True if ("true" in preferences.split("run_on_start: ")[1].lower()) else False
        _currentfiletowatch_ = preferences.split("file_to_watch: ")[1].split("\n")[0]
except Exception as e:
    print e

#Execute
if run_on_startup:
    show_on_start_chk.setChecked(True)
    on_start()

sys.exit(_app_.exec_())
