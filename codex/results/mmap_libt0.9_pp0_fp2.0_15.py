import mmap
import random
import re
import os

__all__ = ["edid", "parse", "DID", "Feature", "Descriptor", "Extension", "MonitorID", "SerialNumber", "DisplayName",
           "DisplaySerial", "DisplayProductCode", "DisplayColorInfo", "DisplayCharacteristics", "DisplayRange",
           "DisplayID", "DisplayInterfaceConnection", "DisplayInterfaceData", "DisplayVideoData", "DisplayMisc",
           "DisplayAdditionalData", "DisplayTimings", "DisplayDescriptor", "BlockDescriptor", "DataBlock",
           "vendor_data_from_edid_raw", "display_from_edid_raw", "display_from_edid",
           "_unpack_color_characteristics", "_unpack_descriptors", "TPI_EDID_OVERRIDES", "BlockType", "DataType",
           "DisplayDetail", "DisplayData", "DisplayTiming", "DisplayMode", "DisplayModes", "GenerateEISAID",
           "GenerateMonitorID", "BaseEDIDV2", "BaseEDIDV2Vesa
