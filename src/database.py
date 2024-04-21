import ujson as json

async def receive(self, response):
    if response["op"] == 0:
        event_type = response.get("t")
        event_data = response.get("d")

        if event_type in ["GUILD_CREATE", "GUILD_UPDATE", "MESSAGE_CREATE", "TYPING_START",
                          "PRESENCE_UPDATE", "MESSAGE_UPDATE", "MESSAGE_REACTION_ADD",
                          "GUILD_ROLE_UPDATE", "GUILD_ROLE_CREATE", "GUILD_ROLE_DELETE",
                          "MESSAGE_DELETE", "MESSAGE_REACTION_REMOVE", "GUILD_BAN_ADD",
                          "MESSAGE_DELETE_BULK", "GUILD_BAN_REMOVE", "CONVERSATION_SUMMARY_UPDATE"]:
            handler_function = globals().get(f"{event_type.lower()}")
            if handler_function:
                await handler_function(self, event_data)
    # any unhandled event probally can ignore them
    
    print(response)

async def message_create(self, data):
    user = data["id"]
    if not self.data.get("users"):
        self.data["users"] = {user: {"MESSAGE_CREATE": data}}
    elif not self.data["users"].get(user) or not self.data["users"][user].get("MESSAGE_CREATE"):
        self.data["users"][user] = {"MESSAGE_CREATE": [data]}
    else:
        if not data in self.data["users"][user]["MESSAGE_CREATE"]:
            self.data["users"][user]["MESSAGE_CREATE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def guild_role_update(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"GUILD_ROLE_UPDATE": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("GUILD_ROLE_UPDATE"):
        self.data["guilds"][guild] = {"GUILD_ROLE_UPDATE": [data]}
    else:
        if not data in self.data["guilds"][guild]["GUILD_ROLE_UPDATE"]:
            self.data["guilds"][guild]["GUILD_ROLE_UPDATE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def conversation_summary_update(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"CONVERSATION_SUMMARY_UPDATE": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("CONVERSATION_SUMMARY_UPDATE"):
        self.data["guilds"][guild] = {"CONVERSATION_SUMMARY_UPDATE": [data]}
    else:
        if not data in self.data["guilds"][guild]["CONVERSATION_SUMMARY_UPDATE"]:
            self.data["guilds"][guild]["CONVERSATION_SUMMARY_UPDATE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))
    
async def guild_role_delete(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"GUILD_ROLE_DELETE": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("GUILD_ROLE_DELETE"):
        self.data["guilds"][guild] = {"GUILD_ROLE_DELETE": [data]}
    else:
        if not data in self.data["guilds"][guild]["GUILD_ROLE_DELETE"]:
            self.data["guilds"][guild]["GUILD_ROLE_DELETE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def message_reaction_remove(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"MESSAGE_REACTION_REMOVE": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("MESSAGE_REACTION_REMOVE"):
        self.data["guilds"][guild] = {"MESSAGE_REACTION_REMOVE": [data]}
    else:
        if not data in self.data["guilds"][guild]["MESSAGE_REACTION_REMOVE"]:
            self.data["guilds"][guild]["MESSAGE_REACTION_REMOVE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def guild_ban_revoke(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"GUILD_BAN_REMOVE": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("GUILD_BAN_REMOVE"):
        self.data["guilds"][guild] = {"GUILD_BAN_REMOVE": [data]}
    else:
        if not data in self.data["guilds"][guild]["GUILD_BAN_REMOVE"]:
            self.data["guilds"][guild]["GUILD_BAN_REMOVE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def guild_ban_add(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"GUILD_BAN_ADD": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("GUILD_BAN_ADD"):
        self.data["guilds"][guild] = {"GUILD_BAN_ADD": [data]}
    else:
        if not data in self.data["guilds"][guild]["GUILD_BAN_ADD"]:
            self.data["guilds"][guild]["GUILD_BAN_ADD"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))


async def message_delete(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"MESSAGE_DELETE": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("MESSAGE_DELETE"):
        self.data["guilds"][guild] = {"MESSAGE_DELETE": [data]}
    else:
        if not data in self.data["guilds"][guild]["MESSAGE_DELETE"]:
            self.data["guilds"][guild]["MESSAGE_DELETE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def message_delete_bulk(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"MESSAGE_DELETE_BULK": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("MESSAGE_DELETE_BULK"):
        self.data["guilds"][guild] = {"MESSAGE_DELETE_BULK": [data]}
    else:
        if not data in self.data["guilds"][guild]["MESSAGE_DELETE_BULK"]:
            self.data["guilds"][guild]["MESSAGE_DELETE_BULK"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))
    
async def guild_role_create(self, data):
    guild = data["guild_id"]
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild: {"GUILD_ROLE_CREATE": data}}
    elif not self.data["guilds"].get(guild) or not self.data["guilds"][guild].get("GUILD_ROLE_CREATE"):
        self.data["guilds"][guild] = {"GUILD_ROLE_CREATE": [data]}
    else:
        if not data in self.data["guilds"][guild]["GUILD_ROLE_CREATE"]:
            self.data["guilds"][guild]["GUILD_ROLE_CREATE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))
    
async def message_reaction_add(self, data):
    user = data["member"]["user"]["id"]
    if not self.data.get("users"):
        self.data["users"] = {user: {"MESSAGE_REACTION_ADD": data}}
    elif not self.data["users"].get(user) or not self.data["users"][user].get("MESSAGE_REACTION_ADD"):
        self.data["users"][user] = {"MESSAGE_REACTION_ADD": [data]}
    else:
        if not data in self.data["users"][user]["MESSAGE_REACTION_ADD"]:
            self.data["users"][user]["MESSAGE_REACTION_ADD"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def message_update(self, data):
    user = data["author"]["id"]
    if not self.data.get("users"):
        self.data["users"] = {user: {"MESSAGE_UPDATE": data}}
    elif not self.data["users"].get(user) or not self.data["users"][user].get("MESSAGE_UPDATE"):
        self.data["users"][user] = {"MESSAGE_UPDATE": [data]}
    else:
        if not data in self.data["users"][user]["MESSAGE_UPDATE"]:
            self.data["users"][user]["MESSAGE_UPDATE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))
    
async def typing_start(self, data):
    user = data["member"]["user"]["id"]
    if not self.data.get("users"):
        self.data["users"] = {user: {"TYPING_START": data}}
    elif not self.data["users"].get(user) or not self.data["users"][user].get("TYPING_START"):
        self.data["users"][user] = {"TYPING_START": [data]}
    else:
        if not data in self.data["users"][user]["TYPING_START"]:
            self.data["users"][user]["TYPING_START"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

async def presence_update(self, data):
    user = data["user"]["id"]
    if not self.data.get("users"):
        self.data["users"] = {user: {"PRESENCE_UPDATE": data}}
    elif not self.data["users"].get(user) or not self.data["users"][user].get("PRESENCE_UPDATE"):
        self.data["users"][user] = {"PRESENCE_UPDATE": [data]}
    else:
        if not data in self.data["users"][user]["PRESENCE_UPDATE"]:
            self.data["users"][user]["PRESENCE_UPDATE"].append(data)
        
    open("data.json", "w").write(json.dumps(self.data, indent=4))

        
async def guild_create(self, data, static=False):
    guild_id = str(data["guild_id" if not static else "id"])
    if not self.data.get("guilds"):
        self.data["guilds"] = {guild_id: {"GUILD_CREATE": data}}
    else:
        if not self.data["guilds"].get(guild_id):
            self.data["guilds"][guild_id] = {"GUILD_CREATE": data}
        else:
            self.data["guilds"][guild_id]["GUILD_CREATE"] = data
    
    open("data.json", "w").write(json.dumps(self.data, indent=4))
