from websocket_server import WebsocketServer
import time
import os
from make_dfs import create_geojson
from template import make_template


# top level class for websocket currently
class Map:

	def __init__(self):
		self.client = ''
		self.server = ''

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
