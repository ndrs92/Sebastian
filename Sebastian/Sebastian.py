#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sebastian main executable.

"""

"""
LICENSE DETAILS
"""

__author__ = "Andrés Vieira"
__copyright__ = "Copyright 2016, Andrés Vieira"
__credits__ = ["Andrés Vieira", "Samuel Rodríguez Borines"]
__license__ = "GPL"
__version__ = "v0.1 BETA"
__maintainer__ = "Andrés Vieira"
__email__ = "anvieiravazquez@gmail.com"
__status__ = "Development"

_webdir_ = "localhost"
_filetowatch_ = "./currentstate.txt"

import sys
from os.path import expanduser
from PySide import QtGui, QtCore, QtWebKit

app = QtGui.QApplication(sys.argv)
w = QtGui.QDialog()
_web_view = QtWebKit.QWebView()

def dprint(string):
    print ">>>Debug: " + str(string)

def on_start():
    sebastian_window = QtGui.QDialog()
    main_layout = QtGui.QHBoxLayout()
    main_layout.setContentsMargins(0,0,0,0)
    _web_view.load(QtCore.QUrl("http://www.google.es/"))
    _web_view.page().mainFrame().setScrollBarPolicy(QtCore.Qt.Orientation.Vertical, QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    main_layout.addWidget(_web_view)
    sebastian_window.setWindowState(QtCore.Qt.WindowFullScreen)
    sebastian_window.setLayout(main_layout)
    sebastian_window.exec_()

def on_config():
    file_path = QtGui.QFileDialog.getOpenFileName(w, "Select File to watch", expanduser("~"), "Text files (*.txt)")
    if len(file_path) > 2:
        #File selected
        _filetowatch_ = file_path
    else:
        #File not selected, ignoring
        pass

def on_about():
    pass

def main():
    """ Main function. """

    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName('UTF-8'))
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
    logo = QtGui.QLabel("Sebastian " + __version__)
    about_button = QtGui.QPushButton("About this")

    first_row_layout.addWidget(start_button)
    first_row_layout.addWidget(config_button)

    second_row_layout.addWidget(logo)
    second_row_layout.addWidget(about_button)
    

    gp_layout.addLayout(first_row_layout)
    gp_layout.addLayout(second_row_layout)
    main_groupbox.setLayout(gp_layout)
    main_layout.addWidget(main_groupbox)
    w.setLayout(main_layout)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()