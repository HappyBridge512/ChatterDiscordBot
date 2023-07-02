import disnake
from disnake.ext import commands

from discordchatbot import DiscordChatBot


class Events(commands.Cog):
     
    def __init__(self, client):
        self.client = client
        self.bot = DiscordChatBot()
        

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.bot:
            return
        
        if self.client.user in message.mentions:
            await self.message_sender(message)
            print('[INFO] Mention message bot')
            return

        if message.reference and message.reference.cached_message and message.reference.cached_message.author == self.client.user:
            original_message = await message.channel.fetch_message(message.reference.message_id)
            if original_message.author == self.client.user:
                await self.message_sender(message)
                print(f'[INFO] Bot message replied by {message.author.name}')
                return
    

    async def message_sender(self, message: disnake.Message):
        clean_content = message.clean_content
        await message.channel.send(self.bot.send_response(clean_content))
        



def setup(client):
    client.add_cog(Events(client))
    print(f'[DEBUG] {__name__} cog loaded')