import serial
import threading
import time
from values.dataPacket import DataPacket

class Interface:
    def __init__(self,Port,Baud: int = 9600):
        print("[INFO]: Serial Connected")
        self.Port = Port
        self.Baud = Baud
        self.Lock = threading.Lock()
        self.Serial = serial.Serial(
            port=self.Port,
            baudrate=self.Baud,
            timeout=1
        )

    def SendPacket(self,Packet: DataPacket) -> None:
        with self.Lock:
            if self.Serial.out_waiting > 0:
                while self.Serial.out_waiting > 0:
                    time.sleep(0.1)
            print("[INFO]: Packet Sent")
            JSONData = Packet.ToJson()
            self.Serial.write(JSONData.encode("utf-8"))
    