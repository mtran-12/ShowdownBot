import websockets
import json
import asyncio
import requests


class ShowdownClient:
    websocket = None
    newestMessage = None
    clientID = None
    challengeString = None
    
    async def connect(address):
        self = ShowdownClient()
        self.websocket = await websockets.connect(address)
        print('Connection successfull')
        self.newestMessage = await self.websocket.recv()
        challngStrId = await self.websocket.recv()
        challngStrId = challngStrId.split('|')
        self.clientID = challngStrId[2]
        self.challengeString = challngStrId[3]
        print(self.clientID)
        print(self.challengeString)
        return self


    def login(self, username, password, loginUri):
        response = requests.post(
            loginUri, data={
                'act': 'login',
                'name': username,
                'pass': password,
                'challstr': "|".join([self.clientID, self.challengeString])
            }
        )
        print(response)
