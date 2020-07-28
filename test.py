import websockets
import json
import asyncio
import logging
# logger = logging.getLogger(__name__)

print('hello World')
logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

# websocket = await websockets.connect('ws://sim.smogon.com:8000/showdown/websocket')
# print('Connection successful')
# while True:
#     message = await websocket.recv()
#     print(message)
#     print("<< {}".format(message))

async def test():
    async with websockets.connect('ws://sim.smogon.com:8000/showdown/websocket') as websocket:
        print('Connection successful')
        message = await websocket.recv()
        print(message)
        print("<< {}".format(message))

asyncio.get_event_loop().run_until_complete(test())