"""Tests for the add function."""

from python_uv_exemplar_template import add


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
