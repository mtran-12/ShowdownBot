import websockets
import json
import asyncio

class showdownClient:
    websocket = None
    username = None
    password = None
    login_uri = None


    
    async def __init__(self, username, password):
        self = PSWebsocketClient()
        self.username = username
        self.password = password
        self.websocket = await websockets.connect(wss://sim.smogon.com/showdown/websocket)
        self.login_uri = "https://play.pokemonshowdown.com/action.php"

    async def startRandomBattle(self):
