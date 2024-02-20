import os
from dotenv import load_dotenv
import discord as ds
from discord.ext import commands
from discord import app_commands

# LOAD THE DISCORD TOKEN
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

def main():
    # intents are the permisions of the bot
    intents = ds.Intents.default() # default, all, none
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'User: {bot.user} (ID: {bot.user.id})')

        # config necesaria para los hybrid commands. Mira dentro del arbol de comandos de discord
        await bot.tree.sync()
            

    # Permite usar tanto los comandos de discord "/" como los comandos "!"
    @bot.hybrid_command(name="helloworld", description="Hello message", with_app_command=True)
    async def ping(ctx: commands.context):
        await ctx.send("pong")

    @bot.tree.command(canal1=True)
    async def ciao(interaction: ds.Interaction):
        await interaction.response.send_message(f'Ciao! {interaction.user.mention}',ephemeral = True)








    bot.run(TOKEN)

if __name__ == '__main__':
    main()