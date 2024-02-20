from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, AppInfo, 
from discord.ext import commands
from responses import get_response

# LOAD THE DISCORD TOKEN
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

# BOT SET UP 
intents: Intents = Intents.all()
intents.message_content = True # NOQA
client: Client = Client(intents = intents)

appinfo = AppInfo(state=)

print(appinfo)
#print(client)

# MESSAGE FUNTIONALITY
async def send_message(message: Message, user_message:str) -> None:
    if not user_message:
        print('Message was empty because intents were not enable probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        print(response)
        print(message.channel)
        print(message)
        if is_private:
            await message.author.send(response) 
        else:
            await message.channel.send(response)

    except Exception as e:
        print(f'Error al enviar mensage: {e}')


# HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

# HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()