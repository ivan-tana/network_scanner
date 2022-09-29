import requests


def connect_server(addr: dict, check='fileserver'):
    """try to connent to the url and check if it contains a response with a key of the varaible check"""
    ip = addr['ip']
    port = addr['port']
    url = f"http://{ip}:{port}"
    try:
        responce = requests.get(url).json()
        try: 
            responce[check]
            return responce
        except:
            pass
        
    except:
        return None