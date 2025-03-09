import time
import pygame
import json
from lib.interface import Interface
from values.joystickSettings import JoystickSettings
from values.dataPacket import DataPacket

class JoystickControl:
    def __init__(self,Settings: JoystickSettings):
        self.Settings = Settings
        self.Running = True
        self.Axes = [[Settings.AILERON_AXIS,"aileron"],[Settings.ELEVATOR_AXIS,"elevator"],[Settings.RUDDER_AXIS,"rudder"],[Settings.THROTTLE_AXIS,"throttle"]]
        pygame.init()
        pygame.joystick.init()
        self.JoystickCount = pygame.joystick.get_count()
        if self.JoystickCount < 0:
            print("[INFO]: No Joysticks Detected")
            self.Running = False
        self.Joystick = pygame.joystick.Joystick(self.Settings.JOYSTICK_INDEX)
        self.Joystick.init()
        print(f"[INFO]: Axes detected: {self.Joystick.get_numaxes()}")
    def Run(self,InterfaceClass: Interface):
        self.InterfaceClass = InterfaceClass
        while self.Running:
            pygame.event.pump()
            Values = {}
            for AxisData in self.Axes:
                AxisIndex = AxisData[0]
                Key = AxisData[1]
                Value = self.Joystick.get_axis(AxisIndex)
                if Key == "throttle":
                    Value = Value * -1
                Values[Key] = Value
            #print(Values)
            NormalizedValues = {}
            for Key in Values:
                Value = Values[Key]
                Normalized = max(0,abs(min(DataPacket.MAX_VALUE,((DataPacket.MAX_VALUE-DataPacket.NETURAL_VALUE)*Value)+2.2)))
                NormalizedValues[Key] = Normalized
            print(NormalizedValues)
            Packet = DataPacket()
            Packet.FromJson(json.dumps(NormalizedValues))
            self.InterfaceClass.WriteQueue.put(Packet)
            time.sleep(self.Settings.DELAY)
                


