import disnake
from disnake.ext import commands

import os
import time

from config import settings
from discordchatbot import DiscordChatBot

from dotenv import load_dotenv

load_dotenv()


bot = DiscordChatBot()
start_time = time.time()
client = commands.Bot(command_prefix='.', intents=disnake.Intents.all())


@client.event
async def on_ready():
    print(f'\n{client.user.name} ready!\nPing: {round(client.latency * 1000)} ms | Guilds: {len(client.guilds)} | Users: {len(client.users)}')
    client.remove_command('help')


@client.command(name='reload')
async def reload_cogs(inter: disnake.CommandInteraction):
	if inter.author.id == settings['OWNER_ID']:
		try:
			start_time = round(time.time(), 4)

			for filename in os.listdir('./cogs'):
				if filename.endswith('.py'):
					client.reload_extension(f'cogs.{filename[:-3]}')
			
			end_time = round(time.time(), 4)
			await inter.reply(embed=disnake.Embed(title='Cogs successfuly reloaded!', color=settings['COLOR']).set_footer(text=f'Response time: {round((end_time - start_time) * 1000)} ms')) 
			print('[RELOAD] Cogs successfuly reloaded')
		except Exception as e:
			await inter.reply(embed=disnake.Embed(title='Reload error', description=f'```py\n{e}\n```', color=disnake.Color.red()))
			print(f'[ERROR] {__name__}: {e}')
	else:
		await inter.reply(embed=disnake.Embed(title=":x: Error :x:", description="You are not an admin!", color=disnake.Color.red()), ephemeral=True)



class Loader:
	# unload cogs
	def unload_cogs(self):
		try:
			for filename in os.listdir('./cogs'):
				if filename.endswith('.py'):
					client.unload_extension(f'cogs.{filename[:-3]}')	
			print('[UNLOAD] Cogs unloaded')
		except Exception as e:
			print(f'[ERROR] {__name__}: {e}')

	# load cogs
	def load_cogs(self):
		try:
			for filename in os.listdir('cogs'):
				if filename.endswith('.py'):
					client.load_extension(f'cogs.{filename[:-3]}')
			print('[LOAD] Cogs loaded')
		except Exception as e:
			print(f'[ERROR] {__name__}: {e}')
			


if __name__ == '__main__':
    Loader().load_cogs()
    try:
        client.run(os.getenv('TOKEN'))
    except Exception as e:
        print(f'[ERROR] {__name__}: {e}')