from discord import user
from discord.ext import commands
import discord
import asyncio
# from discord import Embed
# import os

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx):
    await ctx.send('Hello! <:CrumbHehe:893804991096180737>')

@bot.command()
async def timer(ctx, timeInput):
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        if time > 86400:
            await ctx.send("I can\'t do timers over a day long")
            return
        if time <= 0:
            await ctx.send("Timers don\'t go into negatives :/")
            return
        if time >= 3600:
            message = await ctx.send(f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds")
        elif time >= 60:
            message = await ctx.send(f"Timer: {time//60} minutes {time%60} seconds")
        elif time < 60:
            message = await ctx.send(f"Timer: {time} seconds")
        while True:
            try:
                await asyncio.sleep(5)
                time -= 5
                if time >= 3600:
                    await message.edit(content=f"Timer: {time//3600} hours {time %3600//60} minutes {time%60} seconds")
                elif time >= 60:
                    await message.edit(content=f"Timer: {time//60} minutes {time%60} seconds")
                elif time < 60:
                    await message.edit(content=f"Timer: {time} seconds")
                if time <= 0:
                    await message.edit(content="Ended!")
                    await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
                    break
            except:
                break
    except:
        await ctx.send(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")

'''
Command Start is still under work
'''

@bot.command()
async def Start(ctx, timeInput):
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        if time > 86400:
            await ctx.send("I can\'t do timers over a day long")
            return
        if time <= 0:
            await ctx.send("Timers don\'t go into negatives :/")
            return
        if time >= 3600:
            message = discord.Embed(title="Timer")
            # message.set_author(name=ctx.author.name, icon_url=profilePicture)
            message.add_field(name=ctx.author.name,value=f"Timer: {time//3600} hours {time%3600//60} minutes {time%60} seconds", inline=False)
            await ctx.send(embed=message)
        elif time >= 60:
            message=discord.Embed(title="Timer")
            # message.set_author(name=ctx.author.name, icon_url=profilePicture)
            message.add_field(name=ctx.author.name,value=f"Timer: {time%3600//60} minutes {time%60} seconds", inline=False)
            await ctx.send(embed=message)
        elif time < 60:
            message=discord.Embed(title="Timer")
            # message.set_author(name=ctx.author.name, icon_url=profilePicture)
            message.add_field(name=ctx.author.name,value=f"Timer: {time%60} seconds", inline=False)
            await ctx.send(embed=message)
        while True:
            try:
                await asyncio.sleep(5)
                time -= 5
                    
                if time <= 0:
                    await ctx.send(f"{ctx.author.mention} Your Timer Has ended!")
                    break
            except:
                break
    except:
        await ctx.send(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")

@bot.command()
async def avatar(ctx,  avamember : discord.Member=None):
    if not avamember: avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for `{reason}`')

bot.run('TOKEN')

# embed=discord.Embed(title="Timer")
# embed.add_field(name="undefined", value="{timer}", inline=False)
# await ctx.send(embed=embed)