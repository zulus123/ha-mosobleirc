from homeassistant import config_entries
from .const import DOMAIN


class MosOblEIRCConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    MINOR_VERSION = 1