from resource import prlimit
from scan import NetworkScanner


networkscan = NetworkScanner()

for server in networkscan.servers:
    print(server)

