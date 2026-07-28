import json
import pytest
import pytchat
from pytchat.parser.live import Parser
from pytchat.processors.speed.calculator import SpeedCalculator

parser = Parser(is_replay=False)


def test_speed_1():
    try:
        stream = pytchat.create("mKCieTImjvU", seektime=6000, processor=SpeedCalculator())
    except Exception:
        pytest.skip("YouTube API unreachable or video unavailable")
    while stream.is_alive():
        speed = stream.get()
        assert speed > 100
        break
