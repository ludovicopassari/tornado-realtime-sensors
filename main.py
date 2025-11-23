import asyncio
from app.application import make_app

async def main():
    app = make_app()
    app.listen(8888)

    print("Server started at ws://localhost:8888")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
