#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug

class command():
    def __init__(self):
        pass
    def initialize(self, environment):
        self.env = environment
    def shutdown(self):
        pass
    def getDescription(self):
        return 'No Description found'        

    def run(self):
        if not self.env['runtime']['settingsManager'].getSettingAsBool('keyboard', 'charDeleteEcho'):
            return

        # detect typing or chilling
        if self.env['screenData']['newCursor']['x'] >= self.env['screenData']['oldCursor']['x']:
            return 

        # More than just a deletion happend

        if self.env['runtime']['screenManager'].isDelta():
            return
        # no deletion
        if not self.env['runtime']['screenManager'].isNegativeDelta():
            return
        if self.env['runtime']['inputManager'].noKeyPressed():
            return              

        # too much for a single backspace...
        # word begin produce a diff wiht len == 2 |a | others with 1 |a|
        if len(self.env['screenData']['newNegativeDelta']) > 2:
            return           
        currNegativeDelta = self.env['screenData']['newNegativeDelta']
        if len(currNegativeDelta.strip()) != len(currNegativeDelta) and \
          currNegativeDelta.strip() != '':
            currNegativeDelta = currNegativeDelta.strip()
        self.env['runtime']['outputManager'].presentText(currNegativeDelta, interrupt=True, ignorePunctuation=True, announceCapital=True, flush=False)

    def setCallback(self, callback):
        pass

