from television import Television
import pytest

def test_init():
    tv = Television()
    assert tv._status is False
    assert tv._muted is False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL

def test_starting_volume_change():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME

def test_volume_limits():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME
    tv.volume_down()
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME

def test_channels():
    tv = Television()
    tv.power()
    assert tv._channel == Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv._channel == Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL

def test_str_return():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.volume_up()
    tv._status = "On" if tv._status else "Off"
    expected = f"Power = [{tv._status}], Channel = [{tv._channel}], Volume = [{tv._volume}]"
    assert str(tv) == expected

if __name__ == "__main__":
    pytest.main()