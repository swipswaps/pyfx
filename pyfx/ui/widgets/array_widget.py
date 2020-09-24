#! /usr/bin/env python3

from overrides import overrides

from pyfx.ui.widgets.json_widget import JSONWidget


class ArrayWidget(JSONWidget):
    """ display widget for JSON `array` type node """

    def __init__(self,
                 node: "ArrayNode",
                 display_key: bool,
                 ):
        super().__init__(node, True, display_key)

    @overrides
    def get_display_text(self):
        if self.get_node().get_depth() == 0 or (not self.is_display_key()):
            return ""
        else:
            return self.get_node().get_key() + ":"
