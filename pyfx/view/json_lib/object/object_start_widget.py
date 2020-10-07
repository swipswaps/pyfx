from pyfx.view.json_lib.json_widget import JSONWidget


class ObjectStartWidget(JSONWidget):
    """ display widget for JSON `object` type nodes """

    def __init__(self,
                 node: "ObjectNode",  # to avoid circular dependency
                 display_key: bool,
                 ):
        super().__init__(node, True, display_key)

    def get_display_text(self):
        if self.get_node().get_depth() == 0 or (not self.is_display_key()):
            return "{"
        else:
            return self.get_node().get_key() + ": {"
