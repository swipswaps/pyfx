from overrides import overrides

from pyfx.view.json_lib.object.object_end_widget import ObjectEndWidget
from pyfx.view.json_lib.json_composite_end_node import JSONCompositeEndNode


class ObjectEndNode(JSONCompositeEndNode):
    """
    end node for `object` JSON type
    """

    def __init__(self,
                 start_node
                 ):
        super().__init__(start_node)

    @overrides
    def load_widget(self):
        return ObjectEndWidget(self)
