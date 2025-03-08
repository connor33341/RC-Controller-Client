import serial
import serial.tools.list_ports

class ComSearch:
    def __init__(self,Search):
        self.Ports = serial.tools.list_ports.comports()
        self.SearchQuery = Search
        self.Found = []
    def Search(self):
        for Port in self.Ports:
            PortDescription = Port.description.lower()
            print(f"[INFO]: Found Port: {Port.device} Description: {PortDescription}")
            for Identifer in self.SearchQuery:
                if Identifer == PortDescription:
                    Port = Port.device
                    self.Found.append(Port)
        return self.Found