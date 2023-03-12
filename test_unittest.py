import os
from pydtl_relativepath import rel2abs


def test_abs_path_croot():
    path = rel2abs('README.md', root='c')
    assert path == os.path.join(os.path.abspath(os.curdir), 'README.md')


def test_abs_path_froot():
    path = rel2abs('README.md', root='f')
    assert path == os.path.join(os.path.dirname(__file__), 'README.md')


def test_file_opening():
    path = rel2abs('README.md', root='f')
    f = open(path, mode='r')
    f.close()


if __name__ == "__main__":
    import pytest
    pytest.main(args=["-v"])
