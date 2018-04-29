from websocket_server import WebsocketServer
import time
import os
from make_dfs import create_geojson
from template import make_template
import json
import sys
import mercantile as m

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch
getch = _find_getch()

# code from stack shit
def byte2int(str):
	return int(str.encode('hex'), 16)

# currently defaults to top left
def zoomin(tile):
	bds = m.bounds(tile)
	return m.tile(bds.west,bds.north,tile.z+1)

def zoomout(tile):
	bds = m.bounds(tile)
	center = [(bds.west + bds.east) / 2.,(bds.north+bds.south)/2.]
	return m.tile(center[0],center[1],tile.z-1)

def centerzoom(tile):
	bds = m.bounds(tile)
	center = [(bds.west + bds.east) / 2.,(bds.north+bds.south)/2.]
	return '{"center":%s,"zoom":%s}' % (str(center),tile.z)

# structure for finding overlapping values
def overlapping_oned(box1min,box1max,box2min,box2max):
	if box1max >= box2min and box2max >= box1min:
		return True
	else:
		return False
	
	return False



# returns a boolval for whether or not the bb intersects
def intersect_bb(bdsref,bds):
	if overlapping_oned(bdsref['w'],bdsref['e'],bds['w'],bds['e']) and overlapping_oned(bdsref['s'],bdsref['n'],bds['s'],bds['n']):
		return True
	else:
		return False
	return False

# [west, south, east, north]
def mymap(x,bounds):
	x = str.split(x,',')
	if len(x) != 4:
		return False
	else:
		return intersect_bb(bounds,{'w':float(x[0]),'s':float(x[1]),'e':float(x[2]),'n':float(x[3])})

# top level class for websocket currently
class Map:

	def __init__(self):
		self.client = ''
		self.server = ''
		self.bb = {}
		self.boolval = False

		# Called for every client connecting (after handshake)
		def new_client(client, server):
			print("New client connected and was given id %d" % client['id'])
			self.client = client
			server.send_message_to_all("Hey all, a new client has joined us")


		# Called for every client disconnecting
		def client_left(client, server):
			print("Client(%d) disconnected" % client['id'])


		# Called when a client sends a message
		def message_received(client, server, message):
			if len(message) > 200:
			    message = message[:200]+'..'
			print("Client(%d) said: %s" % (client['id'], message))
			if self.boolval:
				self.boolval = False
				self.bb = json.loads(message)


		PORT=9001
		server = WebsocketServer(PORT)
		server.set_fn_new_client(new_client)
		server.set_fn_client_left(client_left)
		server.set_fn_message_received(message_received)
		server.run_forever()
		self.server = server
		make_template()
		os.system('open index.html')



	def send(self,*dfs):
		self.server.send_message(self.client,create_geojson(*dfs))
	
	def bounds(self):
		self.boolval = True
		self.server.send_message(self.client,"ping")
		
		return self.bb
	
	def clip(self,data):
		self.bounds()
		time.sleep(.1)
		return data[data.Bounds.apply(mymap,bounds=self.bb) == True]
	

	def nav(self):
		self.bounds()
		time.sleep(.1)
		bb = self.bb
		#tile = m.Tile(33,48,7)
		center = [(bb['w'] + bb['e']) / 2.0,(bb['n'] + bb['s']) / 2.0]
		tile = m.tile(center[0],center[1],5)

		boolval = True
		oldoldgetch = 0
		oldgetch = 0
		while  boolval:
			getchval = byte2int(getch())
			if getchval == 113:
				boolval = False
			if getchval == 43:
				tile = zoomin(tile)
				self.server.send_message(self.client,'ccc')
				self.server.send_message(self.client,centerzoom(tile))
				sys.stdout.write("\rTile:[X:%s,Y:%s,Z:%s]" % (tile.x,tile.y,tile.z) )
				sys.stdout.flush()
			elif getchval == 95:
				tile = zoomout(tile)
				self.server.send_message(self.client,'ccc')
				self.server.send_message(self.client,centerzoom(tile))
				sys.stdout.write("\rTile:[X:%s,Y:%s,Z:%s]" % (tile.x,tile.y,tile.z) )
				sys.stdout.flush()
			elif oldoldgetch == 27 and oldgetch == 91 and getchval == 67:
				tile = m.Tile(tile.x + 1,tile.y,tile.z)
				self.server.send_message(self.client,'ccc')
				self.server.send_message(self.client,centerzoom(tile))
				sys.stdout.write("\rTile:[X:%s,Y:%s,Z:%s]" % (tile.x,tile.y,tile.z) )
				sys.stdout.flush()
			elif oldoldgetch == 27 and oldgetch == 91 and getchval == 68:
				tile = m.Tile(tile.x - 1,tile.y,tile.z)
				self.server.send_message(self.client,'ccc')
				self.server.send_message(self.client,centerzoom(tile))
				sys.stdout.write("\rTile:[X:%s,Y:%s,Z:%s]" % (tile.x,tile.y,tile.z) )
				sys.stdout.flush()
			elif oldoldgetch == 27 and oldgetch == 91 and getchval == 66:
				tile = m.Tile(tile.x,tile.y+1,tile.z)
				self.server.send_message(self.client,'ccc')
				self.server.send_message(self.client,centerzoom(tile))
				sys.stdout.write("\rTile:[X:%s,Y:%s,Z:%s]" % (tile.x,tile.y,tile.z) )
				sys.stdout.flush()
			elif oldoldgetch == 27 and oldgetch == 91 and getchval == 65:
				tile = m.Tile(tile.x,tile.y-1,tile.z)
				self.server.send_message(self.client,'ccc')
				self.server.send_message(self.client,centerzoom(tile))
				sys.stdout.write("\rTile:[X:%s,Y:%s,Z:%s]" % (tile.x,tile.y,tile.z) )
				sys.stdout.flush()

			#print '\n',oldoldgetch,oldgetch,getchval,'\n'
			oldoldgetch = oldgetch
			oldgetch = getchval 
