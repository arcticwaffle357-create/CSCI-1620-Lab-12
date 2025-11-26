class Television:
    '''This function takes input from main.py and modifies the TV's power status, volume, and channel.
    :param MIN_VOLUME: The minimum allowed volume value for the TV.
    :param MAX_VOLUME: The maximum allowed volume value for the TV.
    :param MIN_CHANNEL: The minimum allowed channel value for the TV.
    :param MAX_CHANNEL: The maximum allowed channel value for the TV.
    :return:
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
    def __init__ sets the initial values for the TV's power status, volume, and channel.

    :param self._status: A private variable that sets the initial power status of the TV to on (True) or off (False)
    :param self._muted: A private variable that sets the initial mute status of the TV to on (True) or off (False)
    :param self._volume: A private variable that sets the initial volume status of the TV to the previously defined MIN_VOLUME
    :param self._channel: A private variable that sets the initial channel status of the TV to the previously defined MIN_CHANNEL
        '''
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