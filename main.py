import requests
import time
from stem import Signal
from stem.control import Controller
import nmap

def nmap_scanner(results=None):
    nm = nmap.PortScanner()
    results = nm.scan('45.33.32.158', '22')
    return results

def get_current_ip():
    session = requests.session()
    data = nmap_scanner()
    # TO Request URL with SOCKS over TOR
    session.proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
    }

    try:
        r = session.get(data)
    except Exception as e:
        print (str(e))
    else:
        return r.text


def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="TEST_PASSWORD")
        controller.signal(Signal.NEWNYM)

if __name__ == "__main__":
    for i in range(1):
        print (get_current_ip())
        renew_tor_ip()
        time.sleep(5)
