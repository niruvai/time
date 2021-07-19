"""Speak the time."""



import time

droid = androidhelper.Android()

droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
