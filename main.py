import botpy
import config
import numpy as np
from botpy.message import Message

appid= config.Configuration.AppID()
token= config.Configuration.Token()

class BigHeadClient(botpy.Client):
    async def on_at_message_create(self,message: Message):
        await message.reply(content=f"机器人{self.robot.name}收到你的@消息了:{message.content}")


intents = botpy.Intents(public_guild_messages=True)
client = BigHeadClient(intents = intents)
client.run(appid={appid},token={token})