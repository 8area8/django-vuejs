"""Add development datas in the database."""

from django.core.management.base import BaseCommand

# pylint: disable = import-error
from .superuser import add_superuser


class Command(BaseCommand):
    """Command class."""

    help = 'Add development datas in your database.'

    def handle(self, *args, **options):
        """Handle the command."""
        add_superuser()
