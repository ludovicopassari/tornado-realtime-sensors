import asyncio
import json
import numpy as np
from tornado.websocket import websocket_connect


async def sensore(sensore_id, uri="ws://localhost:8888/sensors"):

    """
    Simulates a temperature sensor that periodically sends data to a WebSocket server.

    Parameters
    ----------
    sensore_id : str
        Unique identifier for the sensor.
    uri : str, optional
        WebSocket server URL to send data to (default: "ws://localhost:8888/sensors").

    Behavior
    --------
    - Connects the sensor to the specified WebSocket server.
    - Generates a random temperature value using a normal distribution
      with mean 25 and standard deviation 2.
    - Creates a JSON message containing:
        - sensore_id
        - data type ("temperature")
        - temperature value rounded to 2 decimals
        - current timestamp
    - Sends the message to the server every 2 seconds.
    - Handles exceptions by printing an error message.
    - Closes the WebSocket connection upon completion or error.
    """

    media = 25         # average temperature
    dev_std = 2        # standard deviation

    # connection to server WebSocket
    ws = await websocket_connect(uri)
    print(f"{sensore_id} connesso al server")

    try:
        while True:
            # sample from a normal distribution temperature value
            valore = np.random.normal(media, dev_std)
            
            # build message
            dato = {
                "sensore_id": sensore_id,
                "tipo": "temperatura",
                "valore": round(valore, 2),
                "timestamp": asyncio.get_event_loop().time()
            }
            
            # send message through WebSocket
            await ws.write_message(json.dumps(dato))
            
            # wait two seconds
            await asyncio.sleep(2)

    except Exception as e:
        print(f"{sensore_id} errore: {e}")
    finally:
        ws.close()

async def main():
    sensor_num = 10 # number of sensors
    tasks = []
    for i in range(sensor_num):
        tasks.append(sensore(f"temp_{i}"))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
