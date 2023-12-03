import discord

from commands import ping

class AIBot(discord.Bot):
    def __init__(self, description=None, *args, **options):
        super().__init__(description, *args, **options)

        self.add_application_command(ping)
    

