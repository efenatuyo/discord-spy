import websockets
import json
import time
import asyncio
from . import database
        
async def lazy_guild_loading(websocket, guild_id):
    try:
        request_payload = {
            'op': 14,
            'd': {
                'guild_id': guild_id,
                "presences": True,
                "typing": True,
                "voiceStates": True,
                "activities": True,
                "emojis": True,
                'roles': True,
                'guildMembers': True,
                'threads': True,
                'integrations': True,
                'webhooks': True,
                'invites': True,
            }
        }
        await websocket.send(json.dumps(request_payload))
        print(f"Lazy guild loading initiated for guild ID: {guild_id}")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"WebSocket connection closed unexpectedly: {e}")
        
async def connect_to_gateway(self, token):
    try:
        last_heartbeat_time = time.time()
        async with websockets.connect('wss://gateway.discord.gg/?v=9&encoding=json', max_size=None) as websocket:
            identify_payload = {'op': 2, 'd': {'token': token, 'properties': {'$os': 'linux', '$browser': 'my_custom_bot', '$device': 'my_custom_bot'}}}
            await websocket.send(json.dumps(identify_payload))
            heartbeat_interval = json.loads(await websocket.recv())['d']['heartbeat_interval'] / 2

            guilds_response = await websocket.recv()
            guilds_data = json.loads(guilds_response)
            for guild in guilds_data['d']['guilds']:
                await database.guild_create(self, guild, True)
            guild_ids = [str(guild['id']) for guild in guilds_data['d']['guilds']]
            print(f"Bot is connected to guilds: {guild_ids}")
            
            for guild_id in guild_ids:
                await lazy_guild_loading(websocket, guild_id)
            while True:
                try:
                    current_time = time.time()
                    time_since_last_heartbeat = current_time - last_heartbeat_time
                    if time_since_last_heartbeat >= heartbeat_interval / 1000:
                        heartbeat_payload = {'op': 1, 'd': int(time.time() * 1000)}
                        await websocket.send(json.dumps(heartbeat_payload))
                        last_heartbeat_time = current_time
                        print("Heartbeat sent")
                    message = await websocket.recv()
                    data = json.loads(message)
                    if data.get("op") == 1:
                        heartbeat_payload = {'op': 1, 'd': int(time.time() * 1000)}
                        await websocket.send(json.dumps(heartbeat_payload))
                        print("Heartbeat sent")
                    await asyncio.create_task(database.receive(self, data))
                except:
                    pass

    except websockets.exceptions.ConnectionClosed as e:
        print(f"WebSocket connection closed unexpectedly: {e}")
