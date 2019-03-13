#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Avalon generic user I/O framework

Description: this framework tries to make printing messages and
getting user input easier it includes most UNIX terminal background
and foreground colors.

Name: Avalon Framework
Author: K4T
Date Created: March 20, 2017
Last Modified: March 13, 2019

Licensed under the GNU Lesser General Public License Version 3 (GNU LGPL v3),
    available at: https://www.gnu.org/licenses/lgpl-3.0.txt

(C) 2017 - 2019 K4YT3X
"""
import sys

if sys.platform == 'win32':
    from colorama import init
    init()
else:
    import syslog

VERSION = '1.6.3'


class Avalon:
    """ Avalon Standard Input/Output Framework

    The avalon framework provides convenient and beautiful methods
    to handle command line user input or program output. It's based on
    Unix console colors, and is made compatible with the Windows platform
    with the colorama library.
    """

    class FG():
        """ Foreground Colors

        This class contains all foreground colors.
        Access colors via Avalon.FG.Color.
        """

        # Standard colors
        BL = '\033[30m'  # Black
        R = '\033[31m'  # Red
        G = '\033[32m'  # Green
        Y = '\033[33m'  # Yellow
        B = '\033[34m'  # Blue
        M = '\033[35m'  # Magenta
        C = '\033[36m'  # Cyan
        
        # Light colors
        LGR = '\033[37m'  # Light Grey
        DGR = '\033[90m'  # Dark Grey
        LR = '\033[91m'  # Light Red
        LG = '\033[92m'  # Light Green
        LY = '\033[93m'  # Light Yellow
        LB = '\033[94m'  # Light Blue
        LM = '\033[95m'  # Light Magenta
        LC = '\033[96m'  # Light Cyan
        W = '\033[97m'  # White

    class BG():
        """ Foreground Colors

        This class contains all background colors.
        Access colors via Avalon.BG.Colors.
        """
        BL = '\033[40m'  # Black
        R = '\033[41m'  # Red
        G = '\033[42m'  # Green
        Y = '\033[43m'  # Yellow
        B = '\033[44m'  # Blue
        M = '\033[45m'  # Magenta
        C = '\033[46m'  # Cyan
        LGR = '\033[47m'  # Light Grey
        DGR = '\033[100m'  # Dark Grey
        LR = '\033[101m'  # Light Red
        LG = '\033[102m'  # Light Green
        LY = '\033[103m'  # Light Yellow
        LB = '\033[104m'  # Light Blue
        LM = '\033[105m'  # Light Magenta
        LC = '\033[106m'  # Light Cyan
        WT = '\033[107m'  # White

    class FM():
        """ Formatting Sequences

        This class contains all formatting-related
        sequences, such as bold or italic.
        Access formats via Avalon.FM.Color.
        """
        # SET
        BD = '\033[1m'  # Bold
        DM = '\033[2m'  # Dim
        UN = '\033[4m'  # Underlined
        BL = '\033[5m'  # Blink
        RV = '\033[7m'  # Reverse
        HD = '\033[8m'  # Hidden

        # RESET
        RST = '\033[0m'  # Reset ALL
        RBD = '\033[21m'  # Bold
        RDM = '\033[22m'  # Dim
        RUN = '\033[24m'  # Underlined
        RBL = '\033[25m'  # Blink
        RRV = '\033[27m'  # Reverse
        RHD = '\033[28m'  # Hidden

    def info(msg, log=False):
        """ print regular information
        """
        print('{}[+] INFO: {}{}'.format(Avalon.FG.G, str(msg), Avalon.FM.RST))
        if log and sys.platform != 'win32':
            syslog.syslog(syslog.LOG_INFO, msg)

    def time_info(msg, log=False):
        """ print regular information with time stamp
        """
        import datetime
        print('{}{}{} [+] INFO: {}{}'.format(Avalon.FM.RST, str(datetime.datetime.now()), Avalon.FG.G, str(msg), Avalon.FM.RST))
        if log and sys.platform != 'win32':
            syslog.syslog(syslog.LOG_INFO, msg)

    def debug_info(msg, log=True):
        """ print information fo debugging
        """
        import datetime
        print('{}{} [+] INFO: {}{}'.format(Avalon.FG.DGR, str(datetime.datetime.now()), str(msg), Avalon.FM.RST), file=sys.stderr)
        if log and sys.platform != 'win32':
            syslog.syslog(syslog.LOG_DEBUG, msg)

    def warning(msg, log=False):
        """ print a warning message
        """
        print('{}{}[!] WARNING: {}{}'.format(Avalon.FG.Y, Avalon.FM.BD, str(msg), Avalon.FM.RST), file=sys.stderr)
        if log and sys.platform != 'win32':
            syslog.syslog(syslog.LOG_WARNING, msg)

    def error(msg, log=True):
        """ print an error message
        """
        print('{}{}[!] ERROR: {}{}'.format(Avalon.FG.R, Avalon.FM.BD, str(msg), Avalon.FM.RST), file=sys.stderr)
        if log and sys.platform != 'win32':
            syslog.syslog(syslog.LOG_WARNING, msg)

    def debug(msg, log=True):
        """ print a debug message
        """
        print('{}{}[*] DEBUG: {}{}'.format(Avalon.FG.R, Avalon.FM.RDM, str(msg), Avalon.FM.RST), file=sys.stderr)
        if log and sys.platform != 'win32':
            syslog.syslog(syslog.LOG_DEBUG, msg)

    def gets(msg, default=None, batch=False):
        """ Gets user input as a string
        """

        # if batch is set, return the default value
        if batch:
            return default

        print('{}{}[?] USER: {}{}'.format(Avalon.FG.Y, Avalon.FM.BD, msg, Avalon.FM.RST), end='')
        return input()

    def ask(msg, default=False, batch=False):
        """ Gets a True / False answer from user

        This method will ask user a question that will
        require a true / false answer. Pressing enter without
        entering anything will return the default value.
        """

        # if batch is set, return the default value
        if batch:
            return default

        elif default is False:
            while True:
                ans = Avalon.gets(msg + ' [y/N]: ')
                if ans == '' or ans[0].upper() == 'N':
                    return False
                elif ans[0].upper() == 'Y':
                    return True
                else:
                    Avalon.error('Invalid Input!')
        elif default is True:
            while True:
                ans = Avalon.gets(msg + ' [Y/n]: ')
                if ans == '' or ans[0].upper() == 'Y':
                    return True
                elif ans[0].upper() == 'N':
                    return False
                else:
                    Avalon.error('Invalid Input!')
        else:
            raise TypeError('invalid type for positional argument: \' default\'')
