import disnake
from disnake.ext import commands
from disnake import Option, OptionType, TextInputStyle

from text_utils import Utils


class DiscordChatBotModal(disnake.ui.Modal):

    def __init__(self, client):
        components = [
            disnake.ui.TextInput(
                label='Enter message',
                placeholder='Hi, how are you?',
                custom_id='message',
                style=TextInputStyle.short,
                required=True,
            ),
        ]
        super().__init__(title='Message', components=components)
        self.client = client
        self.utils = Utils(self.client)
    

    async def callback(self, inter: disnake.ModalInteraction):
        await inter.response.defer(ephemeral=True)
        text = await self.utils.create_message(author=inter.author.name, author_text=inter.text_values['message'])
        await inter.followup.send(text, view=DiscordChatBotButton(self.client))



class DiscordChatBotButton(disnake.ui.View):

    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client
    

    @disnake.ui.button(label='Send message', style=disnake.ButtonStyle.blurple)
    async def send_message_button(self, _: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_modal(modal=DiscordChatBotModal(self.client))



class DiscordChatBotCog(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.utils = Utils(self.client)
    

    @commands.slash_command(name='ask', description='Ask chat bot',
        options=[
            Option('text', 'Text for bot', OptionType.string, required=True)
        ]
    )
    async def ask_chat_bot(self, inter: disnake.CommandInteraction, text):
        await inter.response.defer(ephemeral=True)
        text = await self.utils.create_message(author=inter.author.name, author_text=text)
        await inter.followup.send(text, view=DiscordChatBotButton(self.client))
    


def setup(client):
    client.add_cog(DiscordChatBotCog(client))
    print(f'[DEBUG] {__name__} cog loaded')