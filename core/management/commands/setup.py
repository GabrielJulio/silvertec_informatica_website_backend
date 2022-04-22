from django.core.management.base import BaseCommand, no_translations
from django.core.management import execute_from_command_line
from django.contrib.auth.models import User
from processor.models import Processor


class Command(BaseCommand):
    help = 'Setup enviroment'

    @no_translations
    def handle(self, *args, **options):
        self._migrate()
        self._create_first_user()
        self._create_processors()

    @staticmethod
    def _migrate() -> None:
        """Migrate the database

        Run all migrations, if you didn't.
        """
        execute_from_command_line(["manage.py", "migrate"])

    @staticmethod
    def _create_first_user() -> bool:
        """Create the first superuser

        Create a superuser 'admin' with the password 'admin'.
        """
        User.objects.create_superuser('admin', password='admin').save()

        return True

    @staticmethod
    def _create_processors() -> bool:
        """Create sample processors

        Populates the database with 4 sample processors.
        """
        processors_data = [
            {'name': 'Processador Intel Core i5', 'brand': 'INT'},
            {'name': 'Processador Intel Core i7', 'brand': 'INT'},
            {'name': 'Processador AMD Athlon', 'brand': 'AMD'},
            {'name': 'Processador AMD Ryzen 7', 'brand': 'AMD'},
        ]

        for processor_data in processors_data: Processor.objects.create(**processor_data)
        print('Sample processors created')
        return True
