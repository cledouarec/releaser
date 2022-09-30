#! python3

"""
Manage command line interface.
"""

import logging
import sys
import click


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose mode")
def main(verbose) -> None:
    """
    Entry point of all commands.
    """
    # Create logger
    if verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(
        stream=sys.stdout,
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=log_level,
    )
