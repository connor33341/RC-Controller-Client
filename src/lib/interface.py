import serial
import threading
import time
import queue
from values.dataPacket import DataPacket

class Interface:
    def __init__(self,Port,Baud: int = 9600):
        print("[INFO]: Serial Connected")
        self.Port = Port
        self.Baud = Baud
        self.Lock = threading.Lock()
        self.StopEvent = threading.Event()
        self.WriteQueue = queue.Queue()
        self.Serial = serial.Serial(
            port=self.Port,
            baudrate=self.Baud,
            timeout=1
        )

    def AsyncPacketWriter(self):
        while not self.StopEvent.is_set():
            try:
                Packet: DataPacket = self.WriteQueue.get(timeout=1.0)
                self.SendPacket(Packet)
                self.WriteQueue.task_done()
                time.sleep(0.5)
            except queue.Empty:
                continue

    def SendPacket(self,Packet: DataPacket) -> None:
        with self.Lock:
            if self.Serial.out_waiting > 0:
                while self.Serial.out_waiting > 0:
                    time.sleep(0.1)
            print("[INFO]: Packet Sent")
            JSONData = Packet.ToJson()
            self.Serial.write(JSONData.encode("utf-8"))
            print(self.Serial)
            #time.sleep(0.2)
    