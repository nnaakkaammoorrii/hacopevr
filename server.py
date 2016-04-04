import CGIHTTPServer
CGIHTTPServer.test()


import CGIHTTPServer
import SocketServer
import mimetypes

PORT = 80

Handler = CGIHTTPServer.CGIHTTPRequestHandler

Handler.extensions_map['.json']='application/json'
#Handler.extensions_map['.json']='application/json;charset=UTF-8'
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()