import pytest
from src.keyboard import Keyboard


def test_property_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    with pytest.raises(AttributeError):
        kb.language = "RU"

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.change_lang().language == "RU"
    assert kb.change_lang().language == "EN"