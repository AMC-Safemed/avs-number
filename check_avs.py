#!/usr/bin/env python3

__author__ = 'Mathieu Clement'
__license__ = 'GPL'

def canonize(avs_no):
    return avs_no.replace('.', '') # remove dots

def is_valid_avs_number(number):
    """Checks AVS/AHV number. Provide number as string with or without dots."""
    # https://www.admin.ch/opc/fr/classified-compilation/20071554/index.html#app1
    # admin.ch document 831.101.4 ... "Logique de la cle de controle"

    number = canonize(number)

    if len(number) != 13:
        return False

    odd = lambda i: 3 * int(number[i])
    even = lambda i: int(number[i])

    total = odd(11) + even(10) + odd(9) + even(8) + odd(7) + even(6) + \
            odd(5) + even(4) + odd(3) + even(2) + odd(1) + even(0)

    expected_key = 0
    if total % 10 != 0:
        ten_up = (total//10)*10 + 10
        expected_key = ten_up - total

    actual_key = int(number[12])

    return actual_key == expected_key
