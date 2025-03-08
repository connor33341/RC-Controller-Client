import serial
import serial.tools.list_ports
import time
from lib.comSearch import ComSearch
from lib.interface import Interface
from values.dataPacket import DataPacket
from lib.keyboardControl import KeyboardControl
from values.keyboardSettings import KeyboardSettings

ARDUINO_DESCRIPTION = ["arduino","ch340","ch341","ftdi","usb-serial","ttyacm1"]
BAUD_RATE = 115200
MODE = "KEYBOARD" # JOYSTICK

class Main:
    def __init__(self):
        ComSearchClass = ComSearch(ARDUINO_DESCRIPTION)
        self.Devices = ComSearchClass.Search()
        if self.Devices:
            print("[INFO]: Device Found")
        else:
            print("[ERROR]: No devices found")
            return
        
    def Connect(self):
        self.InterfaceClass = Interface(self.Devices[0],BAUD_RATE)

    def SetInital(self):
        InitalPacket = DataPacket()
        InitalPacket.THROTTLE = 0
        InitalPacket.AILERON = DataPacket.NETURAL_VALUE
        InitalPacket.ELEVATOR = DataPacket.NETURAL_VALUE
        InitalPacket.RUDDER = DataPacket.NETURAL_VALUE
        self.InterfaceClass.SendPacket(InitalPacket)
    
    def ControlMode(self):
        if MODE == "KEYBOARD":
            KeyboardControlSettings = KeyboardSettings()
            KeyboardControlClass = KeyboardControl(KeyboardControlSettings)
            KeyboardControlClass.Run(self.InterfaceClass)

if __name__ == "__main__":
    print("[INFO]: Initalized")
    MainClass = Main()
    MainClass.Connect()
    MainClass.SetInital()
    MainClass.ControlMode()