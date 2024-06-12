import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonXMusic.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "᠂ ⃪ᠰ⋆𓆩𔘓⃭𓆪࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 10 < anon < 20:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌𓆩𔘓⃭𓆪Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 20 <= anon < 30:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴ𓆩𔘓⃭𓆪ʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 30 <= anon < 40:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘ𓆩𔘓⃭𓆪ɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 40 <= anon < 50:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌𓆩𔘓⃭𓆪 ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 50 <= anon < 60:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀ𓆩𔘓⃭𓆪ɪ ‌୫࿁ᠰ⃪᠂"
    elif 60 <= anon < 70:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌𓆩𔘓⃭𓆪୫࿁ᠰ⃪᠂"
    elif 70 <= anon < 80:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌𓆩𔘓⃭𓆪୫࿁ᠰ⃪᠂"
    elif 80 <= anon < 95:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁𓆩𔘓⃭𓆪ᠰ⃪᠂"
    else:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂𓆩𔘓⃭𓆪"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="◧", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="★", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▣", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◯ ᴄʟᴏsᴇ ◯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "᠂ ⃪ᠰ⋆𓆩𔘓⃭𓆪࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 10 < anon < 20:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌𓆩𔘓⃭𓆪Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 20 <= anon < 30:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴ𓆩𔘓⃭𓆪ʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 30 <= anon < 40:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘ𓆩𔘓⃭𓆪ɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 40 <= anon < 50:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌𓆩𔘓⃭𓆪 ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂"
    elif 50 <= anon < 60:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀ𓆩𔘓⃭𓆪ɪ ‌୫࿁ᠰ⃪᠂"
    elif 60 <= anon < 70:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌𓆩𔘓⃭𓆪୫࿁ᠰ⃪᠂"
    elif 70 <= anon < 80:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌𓆩𔘓⃭𓆪୫࿁ᠰ⃪᠂"
    elif 80 <= anon < 95:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁𓆩𔘓⃭𓆪ᠰ⃪᠂"
    else:
        bar = "᠂ ⃪ᠰ⋆࿁୫ ‌Ƴʋ‌ᩘɤɩ‌ ‌᪳ʋ‌ᩘʀɪ ‌୫࿁ᠰ⃪᠂𓆩𔘓⃭𓆪"

    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
