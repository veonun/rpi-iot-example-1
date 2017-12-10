import socket
from machine import Pin

led_pin = Pin(5, Pin.OUT)

CONTENT = """\
HTTP/1.0 200 OK
Content-Type: text/html
<html>
  <head>
     <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <p>Hello #%d from MicroPython!</p>
    <a href="/toggle">Click here to toggle LED hooked to pin 5</a>
	<div id="pinForm">
       <p class="paragraph">Choose pin value:</p>
       <input type="range" name="pinIn" class="slider" id="pinInId"   value="1" min="1" max="5" maxlength="3" oninput="pinOutId.value = pinInId.value">
       <input type="text" name="pinOut" id="pinOutId" class="out"></input>
    </div>
  </body>
</html>
"""

def main():
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://<this_host>:8080/")

    counter = 0
    while True:
        sock, addr = s.accept()
        print("Client address:", addr)
        stream = sock.makefile("rwb")
        req = stream.readline().decode("ascii")
        method, path, protocol = req.split(" ")
        print("Got", method, "request for", path)
        if path == "/toggle":
            led_pin.value(1-led_pin.value())
        while True:
            h = stream.readline().decode("ascii").strip()
            if h == "":
                break
            print("Got HTTP header:", h)
        stream.write((CONTENT % counter).encode("ascii"))
        stream.close()
        sock.close()
        counter += 1
        print()

main() # Press Ctrl-C to stop web server
