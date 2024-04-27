
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

BOT_USERNAME = getenv("BOT_USERNAME" , "IQMCBOT")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999999999"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "999999999999999"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

BOT_NAME = getenv("BOT_NAME", None)

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", None)

OWNER_USERNAME = getenv("OWNER_USERNAME","IQ7amo")

USER_OWNER = getenv("USER_OWNER","IQ7amo")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1818734394 833360381").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID")
ASSUSERNAME = getenv("ASSUSERNAME" , None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/iox7ssz/jdekhf893hu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MGIMT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/IQSUPP")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/IQSUPP")
OWNER_CHANNEL = getenv("OWNER_CHANNEL", "https://t.me/EHS4SS")
GROUP_BOT = int(getenv("GROUP_BOT", "-1001962701094"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", None)

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/d593c6064ff7657d0c714.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/3202937ba2792dfa8722f.jpg"

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = "https://graph.org/file/3202937ba2792dfa8722f.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/3202937ba2792dfa8722f.jpg"
STREAM_IMG_URL = "https://graph.org/file/5eb96c4141db368f17b84.jpg"

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

