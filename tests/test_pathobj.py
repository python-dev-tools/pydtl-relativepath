"""Unittesting for pydtl_relativepath tool"""

import os
from pathlib import Path

import pytest
from pydtl_relativepath import RelativePathType, rel2abs


def test_relative_to_current_working_directory():
    """Test abosolute path construction relative to current working directory"""

    # Test for file
    path = rel2abs("README.md", relative_type=RelativePathType.RELATIVE_TO_WORKING_DIRECTORY)
    assert path.is_absolute()
    assert path.is_file()
    assert path.samefile(os.path.join(os.path.abspath(os.curdir), "README.md"))

    # Test for directory
    path = rel2abs("tests", relative_type=RelativePathType.RELATIVE_TO_WORKING_DIRECTORY)
    assert path.is_absolute()
    assert path.is_dir()
    assert path.samefile(os.path.join(os.path.abspath(os.curdir), "tests"))


def test_relative_to_current_file_directory():
    """Test abosolute path construction relative to current file's directory"""

    # Test for file
    path = rel2abs("..", "README.md", relative_type=RelativePathType.RELATIVE_TO_CURRENT_FILE)
    root_dir = os.path.dirname(os.path.dirname(__file__))
    assert path.is_absolute()
    assert path.is_file()
    assert path.samefile(os.path.join(root_dir, "README.md"))

    # Test for directory
    path = rel2abs("..", "tests", relative_type=RelativePathType.RELATIVE_TO_CURRENT_FILE)
    root_dir = os.path.dirname(os.path.dirname(__file__))
    assert path.is_absolute()
    assert path.is_dir()
    assert path.samefile(os.path.join(root_dir, "tests"))


def test_parent_dir_jump():
    """Test abosolute path construction relative to current file's directory"""

    # Test for file
    path = rel2abs(
        "README.md",
        relative_type=RelativePathType.RELATIVE_TO_CURRENT_FILE,
        parent_dir_jump=-1,
    )
    root_dir = os.path.dirname(os.path.dirname(__file__))
    assert path.is_absolute()
    assert path.is_file()
    assert path.samefile(os.path.join(root_dir, "README.md"))

    # Test for directory
    path = rel2abs(
        "tests",
        relative_type=RelativePathType.RELATIVE_TO_CURRENT_FILE,
        parent_dir_jump=-1,
    )
    root_dir = os.path.dirname(os.path.dirname(__file__))
    assert path.is_absolute()
    assert path.is_dir()
    assert path.samefile(os.path.join(root_dir, "tests"))


def test_file_opening_with_output_path():
    """Test abosolute path constructed with file open"""

    path = rel2abs("..", "README.md", relative_type=RelativePathType.RELATIVE_TO_CURRENT_FILE)
    readme = open(path, mode="r", encoding="utf-8")
    readme.close()


def test_invalid_option():
    """Test invalid relative to option"""

    with pytest.raises(ValueError):
        rel2abs("README.md", relative_type="a")


def test_pathlib_compatibility():
    """Test pathlib compatibility"""

    path = rel2abs("README.md", relative_type=RelativePathType.RELATIVE_TO_WORKING_DIRECTORY)
    reconstructed_path = path.parent / path.name
    assert path == reconstructed_path
    assert isinstance(path, Path)
