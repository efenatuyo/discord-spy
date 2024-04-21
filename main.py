from src import websocket
import src
import asyncio
import json

async def main(config):
    sp = src.spy()
    tasks = [websocket.connect_to_gateway(sp, token) for token in config["token"]]
    await asyncio.gather(*tasks)
    
asyncio.run(main(json.loads(open("config.json", "r").read())))