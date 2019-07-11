from serial import Serial


class Controll:
    # Atribute:
    ser = ""
    logcounter = 0
    # Methods:

    # Init Methode
    def __init__(self, PORT, logger):
        logger.writelog("Conrtoll  INIT Start", 3)
        self.ser = Serial()  # serial port
        logger.writelog("Versuche Bautrate festzulegen", 3)
        self.ser.baudrate = 9600     # set bautdrate
        logger.writelog("Bautrate festgelegt auf 9600", 3)
        logger.writelog("Versuche Port Festzulegen", 3)
        self.ser.port = PORT     # Set PORT
        logger.writelog("Port Festgelegt", 3)
        logger.writelog("Versuche Port zu öffnen", 3)
        self.ser.open()          # open Port
        logger.writelog("Serieller Port geöffnet: " + PORT, 2)

        self.logger = logger

    # Step UP Methode
    def step_up(self):
        self.ser.write(b'UP')     # write a string "UP"
        self.logger.writelog("Butten UP Gedrückt", 2)

    # Step DOWN Methode
    def step_down(self):
        self.ser.write(b'DOWN')     # write a string "DOWN"
        self.logger.writelog("Butten DOWN Gedrückt", 2)

    # Step FORWARD Methode
    def step_forward(self):
        self.ser.write(b'FORWARD')     # write a string "FORWARD"
        self.logger.writelog("Butten FORWARD Gedrückt", 2)

    # Step BACK Methode
    def step_back(self):
        self.ser.write(b'BACK')     # write a string "BACK"
        self.logger.writelog("Butten BACK Gedrückt", 2)

    def step_go(self):
        self.ser.write(b'GO')  # write a string "GO"
        self.logger.writelog("Butten GO Gedrückt", 2)

    # Print
    def write(self, STRING):
        self.logger.writelog("Versuche String Zu übermitteln", 3)
        self.ser.write(STRING)
        self.logger.writelog("Sting " + STRING + " Konnte nicht übermittelt werden", 1)
