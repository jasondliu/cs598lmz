import codecs
codecs.decode("")

# This method will delete any expired pandas and do an update on any pandas that have an invaid name.
async def get_pandas_data(self, panda_id):
    try:
        httpRequest = requests.get("https://thepandainfoapi.herokuapp.com/getpanda", dict(pandaid=panda_id), timeout=10)
        jsonResponse = json.loads(httpRequest.text)
    except:
        query = "select * from pandas where pandaid=%s;"
        result = await self.db_pool.fetchrow(query, panda_id)
        if result:
            await asyncio.sleep(90)
        return result['id'], result['name'], result['is_expired'], result

    if jsonResponse['isExpired'] == "":
        query = "select * from pandas where pandaid=%s;"
        result = await self.db_pool.fetchrow(query, panda_id)
        if len(jsonResponse['name']) >
