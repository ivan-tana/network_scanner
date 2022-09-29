import socket
import threading
import concurrent.futures


thread_lock = threading.Lock()
def scan(ip,port,callback):
    # try a to establish a connection with the address 
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        scanner.connect((ip,port))
        scanner.close()
        with thread_lock:
            callback(port, ip)
    except:
        pass





# create a multitred process to run the scan for a range of port
def scanport(ip,callback, start,end):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start,end):
            executor.submit(scan, ip,port,callback)


