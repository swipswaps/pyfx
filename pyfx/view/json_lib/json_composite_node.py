from abc import ABCMeta
from abc import abstractmethod
from typing import Union

from overrides import final
from overrides import overrides

from pyfx.view.json_lib.json_simple_node import JSONSimpleNode


class JSONCompositeNode(JSONSimpleNode, metaclass=ABCMeta):

    def __init__(self,
                 key: Union[str, None],
                 value: object,
                 parent: Union["ObjectNode", "ArrayNode", None] = None,
                 display_key: bool = True
                 ):
        super().__init__(key, value, parent, display_key)
        self._expanded = False
        self._start_widget = None
        self._unexpanded_widget = None
        self._end_node = None

    # =================================================================================== #
    # getters and setters                                                                 #
    # =================================================================================== #

    # expanded
    def is_expanded(self):
        return self._expanded

    def toggle_expanded(self):
        self._expanded = not self._expanded

    @abstractmethod
    def has_children(self) -> bool:
        pass

    @abstractmethod
    def get_first_child(self) -> Union["JSONSimpleNode", None]:
        pass

    @abstractmethod
    def get_last_child(self) -> Union["JSONSimpleNode", None]:
        pass

    @abstractmethod
    def prev_child(self, key) -> Union["JSONSimpleNode", None]:
        pass

    @abstractmethod
    def next_child(self, key) -> Union["JSONSimpleNode", None]:
        pass

    # =================================================================================== #
    # ui                                                                                  #
    # =================================================================================== #

    @final
    @overrides
    def get_widget(self):
        if not self.is_expanded():
            return self.get_unexpanded_widget()
        return self.get_start_widget()

    @final
    @overrides
    def load_widget(self):
        raise AttributeError(
            f"{type(self)} is a composite node and does not have #load_widget() method."
        )

    # start widget
    def get_start_widget(self):
        if self._start_widget is None:
            self._start_widget = self.load_start_widget()
        return self._start_widget

    @abstractmethod
    def load_start_widget(self):
        pass

    # unexpanded widget
    def get_unexpanded_widget(self):
        if self._unexpanded_widget is None:
            self._unexpanded_widget = self.load_unexpanded_widget()
        return self._unexpanded_widget

    @abstractmethod
    def load_unexpanded_widget(self):
        pass

    # end_widget
    def get_end_node(self):
        if self._end_node is None:
            self._end_node = self.load_end_node()
        return self._end_node

    @abstractmethod
    def load_end_node(self):
        pass
