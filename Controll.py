import serial

class Controll:
    # Atribute:
    ser = ""

    # Methods:

    #Init Methode
    def __init__(self, PORT):
        self.ser = serial.Serial()   # serial port
        self.ser.baudrate = 9600     # set bautdrate
        self.ser.port = PORT     # Set PORT
        self.ser.open()          # open Port
        if not self.ser.is_open():
            print("Port is not Open")   # Check port open
            exit("Error in Controll.py")

    # Step UP Methode
    def step_up(self):
        self.ser.write(b'UP')     # write a string "UP"

    # Step DOWN Methode
    def step_down(self):
        self.ser.write(b'DOWN')     # write a string "DOWN"

    # Step FORWARD Methode
    def step_forward(self):
        self.ser.write(b'FORWARD')     # write a string "FORWARD"

    # Step BACK Methode
    def step_back(self):
        self.ser.write(b'BACK')     # write a string "BACK"

    # Print
    def write(self, STRING):
        self.ser.write(STRING)
