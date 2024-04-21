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
            "GUILD_MEMBER_REMOVE": handle_guild_event
        }

        if event_type in handler_mapping:
            await handler_mapping[event_type](self, event_data)

def get_or_create_key(dictionary, key, default=None):
    if key not in dictionary:
        dictionary[key] = default if default is not None else {}
    return dictionary[key]

async def handle_user_event(self, data):
    user_id = data.get("member", {}).get("user", {}).get("id") or data.get("author", {}).get("id")
    event_name = data.get("_event_name")

    user_data = get_or_create_key(self.data, "users", {})
    user_event_data = get_or_create_key(user_data, user_id, {})
    user_event_data[event_name] = user_event_data.get(event_name, [])
    user_event_data[event_name].append(data)

    with open("data.json", "w") as file:
        json.dump(self.data, file, indent=4)

async def handle_guild_event(self, data):
    guild_id = data.get("guild_id") or data.get("id")
    event_name = data.get("_event_name")

    guild_data = get_or_create_key(self.data, "guilds", {})
    guild_event_data = get_or_create_key(guild_data, guild_id, {})
    guild_event_data[event_name] = guild_event_data.get(event_name, [])
    guild_event_data[event_name].append(data)

    with open("data.json", "w") as file:
        json.dump(self.data, file, indent=4)
