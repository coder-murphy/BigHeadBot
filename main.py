import botpy
import config
from botpy.types.message import Message

appid= config.Configuration.AppID()
token= config.Configuration.Token()

class BigHeadClient(botpy.client):
    async def on_at_message_create(self,message: Message):
        await self.api.post_message(channel_id = message.channel_id,content="content")


intents = botpy.Intents(public_guild_message=True)
client = BigHeadClient(intents = intents)
client.run(appid={appid},token={token})