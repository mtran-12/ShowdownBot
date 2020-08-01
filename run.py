import logging
import asyncio
import environment
from environs import Env

from IOProcesses.ShowdownClient import ShowdownClient

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())



def parseEnv():
    env = Env()
    env.read_env()

    #required variables with casts
    environment.address = env("ADDRESS")
    environment.loginUri = env("LOGIN_URI")
    environment.username = env("USERNAME")
    environment.password = env("PASSWORD")



async def runShowdown():
    parseEnv()
    client = await ShowdownClient.connect(environment.address)
    client.login(environment.username, environment.password, environment.loginUri)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(runShowdown())