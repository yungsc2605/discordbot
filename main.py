from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.environ.get("DISCORD_TOKEN")
ROLE_NAME = "hehe"
CHANNEL_NAME = "vungoimora"
TARGET_CHANNEL = "hehe"
PASSWORD = "emyeucacanh"

active_users = set()

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    guild = message.guild
    member = message.author
    role = discord.utils.get(guild.roles, name=ROLE_NAME)

    # Nhập đúng mật khẩu ở đúng channel
    if message.channel.name == CHANNEL_NAME and message.content.strip() == f"!pass {PASSWORD}":
        if role is None:
            await message.channel.send("❌ Role 'hehe' không tồn tại.")
            return

        try:
            await member.add_roles(role)
            await message.
