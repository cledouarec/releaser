#! python3

"""
Unit tests for gitclient.
"""

import pytest
from releaser.core.gitclient import GitClient


def test_create_git_client_with_invalid_path() -> None:
    """
    Git client creation with invalid path must raise an exception.
    """
    with pytest.raises(Exception):
        GitClient("invalid_path")
