# 407 status code in python

- The Proxy is connected properly in curl, node, and go, but cannot be connected properly in python. Error 407 lacks proxy-authorization
- Using wireshark, it is found that the Python proxy CONNECT request uses HTTP/1.0. The problem persists after the Connect request is forcibly changed to HTTP/1.1
- Comparing the TCP packet, it is found that the Python CONNECT request packet consists of two segments. The problem is resolved after the packet sending process is changed to one segment.