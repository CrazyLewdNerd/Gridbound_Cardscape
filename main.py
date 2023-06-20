import discord
from map import main
from TOKEN import TOKEN

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
