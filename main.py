import discord
import config
from discord.ext import commands

class MyClient(discord.Client):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.target_message_id = 1064254621536759848
    
    async def on_ready(self):
        print(f'Logged on as: {self.user}!')
        pass
        
    async def on_message(self, message):
        # print(f'Message from {message.author}: {message.content}')
        pass
    
    async def on_raw_reaction_add(self, payload):
        """ give a role based on the reaction """
        
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        
        if payload.emoji.name == '❤️':
            role = discord.utils.get(guild.roles, name = 'Любимка')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name = 'Вреднота')
            await payload.member.add_roles(role)
        
    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on reactions emoji.
        """
        
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        
        if member is not None:
            if payload.emoji.name == '❤️':
                role = discord.utils.get(guild.roles, name = 'Любимка')
                await member.remove_roles(role)
            elif payload.emoji.name == '💩':
                role = discord.utils.get(guild.roles, name = 'Вреднота')
                await member.remove_roles(role)
        else:
            print(f'{member} — {guild.get_member(payload.user_id)}\n{payload.user_id}')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run(config.BOT_TOKEN)