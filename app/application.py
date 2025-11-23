import tornado.web
from app.handlers.websocket_handler import EchoWebSocket

def make_app():
    return tornado.web.Application([
        (r"/sensors", EchoWebSocket),
    ])