#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug
from utils import line_utils

class command():
    def __init__(self):
        pass
    def initialize(self, environment):
        self.env = environment
    def shutdown(self):
        pass 
    def getDescription(self):
        return _('present first line')        
    
    def run(self):
        x, y, firstLine = \
          line_utils.getCurrentLine(0, 0, self.env['screenData']['newContentText'])
        
        if firstLine.isspace():
            self.env['runtime']['outputManager'].presentText(_("blank"), soundIcon='EmptyLine', interrupt=True)
        else:
            self.env['runtime']['outputManager'].presentText(firstLine, interrupt=True) 
    def setCallback(self, callback):
        pass

