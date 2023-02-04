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
BOT_TOKEN = "6111325298:AAEN5_xubX9ivI4HGKJb4Rm5gwJK_y1s-dQ"
SESSION_STRING = "BQEPw-wAeaX7e20dHcOXwGpVH3o3cHGPcrMCrClrQ8khZQr2zfX8LxKQH0hcdMCoEU1HIO64tl6Im5PWTyya35ppucPg6MZiJoJvICWNJ2xj9MbHiMaQzCFd9scxwI2O5s1SjIGHMd0d0L6Vp_wV21XteJJlrjZoVOGNelYFGBEJacZ1LVNE9SSU8jBWb1ie3Qeckck3QDm5YELACX5eRNQKz1XOED9lyW2vLgej-ZYUvr3BVrON1UHOw5Tbnr56Ytxsr92y8a1RymlVfivYws9NGcKd5-TPc52LWECUDWHJSEoj0vfN_DQQA_n5dldswWy6wgx89XNxSt7kv96JVbEHOotQvQAAAAFEVF1_AA"
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AsmSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
SUDO_USERS = 1256202333
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
