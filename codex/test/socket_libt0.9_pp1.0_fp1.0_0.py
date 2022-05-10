import socket
from urllib.parse import urlparse
import confignew


def get_valid_wav(hass):
    wav = config.get("wavfile", None)

    if wav:
        wav = "{}{}".format(hass.config.path(), wav)

    return wav


def extract_entity_ids(hass, entity_ids):
    """ Extract a list of valid entity ids. """
    entity_id = []
    if entity_ids == 'all':
        entity_id.extend(entity.entity_id for entity in hass.states.all())
    else:
        entity_id.extend(entity.entity_id for entity in hass.states.all() if entity.entity_id in entity_ids)

    return entity_id


def killpid(pid):
    try:
        pid = int(pid)
    except:
        return False
    if pid == 0:
        return True
