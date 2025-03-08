import time
import keyboard
from values.keyboardSettings import KeyboardSettings
from values.dataPacket import DataPacket
from lib.interface import Interface

class KeyboardControl:
    def __init__(self,Settings: KeyboardSettings):
        self.Settings = Settings
        self.Running = True
        self.Delay = Settings.Delay
        self.LastPacket: DataPacket = DataPacket()
    
    def Run(self,PacketInterface: Interface):
        while self.Running:
            Packet = DataPacket()
            Data = False
            if keyboard.is_pressed('w'):
                print("[INFO]: Increasing Throttle")
                Packet.THROTTLE = min(self.Settings.MaxValue,self.LastPacket.THROTTLE+self.Settings.Rate)
                Data = True
                #time.sleep(self.Delay)
            if keyboard.is_pressed("s"):
                print("[INFO]: Decrasing Throttle")
                Packet.THROTTLE = max(self.Settings.MinValue,self.LastPacket.THROTTLE-self.Settings.Rate)
                Data = True
                #time.sleep(self.Delay)
            if keyboard.is_pressed("z"):
                Packet.THROTTLE = 0
                Data = True
                self.Running = False
            if Data:
                #PacketInterface.SendPacket(Packet)
                PacketInterface.WriteQueue.put(Packet)
                self.LastPacket = Packet
                print(Packet.ToJson())
                time.sleep(self.Delay)