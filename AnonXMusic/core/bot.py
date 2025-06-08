from pyrogram import Client
from pyrogram.enums import ParseMode

import config


class Anony(Client):
    def __init__(self):
        super().__init__(
            name="sʏᴀᴀᴀ✘ʀᴏʙᴏᴛ",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        # Logging internal via terminal (opsional)
        print(f"[✅] Bot started as {self.name} (@{self.username})")

    async def stop(self):
        await super().stop()
        print("[🛑] Bot stopped.")
