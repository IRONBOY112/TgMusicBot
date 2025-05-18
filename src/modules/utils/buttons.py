#  Copyright (c) 2025 AshokShau
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the TgMusicBot project. All rights reserved where applicable.

from pytdbot import types

from src import config

# ─────────────────────
# Inline Button Definitions
# ─────────────────────

SKIP_BTN = types.InlineKeyboardButton(
    text="‣‣I", type=types.InlineKeyboardButtonTypeCallback(b"play_skip")
)

STOP_BTN = types.InlineKeyboardButton(
    text="▢", type=types.InlineKeyboardButtonTypeCallback(b"play_stop")
)

PAUSE_BTN = types.InlineKeyboardButton(
    text="II", type=types.InlineKeyboardButtonTypeCallback(b"play_pause")
)

RESUME_BTN = types.InlineKeyboardButton(
    text="▷", type=types.InlineKeyboardButtonTypeCallback(b"play_resume")
)

CLOSE_BTN = types.InlineKeyboardButton(
    text="ᴄʟᴏsᴇ", type=types.InlineKeyboardButtonTypeCallback(b"play_close")
)

CHANNEL_BTN = types.InlineKeyboardButton(
    text="✿ ᴄʜᴀɴɴᴇʟ ✿", type=types.InlineKeyboardButtonTypeUrl(config.SUPPORT_CHANNEL)
)

GROUP_BTN = types.InlineKeyboardButton(
    text="✇ sᴜᴘᴘᴏʀᴛ ✇", type=types.InlineKeyboardButtonTypeUrl(config.SUPPORT_GROUP)
)

SOURCE_BTN = types.InlineKeyboardButton(
    text="❖ sᴏᴜʀᴄᴇ ❖", type=types.InlineKeyboardButtonTypeCallback(b"source")
)

DEVELOPER_BTN = types.InlineKeyboardButton(
    text="✫ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✫", type=types.InlineKeyboardButtonTypeUrl("https://t.me/Ironmanhindigaming")
)

HELP_BTN = types.InlineKeyboardButton(
    text="♪ ᴄᴏᴍᴍᴀɴᴅs ♪", type=types.InlineKeyboardButtonTypeCallback(b"help_all")
)

BACK_BTN = types.InlineKeyboardButton(
    text="⬅ ʙᴀᴄᴋ", type=types.InlineKeyboardButtonTypeCallback(b"back_to_start")
)

USER_BTN = types.InlineKeyboardButton(
    text="♪ ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs ♪", type=types.InlineKeyboardButtonTypeCallback(b"help_user")
)

ADMIN_BTN = types.InlineKeyboardButton(
    text="❖ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ❖", type=types.InlineKeyboardButtonTypeCallback(b"help_admin")
)

OWNER_BTN = types.InlineKeyboardButton(
    text="✇ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅs ✇", type=types.InlineKeyboardButtonTypeCallback(b"help_owner")
)

DEVS_BTN = types.InlineKeyboardButton(
    text="✧ ᴅᴇᴠs ᴄᴏᴍᴍᴀɴᴅs ✧", type=types.InlineKeyboardButtonTypeCallback(b"help_devs")
)

# ─────────────────────
# Inline Keyboard Markups
# ─────────────────────

PlayButton = types.ReplyMarkupInlineKeyboard(
    [[SKIP_BTN, STOP_BTN, PAUSE_BTN, RESUME_BTN], [CLOSE_BTN]]
)

PauseButton = types.ReplyMarkupInlineKeyboard(
    [[SKIP_BTN, STOP_BTN, RESUME_BTN], [CLOSE_BTN]]
)

ResumeButton = types.ReplyMarkupInlineKeyboard(
    [[SKIP_BTN, STOP_BTN, PAUSE_BTN], [CLOSE_BTN]]
)

SupportButton = types.ReplyMarkupInlineKeyboard(
    [[CHANNEL_BTN], [GROUP_BTN]]
)

StartMenu = types.ReplyMarkupInlineKeyboard(
    [[CHANNEL_BTN], [GROUP_BTN], [SOURCE_BTN], [DEVELOPER_BTN], [HELP_BTN]]
)

SourceMenu = types.ReplyMarkupInlineKeyboard([[BACK_BTN]])

HelpMenu = types.ReplyMarkupInlineKeyboard(
    [[USER_BTN, ADMIN_BTN], [OWNER_BTN, DEVS_BTN], [CLOSE_BTN]]
)

BackHelpMenu = types.ReplyMarkupInlineKeyboard([[HELP_BTN, CLOSE_BTN]])

# ─────────────────────
# Dynamic Keyboard Generator
# ─────────────────────

def add_me_markup(username: str) -> types.ReplyMarkupInlineKeyboard:
    """
    Returns an inline keyboard with a button to add the bot to a group
    and support buttons.
    """
    return types.ReplyMarkupInlineKeyboard(
        [
            [
                types.InlineKeyboardButton(
                    text="✦ ᴋɪᴅɴᴀᴘ ᴍᴇ ✦",
                    type=types.InlineKeyboardButtonTypeUrl(
                        f"https://t.me/{username}?startgroup=true"
                    ),
                ),
            ],
            [CHANNEL_BTN],
            [GROUP_BTN],
            [SOURCE_BTN],
            [DEVELOPER_BTN],
            [HELP_BTN],
        ]
    )
