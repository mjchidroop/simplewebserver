from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to bottom, #006400, #98fb98);
      padding: 20px;
    }
    .layer {
      background: #fff;
      border: 2px solid #333;
      border-radius: 8px;
      margin: 20px auto;
      padding: 15px;
      width: 80%;
      box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .layer h2 {
      margin-top: 0;
      color: #005a9c;
    }
    .layer ul {
      list-style-type: square;
      padding-left: 20px;
    }
    .arrow {
      text-align: center;
      font-size: 24px;
      margin: -10px 0;
    }
    .signature {
      text-align: right;
      font-style: italic;
      margin-top: 40px;
    }
  </style>
</head>
<body>

  <h1 style=" text-align:center;"><i>List of Protocols in TCP/IP Protocol Suite</i></h1>

  <div class="layer">
    <h2>1. Application Layer</h2>
    <ul>
      <li>HTTP (Hypertext Transfer Protocol)</li>
      <li>HTTPS (Secure HTTP)</li>
      <li>FTP (File Transfer Protocol)</li>
      <li>SMTP (Simple Mail Transfer Protocol)</li>
      <li>POP3 (Post Office Protocol v3)</li>
      <li>IMAP (Internet Message Access Protocol)</li>
      <li>DNS (Domain Name System)</li>
      <li>Telnet</li>
      <li>SNMP (Simple Network Management Protocol)</li>
      <li>DHCP (Dynamic Host Configuration Protocol)</li>
    </ul>
  </div>

  <div class="arrow">⬇️</div>

  <div class="layer">
    <h2>2. Transport Layer</h2>
    <ul>
      <li>TCP (Transmission Control Protocol)</li>
      <li>UDP (User Datagram Protocol)</li>
    </ul>
  </div>

  <div class="arrow">⬇️</div>

  <div class="layer">
    <h2>3. Internet Layer</h2>
    <ul>
      <li>IP (Internet Protocol)</li>
      <li>ICMP (Internet Control Message Protocol)</li>
      <li>ARP (Address Resolution Protocol)</li>
      <li>RARP (Reverse Address Resolution Protocol)</li>
      <li>IGMP (Internet Group Management Protocol)</li>
    </ul>
  </div>

  <div class="arrow">⬇️</div>

  <div class="layer">
    <h2>4. Network Access Layer</h2>
    <ul>
      <li>Ethernet</li>
      <li>Wi-Fi (IEEE 802.11)</li>
      <li>PPP (Point-to-Point Protocol)</li>
      <li>SLIP (Serial Line Internet Protocol)</li>
    </ul>
  </div>

  <p class="signature">-CHIDROOP M J</p>

</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
httpd= HTTPServer(("localhost",8000),myhandler)
print("My code is running")
httpd.serve_forever()