import curses
import time
import sys


def main(stdscr):
    while True:
        try:
            millis = time.time() * 1000
            jdut = 2440587.5 + (millis/(8.64*pow(10, 7)))
            jdtt = jdut + (37+32.184)/86400
            tj2000 = jdtt - 2451545

            msd = (((tj2000-4.5)/1.027491252) + 44796 - 0.00096)
            mtc = (24*msd) % 24
            minutes = (mtc - int(mtc)) * 60
            seconds = (minutes - int(minutes)) * 60

            sol_date = 'Sol date: {:.6f}'.format(msd)
            cmt = 'Coordinated Mars Time: {:02.0f}:{:02.0f}:{:02.0f}'.format(
                mtc, minutes, seconds)
            stdscr.addstr(0, 0, sol_date)
            stdscr.addstr(1, 0, cmt)
            stdscr.refresh()
        except KeyboardInterrupt:
            sys.exit()

screen = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.wrapper(main)
