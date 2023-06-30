from discordchatbot import DiscordChatBot


class Utils:
    
    def __init__(self, client):
        self.client = client
        self.bot = DiscordChatBot()

    
    async def create_message(self, author, author_text):
        return f'```{author}: {author_text}\n{self.client.user.name}: {self.bot.send_response(author_text)}```'