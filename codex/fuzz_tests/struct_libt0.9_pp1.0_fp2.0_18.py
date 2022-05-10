import _struct

from .wdl_cut import blit_wdl_8


class WDLCut(PluginBase):
    def build_config(self, config):
        config.add_section("WDLCut")
        config.set("WDLCut", "wdl_cut", "0", "Use 8/9-bit WDL cut algorithm")

    def build_parser(self, parser):
        parser.add_argument("--wdl-cut-threshold", type=int,
                            help="WDL cut threshold")

        # for compatibility reasons
        parser.add_argument("--wdl-cut", action="store_true",
                            help="[deprecated] use standard 8-bit WDL cut algorithm")

    def get_default_config(self):
        return {
            "wdl_cut": 0
        }

    def get_config(self):
        return {
            "wdl_cut": int(self.config["WDLCut"]["wdl_cut"])
        }

    def get_uncertain_orders(self, orders):
        return []


