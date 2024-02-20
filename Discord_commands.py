from typing import Final
import os
from dotenv import load_dotenv
import discord as ds
from discord.ext import commands
from responses import get_response
import random 

# LOAD THE DISCORD TOKEN
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

class Slapper(commands.Converter):
    use_nicknames : bool

    def __init__(self, *, use_nicknames) -> None:
        self.use_nicknames = use_nicknames

    async def convert(self, ctx, argument):
        someone = random.choice(ctx.guild.members)
        nickname = ctx.author
        if self.use_nicknames:
            nickname = ctx.author.nick

        return f'{nickname} slaps {someone} with {argument}'

# See who send the command is the guild owner or not   
async def is_owner(ctx):
    return ctx.author.id == ctx.guild.owner_id

def main():
    # intents are the permisions of the bot
    intents = ds.Intents.default() # default, all, none
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'User: {bot.user} (ID: {bot.user.id})')

    @bot.command(
            aliases=['p'], # Agrega la opcion de usarlo con un alias
            help="This is help text",
            description="A particular description",
            brief="This is brief o descripcion corta",
            enabled=True, # Activa o desactiva el comando
            hidden=True # Se oculta o no del !help pero se puede seguir usando si esta desactivado
    )
    async def ping(ctx):
        """Ansers with pong"""
        #await ctx.send("pong")
        await ctx.message.author.send("pong")

    @bot.command()
    async def say(ctx,what = 'What?'):
        await ctx.send(what)

    @bot.command()
    async def say2(ctx,*what):
        await ctx.send(" ".join(what))

    @bot.command()
    async def say3(ctx,what = 'what?', why = 'why?'):
        await ctx.send(what + ' ' + why)

    @bot.command()
    async def choices(ctx,*option):
        await ctx.send(random.choice(option))
    
    @bot.command()
    async def slap(ctx,reason : Slapper(use_nicknames = True)):
        await ctx.send(reason)


    @bot.command()
    @commands.check(is_owner) # Only the owner of the guild can use this command
    async def joined(ctx,who : ds.Member):
        await ctx.send(who.joined_at)

    # If author isnt guild owner, bot send a message
    @joined.error
    async def joined_error(ctx, error):
        if isinstance(error,commands.CommandError):
            await ctx.send('Permision denied!')


    # Grouping commands
    @bot.group(
        brief='Group of math commands'
    )
    async def math(ctx):
        await ctx.send(f'No, {ctx.subcommand_passed} does not belong to math. Check "!help math" command.')

    @math.command()
    async def add(ctx,one : int, two : int):
        await ctx.send(one + two)

    @math.command()
    async def substring(ctx,one : int, two : int):
        await ctx.send(one - two)


    # Send an private message
    @bot.command()
    async def support(ctx):
        #await ctx.message.author.send('Hello dear!')
        user = ds.utils.get(bot.guilds[0].members, name="lautaro.delafuente")
        print(user)
        if user:
            await user.send("Hello 2")
        

    @bot.hybrid_command()
    async def ping(ctx):
        await ctx.send("pong")










    bot.run(TOKEN)

if __name__ == '__main__':
    main()