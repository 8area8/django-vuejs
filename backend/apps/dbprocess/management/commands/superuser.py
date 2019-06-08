"""Superuser module."""

import logging

from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()


def add_superuser():
    """Create the superuser."""
    logger = logging.getLogger('base')
    admin_context = ('admin', 'bar@hotmail.fr', 'pass')
    try:
        User.objects.create_superuser(*admin_context)
        logger.debug("admin created.")
    except IntegrityError:
        logger.warning("'admin' user already exists.")
