"""
This module currently provides a cross-platform getch function
"""

__all__ = ['getch']

try:
    # Windows
    from msvcrt import getch  # type: ignore
except ImportError:
    pass

try:
    # Unix
    import sys
    import termios
    import tty

    def getch():  # type: ignore
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

except ImportError:
    pass
