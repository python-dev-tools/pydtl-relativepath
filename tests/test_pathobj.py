"""Unittesting for pydtl_relativepath tool"""

import os
import pytest
from pydtl_relativepath import rel2abs as r2a


def test_abs_path_crelative_to():
    """Test abosolute path construction relative to current working directory"""

    path = r2a('README.md', relative_to='c')
    assert path == os.path.join(os.path.abspath(os.curdir), 'README.md')


def test_abs_path_frelative_to():
    """Test abosolute path construction relative to current file's directory"""

    path = r2a(r'..\README.md', relative_to='f')
    root_dir = os.path.dirname(os.path.dirname(__file__))
    assert path == os.path.join(root_dir, 'README.md')


def test_file_opening():
    """Test abosolute path constructed with file open"""

    path = r2a(r'..\README.md', relative_to='f')
    readme = open(path, mode='r', encoding='utf-8')
    readme.close()


def test_path_as_str_repr():
    """Test abosolute path constructed as str"""

    path = r2a(r'..\README.md', relative_to='f')
    modified_path = str(path) + "2"
    representation = repr(path)


def test_invalid_option():
    """Test invalid relative to option"""

    with pytest.raises(ValueError):
        r2a("README.md", relative_to='i')
