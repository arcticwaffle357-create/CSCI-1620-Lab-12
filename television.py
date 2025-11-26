class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL 

    def power(self):
        if self._status == False:
            self._status = True
        else:
            self._status = False
    def mute(self):
        if self._muted == False and self._status == True:
            self._muted = True
        elif self._muted == True and self._status == True:
            self._muted = False
    def channel_up(self):
        if self._channel < Television.MAX_CHANNEL and self._status == True:
            self._channel += 1
        elif self._channel == Television.MAX_CHANNEL and self._status == True:
            self._channel = Television.MIN_CHANNEL
    def channel_down(self):
        if self._channel > Television.MIN_CHANNEL and self._status == True:
            self._channel -= 1
        elif self._channel == Television.MIN_CHANNEL and self._status == True:
            self._channel = Television.MAX_CHANNEL
    def volume_up(self):
        if self._volume < Television.MAX_VOLUME and self._status == True:
            self._volume += 1
        else:
            return
    def volume_down(self):
        if self._volume > Television.MIN_VOLUME and self._status == True:
            self._volume -= 1
        else:
            return
    def __str__(self):
        status = "On" if self._status else "Off"
        return f"Power = [{status}], Channel = [{self._channel}], Volume = [{self._volume}]"