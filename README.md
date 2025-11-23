# Tornado-realtime-sensors

**Tornado Sensor Simulator** is a Python project using **Tornado** and **WebSocket** to simulate multiple sensors sending real-time temperature data.  
The server is fully asynchronous using **asyncio**, supports multiple clients, and provides a modular and scalable architecture suitable for learning or prototyping **IoT** and **real-time data streaming applications**.

---

## Features

- Asynchronous Tornado server using **asyncio**
- WebSocket support for real-time connections
- Simulation of multiple sensors sending temperature data
- Robust error handling and connection logging
- Modular project structure:
  - `handlers/` → WebSocket Tornado handlers
  - `services/` → sensor logic
  - `application.py` → app routing and configuration
- Easily extendable for other sensor types or business logic

---

## Run

Install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac



