from tornado.websocket import websocket_connect
import asyncio


uri="ws://localhost:8888/sensors"

async def main():
    ws = await websocket_connect(uri)
    while True:
        

        str = await ws.read_message()
        print(str)

if __name__ == "__main__":
    asyncio.run(main())
