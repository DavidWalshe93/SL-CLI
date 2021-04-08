"""
Author:     David Walshe
Date:       08 April 2021
"""

import logging

from src.db.schema import DB

logger = logging.getLogger(__name__)


class Accessor:
    """
    Core Accessor class to subclass from.
    """

    @property
    def db(self) -> DB:
        """Returns the database instance."""
        return DB.get_db()
