from http.server import HTTPServer, BaseHTTPRequestHandler
content='''
<html>

<title>Configuration Details of HP Laptop</title>

<body>

<table border="2" cellspacing="10" cellpadding="6">

<tr>

<caption>Configuration Details Of HP Laptop </caption>

<th>S.NO</th>

<th>Details</th>

<th>HP</th>

</tr>

<tr>

<td>1</td>

<td>Processor</td>

<td>AMDA Ryzen 5000series </td>

</tr>

<tr>

<td>2</td>

<td>Operating System</td>

<td>Windows 11</td>

</tr>

<tr>

<td>3</td>

<td>Graphics</td>

<td>AMDA Radeon Graphics</td>

</tr>

<tr>

<td>4</td>

<td>Memory</td>

<td>16GB of DDR4</td>

</tr>

<tr>

<td>5</td>

<td>Storage</td> 

<td>512 GB SSD</td>

</tr>

</body>

</html>



'''
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("My Webserver is running...")
httpd.serve_forever()