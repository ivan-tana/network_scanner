
import socket
import asyncio
import platform
from .async_shell_command import networkDevices
from .scan_port import scanport
from .send_request import connect_server


class NetworkScanner:
    def __init__(self):
        self.start_port = 5000
        self.end_port = 5100
        self._devices = []
        self.check = 'type'
        self.devices = self.scannet()
        self.openport = []
        self.servers = []


        self.Scanport()
        self.ConnectServer()

        
        


    def scannet(self):
        """scan the network for all the connented devices"""
        asyncio.run(networkDevices(self.success, self.failed))
        return self._devices
    

    def Scanport(self):
        """scan the post provide for and open port """
        for device in self.devices:
            scanport(device, self._openport,self.start_port,self.end_port)
           
    def _openport(self, port,ip):
        self.openport.append({"ip":ip, "port":port})

    
    def ConnectServer(self):
        for addr in self.openport:
            connenected = connect_server(addr,self.check)
            if connenected:
                data = {
                    "name":connenected['name'],
                    "url":f"http://{addr['ip']}:{addr['port']}"
                }
                self.servers.append(data)

    def success(self, out,ip):
        self._devices.append(ip)
    def failed(self, err, ip):
        pass



