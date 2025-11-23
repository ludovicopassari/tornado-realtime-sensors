import asyncio
import json
import numpy as np
from tornado.websocket import websocket_connect

async def sensore(sensore_id, uri="ws://localhost:8888/sensors"):
    media = 25         # temperatura media
    dev_std = 2        # deviazione standard

    # Connessione al server WebSocket
    ws = await websocket_connect(uri)
    print(f"{sensore_id} connesso al server")

    try:
        while True:
            # Genera valore casuale da distribuzione normale
            valore = np.random.normal(media, dev_std)
            
            # Crea messaggio JSON
            dato = {
                "sensore_id": sensore_id,
                "tipo": "temperatura",
                "valore": round(valore, 2),
                "timestamp": asyncio.get_event_loop().time()
            }
            
            # Invia al server
            await ws.write_message(json.dumps(dato))
            
            # Attendi 2 secondi prima del prossimo invio
            await asyncio.sleep(2)
    except Exception as e:
        print(f"{sensore_id} errore: {e}")
    finally:
        ws.close()

async def main():
    sensor_num = 10
    tasks = []
    for i in range(sensor_num):
        tasks.append(sensore(f"temp_{i}"))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
