from datetime import datetime
import pytz
from datetime import date
import os


class Logger:
    logcounter = 0
    path = ""
    f0 = ""
    f1 = ""
    f2 = ""
    f3 = ""

    def __init__(self):
        x = str(datetime.now(pytz.utc)).replace(":", ".")
        self.path = "log/" + "[" + str(date.today()) + "-" + x + "] Log/"
        os.mkdir(self.path)

        self.f0 = open(self.path + "Level Critical_Error.log", "a")
        self.f1 = open(self.path + "Level Error.log", "a")
        self.f2 = open(self.path + "Level Info.log", "a")
        self.f3 = open(self.path + "Level Debug.log", "a")

    def writelog(self, string, level):
        self.logcounter += 1

        if level == 0:
            Type = "CRITICAL ERROR  "
        elif level == 1:
            Type = "ERROR           "
        elif level == 2:
            Type = "INFO            "
        else:
            Type = "DEBUG           "

        string = Type + ": [" + str('{:10d}'.format(self.logcounter)) + "] " + "[" + str(date.today()) + "-" + str(
            datetime.now(pytz.utc)) + "] - Massage: " + string + "\n"

        if level == 0:
            self.f0.write(string)
            self.f1.write(string)
            self.f2.write(string)
            self.f3.write(string)
        elif level == 1:
            self.f1.write(string)
            self.f2.write(string)
            self.f3.write(string)
        elif level == 2:
            self.f2.write(string)
            self.f3.write(string)
        else:
            self.f3.write(string)
