"""Unittesting for pydtl_relativepath tool"""

import os

import pytest
from pydtl_relativepath import rel2abs


def test_relative_to_current_working_directory():
    """Test abosolute path construction relative to current working directory"""

    path = rel2abs("README.md", relative_to="c")
    assert path == os.path.join(os.path.abspath(os.curdir), "README.md")


def test_relative_to_current_file():
    """Test abosolute path construction relative to current file's directory"""

    path = rel2abs(r"..\README.md", relative_to="f")
    root_dir = os.path.dirname(os.path.dirname(__file__))
    assert path == os.path.join(root_dir, "README.md")


def test_file_opening_with_output_path():
    """Test abosolute path constructed with file open"""

    path = rel2abs(r"..\README.md", relative_to="f")
    readme = open(path, mode="r", encoding="utf-8")
    readme.close()


def test_string_manipulation_on_output_path():
    """Test abosolute path constructed as str"""

    path = rel2abs(r"..\README.md", relative_to="f")
    assert (str(path) + "2").endswith("2")
    assert path == repr(path)


def test_invalid_option():
    """Test invalid relative to option"""

    with pytest.raises(ValueError):
        rel2abs("README.md", relative_to="i")
