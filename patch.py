# -*- coding: utf-8 -*-
# @Time    : 10/7/23 8:00 PM
# @Author  : stdchi

import http.client

def _tunnel(self):
    connect_str = "CONNECT %s:%d HTTP/1.0\r\n" % (self._tunnel_host, self._tunnel_port)
    connect_bytes = connect_str.encode("ascii")
    header_bytes = b''
    for header, value in self._tunnel_headers.items():
        header_str = "%s: %s\r\n" % (header, value)
        header_bytes += header_str.encode("latin-1")
    send_bytes = connect_bytes + header_bytes + b'\r\n'
    self.send(send_bytes)

    response = self.response_class(self.sock, method=self._method)
    (version, code, message) = response._read_status()

    if code != http.HTTPStatus.OK:
        self.close()
        raise OSError("Tunnel connection failed: %d %s" % (code,
                                                           message.strip()))
    _MAXLINE = 65536
    _MAXHEADERS = 100
    while True:
        line = response.fp.readline(_MAXLINE + 1)
        if len(line) > _MAXLINE:
            raise http.client.LineTooLong("header line")
            pass
        if not line:
            # for sites which EOF without sending a trailer
            break
        if line in (b'\r\n', b'\n', b''):
            break

        if self.debuglevel > 0:
            print('header:', line.decode())

http.client.HTTPConnection._tunnel = _tunnel