#! python3

"""
Client to communicate with Git
"""

import logging
from typing import List
from git import Repo

#: Create logger for this file.
logger = logging.getLogger()


class GitClient:
    """
    This class is used to interfacing Git repository.
    """

    def __init__(self, path: str):
        """
        Constructs the Git client.

        :param path: Git repository path.
        """
        logger.info("Connecting to Git repository : %s", path)

        #: Git repository.
        self.__repository = Repo(path)
        if self.__repository.bare:
            raise Exception("Could not connect to repository")

        logger.info("Connected to Git repository")

    def fetch_commits_title(
        self, from_commit: str, to_commit: str
    ) -> List[str]:
        """
        Fetch all commits title from commit ancestor.

        :param from_commit: Get titles from this commit.
        :param to_commit: Get titles to this commit.
        :return: Commits title list.
        """
        commits = list(
            self.__repository.iter_commits(from_commit + ".." + to_commit)
        )
        commits_title = []
        for commit in commits:
            commits_title.append(commit.summary)
        return commits_title
