import codecs
codecs.register_error('skip', lambda error: ('', error.end))

class BadWords(Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        async with aiosqlite.connect('bad_words.db') as db:
            cursor = await db.cursor()
            cursor.execute("SELECT * FROM BA")
            bad_words = cursor.fetchall()
            mess = message.content
            mess = mess.lower()
            bad_words = [word[0] for word in bad_words]
            for bad_word in bad_words:
                mess = mess.replace(bad_word, "*"*len(bad_word))
            await db.commit()
            await message.edit(content=mess)
            
def setup(bot):
    bot.add_cog(BadWords(bot))
