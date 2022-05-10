import codecs
codecs.register_error("strict", codecs.ignore_errors)


class LjUserCRNItem(Item):
    url = Field()
    username = Field()
    id = Field()
    actives = Field()
    archived = Field()
    private = Field()
    friends = Field()
    updates = Field()
    comments = Field()
    friendsfriends = Field()
    communities = Field()
    totalpreviews = Field()
    lastupdate = Field()
    latestpostid = Field()
    latestcommunitypostid = Field()
    latestpost_norepost = Field()
    latestcommunitypost_norepost = Field()
    lastsync = Field()
    lastscanned = Field()

    def __repr__(self):
        return '<' + self.url + '>'


class LjFriendsItem(Item):
    id = Field()
    url = Field()


class LjCommunityItem(Item):
    id = Field()
    url = Field()


class LjFriendsFriendsItem(Item):
    id = Field()
    url = Field()


class L
