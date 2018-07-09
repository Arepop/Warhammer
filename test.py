import machine
import neopixel
import time
import socket
import os
import math


def begin():
    np = neopixel.NeoPixel(machine.Pin(4, machine.Pin.OUT), 108)
    for i in range(108):
        np[i] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    for i in range(108):
        np[i] = (0, 0, 0)
    np.write()

    return np


def recive_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind('', 80)
    s.listen(5)
    print('socket established')

    return s


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('JaskiniaSmoka', 'Czerwony$m0k')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def get_command(soc):
    conn, addr = soc.accept()
    rq = str(conn.recv(512))
    command = rq[rq.find('b')+1:rq.find('e')]

    return command

def color(np, leds, br, r, g, b):

    br = int(br)
    r, g, b = int(r)*(br/255), int(g)*(br/255), int(b)*(br/255)
    for led in leds:
        np[led] = (int(r), int(g), int(b))


def led_rand(np, leds):
    colors = [np[i] for i in range(108)]
    RNG = int.from_bytes(os.urandom(1), byteorder='big') % 6
    T = 0.01
    for i in range(18+RNG):
        RNG2 = int.from_bytes(os.urandom(1), byteorder='big') % 6
        color(np, leds[RNG2], br, 255, 255, 255)
        time.sleep(math.sqrt(T))
        np.write()
        color(np, leds[RNG2], 0, 255, 255, 255)
        T += 0.003

    for i in range(4):
        color(np, leds[RNG2], 0, 255, 0, 0)
        time.sleep_ms(25)
        np.write()
        color(np, leds[RNG2], 0, 255, 255, 255)
        time.sleep_ms(25)
        np.write()
    return colors


def update(np):
    soc = recive_socket()
    all_leds = list(range(18*i, 18*(i+1)) for i in reversed(range(6)))
    while True:
        command = get_command(soc)
        conds, br, r, g, b, mode = command.split('?')
        table = zip(list(conds), all_leds)
        for con, leds in table:
            if int(con):
                color(np, leds, br, r, g, b)

        if int(mode) == 1:
            colors = led_rand(np, leds)
            for led, colo in enumerate(colors):
                np[led] = colo

        if mode == 2:

        np.write()


if __name__ == '__main__':
    np = begin()
    do_connect()
    update(np)
