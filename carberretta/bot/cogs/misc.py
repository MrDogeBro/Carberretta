"""
MISCELLANEOUS

A place for commands which don't fit anywhere else.
"""

import unicodedata

import discord
from discord.ext import commands

from carberretta.utils import DEFAULT_EMBED_COLOUR


class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        if not self.bot.ready.booted:
            self.bot.ready.up(self)

    @commands.command(name="charinfo")
    async def command_charinfo(self, ctx: commands.Context, *, characters: str):
        if len(characters) > 15:
            return await ctx.send("You can only pass 15 characters at a time.")

        names = []
        points = []

        for c in characters:
            digit = f"{ord(c):x}".upper()
            name = unicodedata.name(c, "N/A")
            names.append(f"[{name}](https://fileformat.info/info/unicode/char/{digit})")
            points.append(f"U+{digit:>04}")

        embed = discord.Embed.from_dict(
            {
                "title": "Character information",
                "description": f"Displaying information on {len(characters)} character(s).",
                "color": DEFAULT_EMBED_COLOUR,
                "author": {"name": "Query"},
                "footer": {"text": f"Requested by {ctx.author.display_name}", "icon_url": f"{ctx.author.avatar_url}",},
                "fields": [
                    {"name": "Names", "value": "\n".join(names), "inline": True},
                    {"name": "Code points", "value": "\n".join(points), "inline": True},
                ],
            }
        )

        await ctx.send(embed=embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Miscellaneous(bot))
