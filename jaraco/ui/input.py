"""
This module currently provides a cross-platform getch function
"""

import sys

if sys.platform == "win32":
    from msvcrt import getch as getch
else:
    try:
        # Unix
        import sys
        import termios
        import tty

        def getch():
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)

    except ImportError:
        pass
