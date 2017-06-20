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

    total = 0
    for i in range(0,12,2):
        total += even(i)
    for i in range(1,12,2):
        total += odd(i)

    expected_key = 0
    if total % 10 != 0:
        round_ten_up = (total//10)*10 + 10
        expected_key = round_ten_up - total

    actual_key = int(number[12])

    return actual_key == expected_key

if __name__ == '__main__':
    print('Expected: True, actual:', is_valid_avs_number('756.1234.5678.97'))
    print('Expected: False, actual:', is_valid_avs_number('756.1234.5678.98'))
    print('Expected: False, actual:', is_valid_avs_number('756.1234.5678.99'))
    print('Expected: False, actual:', is_valid_avs_number('756.1234.5678.9'))
    print('Expected: False, actual:', is_valid_avs_number('756.1234.5678.999'))
