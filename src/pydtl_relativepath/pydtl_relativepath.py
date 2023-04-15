"""
Relative Path Utilities for multi-structured frameworks
=======================================================

#How-To-Use-PathObj

Whenever specifying a relative path use `rel2abs`

See an Example below

> from pydtl_relativepath import rel2abs as r2a
> readmepath = r2a("README.txt")
> print(open(readmepath, mode="r", encoding="utf-8").read())

This will convert relative path specified to an absolute path: <absolute path of current file's directory>/README.txt
Here, readmepath contains the absolute path for README.txt file and it is compatible with os.PathLike objects.
"""


import os
import inspect


class PathObj(os.PathLike):
    """Relative Path Object for all path handlings"""
    def __init__(self, relative_path: str, relative_to: str):
        """
        Path Object

        :param relative_path: Specify the relative path to be converted
        :param relative_to: Specify the root location. possible values: 'f' - current file's dir, 'c' - current working dir
        """

        self.relative_path = relative_path
        self.relative_to = relative_to
        self.absolute_path = self._frame_abs_path()

    def _frame_abs_path(self) -> str:
        root_path = ""

        if self.relative_to == 'f':
            root_path = os.path.dirname(inspect.stack()[3].filename)  # current file's dir
        elif self.relative_to == 'c':
            root_path = os.path.abspath(os.curdir)  # current working dir
        else:
            raise ValueError(f"Invalid root option [{self.relative_to}]\nPossible options: "
                              "'f' - current file's dir, 'c' - current working dir")

        abs_path = os.path.join(root_path, self.relative_path)
        return os.path.normcase(os.path.normpath(abs_path))

    def __repr__(self):
        return self.absolute_path

    def __str__(self):
        return self.absolute_path

    def __fspath__(self):
        return self.absolute_path

    def __eq__(self, other):
        return os.path.samefile(self.absolute_path, other)


def rel2abs(relative_path: str, relative_to='f'):
    """
    Convert Relative Path to Absolute Path Object

    :param relative_path: Specify the relative path to be converted
    :param relative_to: Specify the root location. possible values: 'f' - current file's dir, 'c' - current working dir
    """

    return PathObj(relative_path=relative_path, relative_to=relative_to)
