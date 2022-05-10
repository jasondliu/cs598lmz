import weakref


logger = logging.getLogger(__name__)


class SeriesInfo:
    def __init__(self, url, disk_id, name, engine, manager):
        self._url = url
        self._disk_id = disk_id
        self._name = name
        self._engine = engine
        self._manager = manager

        info = self._engine.get_series_info(self._url, self._disk_id, self._name)
        # TODO Check title.
        self._title = info["title"]
        self._number_of_volumes = info["number_of_volumes"]
        self._volumes = {
            volume_id: VolumeInfo(self, volume_id=volume_id, title=volume["title"])
            for volume_id, volume in info["volumes"].items()
        }

        self._last_volume_id = self._calc_last_volume_id()

    def __str__(self):
        return "Series[{}]".format(self._title)

    def __repr__(
