from main import bot


class TextUtils:
    
    def __init__(self, client):
        self.client = client

    
    async def create_message(self, author, author_text: str) -> str:
        return f'```{author}: {author_text}\n{self.client.user.name}: {bot.send_response(author_text)}```'