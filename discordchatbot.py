from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class DiscordChatBot:
    
    def __init__(self, name: str='ChatBot'):
        self.chatbot = ChatBot(name)
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trainer.train('chatterbot.corpus.english')

    
    def send_response(self, content: str) -> str:
        return self.chatbot.get_response(content)
