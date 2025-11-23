import tornado.websocket

clients = set()

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        clients.add(self)
        print("WebSocket opened")

    def on_message(self, message):
        # reply all messages to all clients connected
        for client in clients:
            client.write_message(message)

    def on_close(self):
        clients.remove(self)
        print("WebSocket closed")