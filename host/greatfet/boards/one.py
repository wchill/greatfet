#
# This file is part of GreatFET
#

from ..board import GreatFETBoard

from ..peripherals.gpio import GPIO
from ..peripherals.led import LED
from ..peripherals.i2c_bus import I2CBus
from ..peripherals.spi_bus import SPIBus
from ..peripherals.spi_flash import SPIFlash

from ..glitchkit import *



class GreatFETOne(GreatFETBoard):
    """ Class representing GreatFET One base-boards. """

    # Currently, all GreatFET One boards have an ID of zero.
    HANDLED_BOARD_IDS = [0]
    BOARD_NAME = "GreatFET One"

    # The GreatFET one has four LEDs.
    SUPPORTED_LEDS = 4

    # All of the GPIO mappings accessible from the GreatFET headers.
    # TODO: 
    GPIO_MAPPINGS = {
        #"J1_P1"   : GND,
        #"J2_P2"   : VCC,
        "J1_P3"    : (5, 13),
        "J1_P4"    : (0, 0),
        "J1_P5"    : (5, 14),
        "J1_P6"    : (0, 1),
        "J1_P7"    : (0, 4),
        "J1_P8"    : (2, 9),
        "J1_P9"    : (2, 10),
        "J1_P10"   : (0, 8),
        #"J2_P11"  : CLK0,
        "J1_P12"   : (0, 9),
        "J1_P13"   : (1, 8),
        "J1_P14"   : (2, 11),
        "J1_P15"   : (1, 0),
        "J1_P16"   : (1, 9),
        "J1_P17"   : (1, 2),
        "J1_P18"   : (1, 1),
        "J1_P19"   : (2, 12),
        "J1_P20"   : (1, 3),
        "J1_P21"   : (1, 5),
        "J1_P22"   : (1, 4),
        "J1_P23"   : (2, 14),
        "J1_P24"   : (2, 13),
        "J1_P25"   : (1, 7),
        "J1_P26"   : (1, 6),
        "J1_P27"   : (2, 15),
        "J1_P28"   : (0, 2),
        "J1_P29"   : (2, 7),
        "J1_P30"   : (0, 3),
        "J1_P31"   : (0, 13),
        "J1_P32"   : (0, 12),
        "J1_P33"   : (5, 18),
        "J1_P34"   : (4, 11),
        "J1_P35"   : (5, 0),
        # P36"     : P6_0,
        "J1_P37"   : (0, 15),
        # P38"     : P1_19,
        "J1_P39"   : (0, 11),
        "J1_P40"   : (0, 10),
        # J2_P1"   : GND,
        # J2_P2"   : VBUS,
        "J2_P3"    : (5, 12),
        "J2_P4"    : (2, 0),
        #"J2_P5"   : ADC0_0,
        "J2_P6"    : (2, 5),
        "J2_P7"    : (2, 4),
        "J2_P8"    : (2, 2),
        "J2_P9"    : (2, 3),
        "J2_P10"   : (2, 6),
        #"J2_P11"  : P4_7,
        #"J2_P12"  : CLK2,
        "J2_P13"   : (5, 7),
        "J2_P14"   : (0, 7),
        "J2_P15"   : (5, 6),
        "J2_P16"   : (3, 15),
        #"J2_P17"  : WAKEUP0,
        "J2_P18"   : (5, 5),
        "J2_P19"   : (5, 4),
        "J2_P20"   : (5, 3),
        #"J2_P21" : PF_4,
        "J2_P22"   : (5, 9),
        "J2_P23"   : (3, 10),
        "J2_P24"   : (5, 8),
        "J2_P25"   : (3, 9),
        #"J2_P26" : P3_0,
        "J2_P27"   : (3, 8),
        "J2_P28"   : (1, 14),
        "J2_P29"   : (5, 16),
        "J2_P30"   : (5, 10),
        "J2_P31"   : (5, 15),
        #"J2_P32" : P3_3,
        "J2_P33"   : (5, 2),
        "J2_P34"   : (0, 5),
        "J2_P35"   : (5, 1),
        "J2_P36"   : (3, 2),
        "J2_P37"   : (1, 15),
        "J2_P38"   : (0, 6),
        #"J2_P39"  : I2C0_SDA,
        #"J2_P40"  : I2C0_SDL,
        #"J7_P1"  : GND,
        "J7_P2"    : (3, 3),
        "J7_P3"    : (3, 4),
        #"J7_P4"   : ADC0_5,
        #"J7_P5"   : ADC0_2,
        "J7_P6"    : (1, 10),
        "J7_P7"    : (1, 12),
        "J7_P8"    : (1, 13),
        #"J7_P9"   : RTC_ALARM,
        #"J7_P10"  : GND,
        #"J7_P11"  : RESET,
        #"J7_P12"  : VBAT,
        "J7_P13"   : (1, 11),
        "J7_P14"   : (0, 14),
        "J7_P15"   : (3, 6),
        "J7_P16"   : (3, 5),
        "J7_P17"   : (3, 1),
        "J7_P18"   : (3, 0),
        #"J7_P19"  : GND,
        #"J7_P20"  : VCC,
    }


    def __init__(self, **device_identifiers):
        """ Initialize a new GreatFET One connection. """

        # Set up the core connection.
        super(GreatFETOne, self).__init__(**device_identifiers)

        # TODO: Abstract the below into a 'pull out standard peripherals'
        # method?

        # Initialize the fixed peripherals that come on the board.
        # TODO: Use a self.add_peripheral mechanism, so peripherals can
        # be dynamically listed?
        self.onboard_flash = SPIFlash(self)
        self.i2c_busses = [ I2CBus(self, 'I2C0') ]
        self.spi_busses = [ SPIBus(self, 'SPI1') ]

        # Create an easy-to-use alias for the primary busses, for rapid
        # hacking/experimentation.
        self.i2c = self.i2c_busses[0]
        self.spi = self.spi_busses[0]

        # Populate the per-board GPIO.
        self._populate_gpio()

        # Add objects for each of our LEDs.
        self._populate_leds(self.SUPPORTED_LEDS)

        # Implement any GlitchKit modules we support.
        self.glitchkit = GlitchKitCollection(self)


