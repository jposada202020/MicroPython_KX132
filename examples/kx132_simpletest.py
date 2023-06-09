# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_kx132 import kx132

i2c = I2C(1, sda=Pin(2), scl=Pin(3))
kx = kx132.KX132(i2c)


while True:
    accx, accy, accz = kx.acceleration
    print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
    time.sleep(0.1)
