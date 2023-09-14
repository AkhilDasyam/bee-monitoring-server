import asyncio
import websockets
import random

async def server(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            if message == "Capture":
                response = random.randint(0, 1)
                await websocket.send(str(response))
    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket connection closed")

start_server = websockets.serve(server, "0.0.0.0", 8080)  # Replace with your desired host and port

async def main():
    await start_server
    await asyncio.Future()  # Keeps the server running

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
