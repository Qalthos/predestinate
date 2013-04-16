import subprocess # to run xautomation


class MouseGod(object):
    """Can predestine the actions of the mouse."""

    def __init__(self):
        pass

    def move(self, x, y, relative=False):
        """Move the mouse pointer. Default is absolute coords.
        x: change in x
        y: change in y
        relative: move mouse relative to its current position"""
        if not relative:
            self.xte_args = "mousemove {} {}".format(x, y)
            subprocess.call(["xte", self.xte_args])
        else:
            self.xte_args = "mousermove {} {}".format(x, y)
            subprocess.call(["xte", self.xte_args])


class KeyGod(object):
    """Can predestine the actions of the keyboard."""

    def __init__(self):
        pass

    def key(self, key):
        """Press and release a key.
        key: a string representing the key to press and release"""
        self.xte_args = "key {}".format(key)
        subprocess.call(["xte", self.xte_args])

    def key_down(self, key):
        """Press a key down.
        key: a string representing the key to press"""
        self.xte_args = "keydown {}".format(key)
        subprocess.call(["xte", self.xte_args])

    def key_up(self, key):
        """Release a key.
        key: a string representing the key to release"""
        self.xte_args = "keyup {}".format(key)
        subprocess.call(["xte", self.xte_args])

    def key_str(self, string):
        """Press and release each character in the string
        string: the string of characters to press and release"""
        self.xte_args = "str {}".format(string)
        subprocess.call(["xte", self.xte_args])
