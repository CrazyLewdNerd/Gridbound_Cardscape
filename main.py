TOKEN = 'MTExMjA5MjYyMzAyMTI3NzMyNA.GJbTXI.U2Bl-QsKgtgbxoHk_2TkzOJCfSomcQsHVXtxeg'
#join clash url: https://discord.com/api/oauth2/authorize?client_id=522719682659090443&permissions=0&scope=bot%20applications.commands
#join scape url: https://discord.com/api/oauth2/authorize?client_id=1112092623021277324&permissions=0&scope=bot%20applications.commands
import discord
from map import main


main()
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id != self.user.id:
            print(f'Message from {message.author}: {message.content}')
            await message.channel.send(file=discord.File('test.png'))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
