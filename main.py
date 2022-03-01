import socketserver
import re
import string
import socket
# import threading
import sys
import time
import logging
import sipfullproxy


HOST, PORT = '0.0.0.0', 5060

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    # ipaddress = "192.168.100.204"
    ipaddress = "192.168.43.174"  #treba zmenit IP adresu       #socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    print("Proxy server started at <%s:%s>" % (ipaddress, PORT))
    server.serve_forever()
