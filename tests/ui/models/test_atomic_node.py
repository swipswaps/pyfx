import unittest

from urwid.compat import B

from pyfx.ui.models.atomic_node import AtomicNode


class AtomicNodeTest(unittest.TestCase):
    def test_integer_node(self):
        data = 1

        # act
        node = AtomicNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B("1                 ")]]
        ]
        self.assertEqual(expected, texts)

    def test_number_node(self):
        data = 1.0

        # act
        node = AtomicNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B("1.0               ")]]
        ]
        self.assertEqual(expected, texts)

    def test_string_node(self):
        data = "str"

        # act
        node = AtomicNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B("str               ")]]
        ]
        self.assertEqual(expected, texts)

    def test_boolean_node(self):
        data = True

        # act
        node = AtomicNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B("True              ")]]
        ]
        self.assertEqual(expected, texts)

    def test_null_node(self):
        data = None

        # act
        node = AtomicNode("", data, display_key=False)
        widget = node.get_widget()

        contents = []
        while widget is not None:
            contents.append(widget.render((18,)).content())
            if widget.is_expandable():
                widget.keypress((18,), "enter")
            widget = widget.next_inorder()

        texts = [[[t[2] for t in row] for row in content] for content in contents]

        # verify
        self.assertEqual(1, len(texts))
        expected = [
            [[B("null              ")]]
        ]
        self.assertEqual(expected, texts)