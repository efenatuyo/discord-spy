import ujson as json

async def receive(self, response):
    if response["op"] == 0:
        event_type = response.get("t")
        event_data = response.get("d")

        handler_mapping = {
            "GUILD_CREATE": handle_guild_event,
            "GUILD_UPDATE": handle_guild_event,
            "MESSAGE_CREATE": handle_user_event,
            "TYPING_START": handle_user_event,
            "PRESENCE_UPDATE": handle_user_event,
            "MESSAGE_UPDATE": handle_user_event,
            "MESSAGE_REACTION_ADD": handle_user_event,
            "GUILD_ROLE_UPDATE": handle_guild_event,
            "GUILD_ROLE_CREATE": handle_guild_event,
            "GUILD_ROLE_DELETE": handle_guild_event,
            "MESSAGE_DELETE": handle_user_event,
            "MESSAGE_REACTION_REMOVE": handle_user_event,
            "GUILD_BAN_ADD": handle_guild_event,
            "MESSAGE_DELETE_BULK": handle_user_event,
            "GUILD_BAN_REMOVE": handle_guild_event,
            "CONVERSATION_SUMMARY_UPDATE": handle_guild_event,
            "CHANNEL_UPDATE": handle_guild_event,
            "GUILD_MEMBER_REMOVE": handle_guild_event,
            "THREAD_LIST_SYNC": handle_guild_event
        }

        if event_type in handler_mapping:
            return await handler_mapping[event_type](self, event_data, event_type)
        
        print(response)
        
def get_or_create_key(dictionary, key, default=None):
    if key not in dictionary:
        dictionary[key] = default if default is not None else {}
    return dictionary[key]

async def handle_user_event(self, data, event_name):
    user_id = data.get("member", {}).get("user", {}).get("id") or data.get("author", {}).get("id")

    user_data = get_or_create_key(self.data, "users", {})
    user_event_data = get_or_create_key(user_data, user_id, {})
    user_event_data[event_name] = user_event_data.get(event_name, [])
    user_event_data[event_name].append(data)

    with open("data.json", "w") as file:
        json.dump(self.data, file, indent=4)

async def handle_guild_event(self, data, event_name):
    guild_id = data.get("guild_id") or data.get("id")

    guild_data = get_or_create_key(self.data, "guilds", {})
    guild_event_data = get_or_create_key(guild_data, guild_id, {})
    if event_name == "GUILD_CREATE":
        guild_event_data[event_name] = guild_event_data.get(event_name, data)
    else:
        guild_event_data[event_name] = guild_event_data.get(event_name, [])
        guild_event_data[event_name].append(data)

    with open("data.json", "w") as file:
        json.dump(self.data, file, indent=4)
