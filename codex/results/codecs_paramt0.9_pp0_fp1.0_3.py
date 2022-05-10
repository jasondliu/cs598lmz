import codecs
codecs.register_error("PopulateData", lambda e: (u" ", e.start + 1))


class Shopbot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.shop = Shop(self.bot)
        self.stats_cache = Cache(max_size=10, default_timeout=1)

    async def load_image(self, url, extension=".png"):
        getbytes = lambda ext: await self.bot.loop.run_in_executor(None, functools.partial(get_bytes, url, ext))
        try:
            with Image.open(io.BytesIO(await getbytes())) as b:
                return b
        except Exception as e:
            logger.exception("Error loading image: %s", url, exc_info=e)
            return None

    async def get_base_stats(self, name):
        if name == "bst":
            return 718

        # Gets base stats as long as the pokemon's name is valid
        try:

            # Checks if the name is non
