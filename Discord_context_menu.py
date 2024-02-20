import os
from dotenv import load_dotenv
import discord as ds
from discord.ext import commands
from discord import app_commands
from datetime import date

# LOAD THE DISCORD TOKEN
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

def main():
    # intents are the permisions of the bot
    intents = ds.Intents.all() # default, all, none

    bot = commands.Bot(command_prefix='!', intents=intents)


    @bot.event
    async def on_ready():
        print(f'User: {bot.user} (ID: {bot.user.id}) - {bot.guilds[0].id}')

        guild_id = ds.Object(id=int(bot.guilds[0].id))

        #await bot.user.edit(username='Wapubot')

        # config necesaria para los hybrid commands. Mira dentro del arbol de comandos de discord
        bot.tree.copy_global_to(guild=guild_id)
        await bot.tree.sync(guild=guild_id)
            

    @bot.tree.context_menu(name='Show join date')
    async def get_joined_date(interaction: ds.Interaction, member: ds.Member):
        await interaction.response.send_message(f'Member joined: {member.joined_at}',ephemeral = True)

    
    @bot.command()
    async def rename(ctx,name):
        await bot.user.edit(username=name)





    bot.run(TOKEN)

if __name__ == '__main__':
    main()