import discord
import wikipedia
from discord.ext import commands
class Wiki:
	def __init__(self, bot):
		self.bot = bot

	@commands.group(invoke_without_command=True,pass_context=True)
	async def wiki(self, ctx, *, query: str):
		await ctx.message.delete()
		try:
			resultlst = wikipedia.search(query)
			item = resultlst[0]
			pg = wikipedia.page(item)
		except wikipedia.exceptions.DisambiguationError as e:
			pg = wikipedia.page(e.options[0])
		await ctx.send(pg.url)
	@wiki.command(pass_context=True)
	async def search(self, ctx, *, query: str):
		await ctx.message.delete()
		resultlst = wikipedia.search(query)
		msg = "```py\n"
		for number, option in enumerate(resultlst[:4]):
			msg += "{0}. {1}\n".format(number+1, option)
		msg += "\n\nType 'exit' to leave the menu\n```"
		menumsg = await ctx.send(msg)
		def check(m):
			return m.author == ctx.message.author and m.channel == ctx.message.channel and m.content.isdigit()
		response = await self.bot.wait_for('message',check=check)
		try:
			if response.content.lower() == 'exit':
				await response.delete()
				await menumsg.delete()
				return
			else:
				await response.delete()
				await menumsg.delete()
				item = resultlst[int(response.content)-1]
		except IndexError:
			return
		await ctx.send(wikipedia.page(item).url)
def setup(bot):
	bot.add_cog(Wiki(bot))