import asyncio
import discord
import requests
import logging
import msvcrt

'''
TODO:
Improve line 37's exception handler
Add voice recorder
Keyboard listener is not that good so it needs improvement
'''
# logging.basicConfig(level=logging.INFO)

class Client(discord.Client):
    async def kbfunc(self):
        x = msvcrt.kbhit()
        if x:
            ret = msvcrt.getch()
        else:
            ret = False
        return ret

    async def kb_listner(self):
        while True:
            x = await self.kbfunc()
            me = discord.utils.get(client.get_all_members(), guild__name = "da zoo", name="arex")

            if x != False and x.decode() == '-':
                print('Client logging out')
                await self.logout()

            if x != False and x.decode() == '*':
                try:
                    print('Client connected to voice or not!')
                    Voice_Client = await me.voice.channel.connect()
                except:
                    pass

            if x != False and x.decode() == 's':
                try:
                    Voice_Client.play(discord.FFmpegPCMAudio('bits/meow.mp3'))
                except:
                    pass
                Voice_Client.source = discord.PCMVolumeTransformer(Voice_Client.source)
                Voice_Client.source.volume = 1.0
                
            if x != False and x.decode() == '/':
                print('Client disconnected from voice')
                await Voice_Client.disconnect()

            await asyncio.sleep(0.1)

    async def kb_listener_loop(self):
        print('Starting listener')
        asyncio.ensure_future(self.kb_listner())

    async def on_ready(self):
        print('Logged in as {0}'.format(self.user))
        await self.kb_listener_loop()
        await self.change_presence(status=discord.Status.offline)

    async def on_message(self, message):
        if message.content.startswith('$ping'):
            await message.channel.send('pong!')

        if message.content.startswith('$lo'):
            await self.logout()


if __name__ == '__main__':
    client = Client()
    client.run('API CODE')
