import discord
from discord.ext import commands


class Base:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pingpong'])
    async def ping(self, ctx):
        await ctx.message.delete()
        pingtime = self.bot.latency * 1000
        pingtimerounded = int(pingtime)
        totalstring = str(pingtimerounded) + 'ms'
        emb = discord.Embed(title='\U0001f3d3 Pong ' +
                            totalstring, colour=self.bot.embed_colour)
        await ctx.send(embed=emb)

    @commands.command(aliases=['emb'])
    async def embed(self, ctx, *, message: str = None):
        if message == None:
            await ctx.message.delete()
            await ctx.send(":x: You need a message to embed")
        else:
            await ctx.message.delete()
            emb = discord.Embed(title=message, colour=self.bot.embed_colour)
            await ctx.send(embed=emb)

    @commands.command(aliases=['status'])
    async def presence(self, ctx, mode, *, message: str = None):

        change = 1

        if message == None:
            change = 0
            emb = discord.Embed(colour=self.bot.embed_colour)
            emb.add_field(name='Options',
                          value='Stream, Online, Idle, DND or Invis')
            await ctx.send(embed=emb)

        else:
            if mode.lower() == "stream" or mode.lower() == "twitch":
                await self.bot.change_presence(status=discord.Status.online, game=discord.Game(name=message, type=1, url="https://www.twitch.tv/{}".format(message)), afk=True)
                colour = self.bot.colors.purple
                status = "Stream"
            elif mode.lower() == "online" or mode.lower() == "on":
                await self.bot.change_presence(status=discord.Status.online, game=discord.Game(name=message), afk=True)
                colour = self.bot.colors.lightgreen
                status = "Online"
            elif mode.lower() == "idle":
                await self.bot.change_presence(status=discord.Status.idle, game=discord.Game(name=message), afk=True)
                colour = self.bot.colors.orange
                status = "Idle"
            elif mode.lower() == "dnd" or mode.lower() == "disturb" or mode.lower() == "donotdisturb":
                await self.bot.change_presence(status=discord.Status.dnd, game=discord.Game(name=message), afk=True)
                colour = self.bot.colors.red
                status = "Do Not Disturb"
            elif mode.lower() == "invisible" or mode.lower() == "invis":
                await self.bot.change_presence(status=discord.Status.invisible, game=discord.Game(name=message), afk=True)
                colour = self.bot.colors.grey
                status = "Invisible"
            else:
                change = 0
                emb = discord.Embed(colour=self.bot.embed_colour)
                emb.add_field(name='Options',
                              value='Stream, Online, Idle, DND or Invis')
                await ctx.send(embed=emb)

        if change == 1:
            emb = discord.Embed(colour=colour)
            emb.add_field(name='Status', value=status, inline=False)
            emb.add_field(name='Message', value=message, inline=False)
            await ctx.send(embed=emb)
        else:
            pass


def setup(bot):
    bot.add_cog(Base(bot))
