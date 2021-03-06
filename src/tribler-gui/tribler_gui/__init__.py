"""
This package contains the code for the GUI, written in pyQt.
"""
import os

from tribler_common.logger import setup_logging


def load_logger_config(log_dir):
    """
    Loads tribler-gui module logger configuration. Note that this function should be called explicitly to
    enable GUI logs dump to a file in the log directory (default: inside state directory).
    """
    logger_config = os.path.join("tribler-gui", __name__, "logger.yaml")
    setup_logging(config_path=logger_config, module='tribler-gui', log_dir=log_dir)
