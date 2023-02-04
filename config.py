"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = 17810412
API_HASH = "bd9cd7df354fb74e2f9ec88f6ee4de48"
BOT_TOKEN = "6091664906:AAE3iilpn9c12MWOZVYTTc6UOvd_x9K77Fc"
SESSION_STRING = "BQEPw-wAhPJrzyT0icCCC50oa0DWoGgozY6vVjgTzfHAfi5YhS-pLKF1dexSUMHEkjI49NRA6leCs0OulbC5M2VdUU3JHk1IRWpxMU0ZJsjDBNK-pJoo_Y_dOOfGyBQt_i93-4vcXK3T-JEdSrY8vWFwcdZil88DAn5C0KL4qxoBbT25XFujz0liIUF-SkvGyaB2pKfsyp3aAIGhLnqOBbCM4yFMYMOsiluHLjjv3FJeaJ375IzAzB6bZpD_ysfp7fKwBuPrcyoWuXPoQAsYzKgbBYypyGgWFLIDLHABGEDM4oODT3KA0f5pHqQ6HcwMUIsmKClFq1AkDjgxmYrHDk9cel2OggAAAAFEVF1_AA"
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AsmSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
SUDO_USERS = 1256202333
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
