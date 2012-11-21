'''\
print colorful string on console

usage: 
> from colorlib import *
> print red('red'), bold('bold')
'''

import sys

__all__ = ['bg_black', 'bg_blue', 'bg_cyan', 'bg_green', \
               'bg_magenta', 'bg_red', 'bg_white', 'bg_yellow', \
               'black', 'blink', 'blue', 'bold', 'cyan', 'green', \
               'hide', 'magenta', 'off', 'red', 'white', 'yellow']



def isColorfull(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False

    return True

def off(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[0m" + str + "\033[0m"

def bold(str):
    if not isColorfull(sys.stdout):
        return str 
    return "\033[1m" + str + "\033[0m"

def blink(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[4m" + str + "\033[0m"

def hide(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[8m" + str + "\033[0m"

def black(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[30m" + str + "\033[0m"

def red(str):
    if not isColorfull(sys.stdout):
        return str

    return "\033[31m" + str + "\033[0m"

def green(str):
    if not isColorfull(sys.stdout):
        return str
    return"\033[32m" + str + "\033[0m"

def yellow(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[33m" + str + "\033[0m"

def blue(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[34m" + str + "\033[0m"

def magenta(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[35m" + str + "\033[0m"

def cyan(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[36m" + str + "\033[0m"

def white(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[37m" + str + "\033[0m"

def bg_black(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[40m" + str + "\033[0m"

def bg_red(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[41m" + str + "\033[0m"

def bg_green(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[42m" + str + "\033[0m"

def bg_yellow(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[43m" + str + "\033[0m"

def bg_blue(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[44m" + str + "\033[0m"

def bg_magenta(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[45m" + str + "\033[0m"

def bg_cyan(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[46m" + str + "\033[0m"

def bg_white(str):
    if not isColorfull(sys.stdout):
        return str
    return "\033[47m" + str + "\033[0m"
