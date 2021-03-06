import logging

from django.core.management.base import BaseCommand, CommandError

from fjord.search.index import es_delete_cmd


class Command(BaseCommand):
    help = 'Delete an index from elastic search.'

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)
        if not args:
            raise CommandError('You must specify which index to delete.')

        es_delete_cmd(args[0])
