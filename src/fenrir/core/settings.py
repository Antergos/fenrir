#!/bin/python
# -*- coding: utf-8 -*-

# Fenrir TTY screen reader
# By Chrys, Storm Dragon, and contributers.

from core import debug

settings = {
'sound': {
  'enabled': True,
  'driver': 'genericDriver', 
  'theme': 'default',
  'volume': 1.0,
  'genericPlayFileCommand': 'play -q -v fenrirVolume fenrirSoundFile',
  'genericFrequencyCommand': 'play -q -v fenrirVolume -n -c1 synth fenrirDuration sine fenrirFrequence'
},
'speech':{
  'enabled': True,
  'driver': 'speechdDriver',
  'rate': 0.75,
  'pitch': 0.5,
  'capitalPitch':0.8,
  'volume': 1.0,    
  'module': 'espeak',
  'voice': '',
  'language': 'english-us',
  'autoReadIncoming': True,
  'genericSpeechCommand':'espeak -a fenrirVolume -s fenrirRate -p fenrirPitch -v fenrirVoice "fenrirText"',
  'fenrirMinVolume':0,
  'fenrirMaxVolume':200,
  'fenrirMinPitch':0,
  'fenrirMaxPitch':99,
  'fenrirMinRate':80,
  'fenrirMaxRate':450,   
},
'braille':{
  'enabled': False, 
  'driver':'brlapiDriver',
  'layout': 'en',
  'flushMode': 'word', #NONE,FIX,CHAR,WORD
  'flushTimeout': 3,
  'cursorFocusMode':'page', # page,fixCell
  'fixCursorOnCell': -1,
  'cursorFollowMode': 'review', # none, review, last, text  
  'panSizeHorizontal': 0 # 0 = display size
},
'screen':{
    'driver': 'vcsaDriver',
    'encoding': 'cp850',
    'screenUpdateDelay': 0.1,
    'suspendingScreen': '',
    'autodetectSuspendingScreen': False,
},
'general':{
  'debugLevel': debug.debugLevel.DEACTIVE,
  'punctuationProfile':'default',
  'punctuationLevel': 'some',
  'respectPunctuationPause':True,
  'newLinePause':True,
  'numberOfClipboards': 10,
  'emoticons': True,
  'fenrirKeys': 'KEY_KP0,KEY_META',
  'scriptKeys': 'KEY_COMPOSE',  
  'timeFormat': '%I:%M%P',
  'dateFormat': '%A, %B %d, %Y',
  'autoSpellCheck': False,
  'spellCheckLanguage': 'en_US',
  'scriptPath':'/usr/share/fenrir/scripts',
  'commandPath':'/usr/share/fenrir/commands',
},
'focus':{
  'cursor': True,
  'highlight': False,
},
'review':{
  'lineBreak': True,
  'endOfScreen': True,
  'leaveReviewOnKeypress': False,
  'leaveReviewOnScreenChange': True,
},
'promote':{
  'enabled': True,
  'inactiveTimeoutSec': 120,
  'list': '',
},
'time':{
  'enabled': False,
  'presentTime': True,
  'presentDate': True,  
  'delaySec': 0,
  'onMinutes': '00,30',
  'announce': True,
  'interrupt': False,
},
'keyboard':{
  'driver': 'evdev',
  'device': 'all',
  'grabDevices': True,
  'ignoreShortcuts': False,  
  'keyboardLayout': "desktop",
  'charEcho': False,
  'charDeleteEcho': True,
  'wordEcho': True,
  'interruptOnKeyPress': True,
  'interruptOnKeyPressFilter': '',
  'doubleTapTimeout': 0.2,
}
}
