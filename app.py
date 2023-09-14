import os  # Import the os module
import asyncio
import websockets
import random

# Get the port value from the PORT environment variable or use a default (e.g., 10000)
port = int(os.environ.get("PORT", 10000))

async def server(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            if message == "Capture":
                response = random.randint(0, 1)
                await websocket.send(str(response))
    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket connection closed")

# Use the port variable to specify the port
start_server = websockets.serve(server, "0.0.0.0", port)

async def main():
    await start_server
    await asyncio.Future()  # Keeps the server running

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
