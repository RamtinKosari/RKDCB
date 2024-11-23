from discord.ext import commands, tasks
from datetime import timezone, datetime
from discord import Embed
import subprocess
import threading
import datetime
import requests
import aioredis
import asyncio
import discord
import random
import redis
import time
import fitz
import os

# - Warning Terminal Output
WARNING = f'\033[38;2;255;255;0m[WARNING]\033[0m'
# - Success Terminal Output
SUCCESS = f'\033[38;2;0;255;0m[SUCCESS]\033[0m'
# - Failed Terminal Output
FAILED = f'\033[38;2;255;0;0m[FAILED]\033[0m'
# - RKDCB Terminal Output
DR = f'\033[38;2;129;195;166m[RKDCB]\033[0m'
# - Log Terminal Output
LOG = f'\033[38;2;153;153;153m[LOG]\033[0m'
# - Receive Color
RECEIVE_COLOR = f'\033[38;2;117;124;154m'
# - Sent Color
SENT_COLOR = f'\033[38;2;128;154;170m'
# - Info Color
INFO = f'\033[38;2;202;207;210m'
# - Error Color
ERR = f'\033[38;2;255;200;0m'
# - Reset Color
RESET = f'\033[0m'
# - Tab
TAB = "  "

# - Failure Responses
FAILURE_RESPONSES = [
    "I apologize, but I'm currently experiencing difficulties in responding. Please try again later.",
    "Uh-oh! It seems I'm having some trouble responding at the moment. Please give me another shot later.",
    "Oops! My responses are acting up right now. Can you try reaching out to me again later?",
    "Sorry, there's a hiccup in my responses. Please be patient and try sending your message again later.",
    "Oh dear! It looks like I'm having trouble generating responses right now. Try contacting me in a bit.",
    "My apologies! Something's gone wrong with my responses. Try reaching out to me again later, please.",
    "Yikes! Responding is a bit challenging for me right now. Can you try sending your message later?",
    "Oh No! I am having Trouble to Respond to Your Message. Please Try Again Later."
]