#!/usr/bin/python
import os
import sys
import time

class CountDown:

    def __init__(self):

        # CHECKS FOR HELP REQUEST
        if sys.argv[1] == "help":
            print "\n./pycounter (hour) (min) (sec)\n"
            quit()

        os.system('clear')

        self.time = .5
        self.scale = 1

        # INTERPRETS ARGUMENTS FROM BASH ENVIRONMENT
        self.hours = int(sys.argv[1])
        self.minutes = int(sys.argv[2])
        self.seconds = int(sys.argv[3])

        # FOR SCROLLING WORDS
        self.char_count = 0

        # TILES FOR NUMBERS
        # Maybe move these somewhere else?
        tile_zero   = [' .d8888b. ', 'd88P  Y88b', '888    888', '888    888', '888    888', '888    888',
                       'Y88b  d88P', ' "Y8888P" ']
        tile_one    = [' d888     ', 'd8888     ', '  888     ', '  888     ', '  888     ', '  888     ',
                       '  888     ', '8888888   ']
        tile_two    = [' .d8888b. ', 'd88P  Y88b', '       888', '     .d88P', ' .od888P" ', 'd88P"     ',
                       '888"      ', '888888888 ']
        tile_three  = [' .d8888b. ', 'd88P  Y88b', '     .d88P', '    8888" ', '     "Y8b.', '888    888',
                       'Y88b  d88P', ' "Y8888P" ']
        tile_four   = ['    d8888 ', '   d8P888 ', '  d8P 888 ', ' d8P  888 ', 'd88   888 ', '8888888888',
                       '      888 ', '      888 ']
        tile_five   = ['888888888 ', '888       ', '888       ', '8888888b. ', '     "Y88b', '       888',
                       'Y88b  d88P', ' "Y8888P" ']
        tile_six    = [' .d8888b. ', 'd88P  Y88b', '888       ', '888d888b. ', '888P "Y88b', '888    888',
                       'Y88b  d88P', ' "Y8888P" ']
        tile_seven  = ['8888888888', '      d88P', '     d88P ', '    d88P  ', ' 88888888 ', '  d88P    ',
                       ' d88P     ', 'd88P      ']
        tile_eight  = [' .d8888b. ', 'd88P  Y88b', 'Y88b. d88P', ' "Y88888" ', '.d8P""Y8b.', '888    888',
                       'Y88b  d88P', ' "Y8888P" ']
        tile_nine   = [' .d8888b. ', 'd88P  Y88b', '888    888', 'Y88b. d888', ' "Y888P888', '       888',
                       'Y88b  d88P', ' "Y8888P" ']

        # DICTIONARY FOR REFERENCING TILES
        self.numbers = {0: tile_zero, 1: tile_one, 2: tile_two, 3: tile_three, 4: tile_four, 5: tile_five, 6: tile_six,
                        7: tile_seven, 8: tile_eight, 9: tile_nine}

    def timer(self):

        # CALCULATES TOTAL SECONDS, ALSO ITERATIONS OF COUNTER
        time_seconds = int((self.hours * 3600) + (self.minutes * 60) + self.seconds)

        # MATH COUNTING UP TO 60 IS A B#$%!, USES THESE RULES:
        for i in range(0, time_seconds):

            if self.seconds !=0:
                self.seconds -= 1
            else:
                self.seconds = 59
                if self.minutes !=0:
                    self.minutes -= 1
                else:
                    self.minutes = 59
                    if self.hours != 0:
                        self.hours -= 1

            # THAT BIG OL' PRETTY COUNTER
            self.printer()

            time.sleep(1)
            os.system('clear')

    def printer(self):

        print_count = 0

        # SEPERATES THE THE HOURS, MINUTES, AND SECONDS INTO EACH DIGIT IT WILL DISPLAY
        hours_tens   = int(self.hours / 10)
        hours_ones   = int(self.hours % 10)

        minutes_tens = int(self.minutes / 10)
        minutes_ones = int(self.minutes % 10)

        seconds_tens = int(self.seconds / 10)
        seconds_ones = int(self.seconds % 10)

        # CHANGES COLOR TO MATRIXY STUFF, MAYBE. DOESN'T WORK ON MY DESKTOP.
        # TRY UNCOMMENTING ON OTHER MACHINES AND SEE IF IT WORKS.
        #print "\033[1;32;40m"

        while print_count < (self.scale * 8):

            # PRINT HOURS
            print self.numbers[hours_tens][print_count],
            print self.numbers[hours_ones][print_count],

            if print_count == 3 or print_count == 5:
                print "  #  ",
            else:
                print "     ",

            # PRINT MINUTES
            print self.numbers[minutes_tens][print_count],
            print self.numbers[minutes_ones][print_count],

            if print_count == 3 or print_count == 5:
                print "  #  ",
            else:
                print "     ",

            # PRINT SECONDS
            print self.numbers[seconds_tens][print_count] + " ",
            print self.numbers[seconds_ones][print_count]
            print_count += 1

            # AFTER PRINTING THE LAST ROW OF CHARACTERS
            if print_count == 8:

                #CLEVER. (YES I MEAN HASHTAG CLEVER AND IT IS MEANT TO BE CLEVER)
                scroll_txt = "     CYBER PATRIOT 2016 - ROUND 2 - HAZEL GREEN HIGH SCHOOL - CAPTAIN PARKER PIERCE " \
                             "EXPECTED TO LEAD HIS TEAM TO VICTORY - SKIPPER NELSON STAYS SILENT ON SEX SCANDAL - " \
                             "COACH CASE CORRECTS THE RECORD ON CLAP CONFUSION - WHILE BASHING LINUX, RATTY MAT SAID" \
                             " 'I DON'T UNDERSTAND THE WHOLE CYBERSECURITY SHEBANG' --  "

                # ENSURES YOU AREN'T GETTING AN ERROR AFTER YOU GO OVER THE LENGTH
                if self.char_count > len(scroll_txt) + 8:
                    self.char_count = 0
                else:
                    pass

                print ""

                # PRINT IT
                print scroll_txt[self.char_count: self.char_count + 80]
                self.char_count += 6

        print ""


c = CountDown()
c.timer()


