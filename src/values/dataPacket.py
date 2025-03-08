import json

class DataPacket:
    NETURAL_VALUE = 2
    def __init__(self):
        self.JSON = {}
        self.THROTTLE = 0.0
        self.AILERON = 0.0
        self.RUDDER = 0.0
        self.ELEVATOR = 0.0
    
    def ToJson(self):
        """
         dacList[0].value = (uint16_t) doc["throttle"];
    dacList[1].value = (uint16_t) doc["rudder"];
    dacList[2].value = (uint16_t) doc["aileron"];
    dacList[3].value = (uint16_t) doc["elevator"];
        """
        self.JSON = {
            "throttle": self.THROTTLE,
            "rudder": self.RUDDER,
            "aileron": self.AILERON,
            "elevator": self.ELEVATOR
        }
        return json.dumps(self.JSON)