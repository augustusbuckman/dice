import os.path
import sys
from unittest import TestCase

from dice import main
from tud_test_base import *
def test_dice():
    try:
        exist = os.path.exists("dice.py")
        assert exist == True
    except:
        sys.exit()

    set_keyboard_input(['y',-251,10000000])
    main()
    output = get_display_output()
    assert output == [
        "This program simulates the dice game of craps.",
        "Do you want to set the seed? Enter y for yes, anything else for no: ",
        "Enter the number of rounds to run: ",
        "Enter an int for the initial seed: ",
        "Player won 4927042 times in 10000000 rounds.",
        "Maximum number of rolls in a round = 52"
    ]
