# buttons.py
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
    text="CHANNEL", type=types.InlineKeyboardButtonTypeUrl(config.SUPPORT_CHANNEL)
)

GROUP_BTN = types.InlineKeyboardButton(
    text="SUPPORT", type=types.InlineKeyboardButtonTypeUrl(config.SUPPORT_GROUP)
)

HELP_BTN = types.InlineKeyboardButton(
    text="HELP & COMMANDS", type=types.InlineKeyboardButtonTypeCallback(b"help_all")
)

USER_BTN = types.InlineKeyboardButton(
    text="User Commands", type=types.InlineKeyboardButtonTypeCallback(b"help_user")
)

ADMIN_BTN = types.InlineKeyboardButton(
    text="Admin Commands", type=types.InlineKeyboardButtonTypeCallback(b"help_admin")
)

OWNER_BTN = types.InlineKeyboardButton(
    text="Owner Commands", type=types.InlineKeyboardButtonTypeCallback(b"help_owner")
)

DEVS_BTN = types.InlineKeyboardButton(
    text="Devs Commands", type=types.InlineKeyboardButtonTypeCallback(b"help_devs")
)

SOURCE_BTN = types.InlineKeyboardButton(
    text="SOURCE", type=types.InlineKeyboardButtonTypeUrl("https://github.com/")
)

DEVELOPER_BTN = types.InlineKeyboardButton(
    text="DEVELOPER", type=types.InlineKeyboardButtonTypeUrl("https://t.me/Ironmanhindigaming")
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

SupportButton = types.ReplyMarkupInlineKeyboard([[CHANNEL_BTN, GROUP_BTN], [CLOSE_BTN]])

HelpMenu = types.ReplyMarkupInlineKeyboard(
    [[USER_BTN, ADMIN_BTN], [OWNER_BTN, DEVS_BTN], [CLOSE_BTN]]
)

BackHelpMenu = types.ReplyMarkupInlineKeyboard([[HELP_BTN, CLOSE_BTN]])

# ─────────────────────
# Dynamic Keyboard Generator
# ─────────────────────


def add_me_markup(username: str) -> types.ReplyMarkupInlineKeyboard:
    """
    Returns an inline keyboard with buttons matching the IRO MUSIC bot's layout:
    - ADD ME TO YOUR GROUP
    - HELP & COMMANDS | CHANNEL
    - SUPPORT | SOURCE
    - DEVELOPER
    """
    return types.ReplyMarkupInlineKeyboard(
        [
            [
                types.InlineKeyboardButton(
                    text="ADD ME TO YOUR GROUP",
                    type=types.InlineKeyboardButtonTypeUrl(
                        f"https://t.me/{username}?startgroup=true"
                    ),
                ),
            ],
            [HELP_BTN, CHANNEL_BTN],
            [GROUP_BTN, SOURCE_BTN],
            [DEVELOPER_BTN],
        ]
    )