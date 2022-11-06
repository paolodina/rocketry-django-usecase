from django.core.management.base import BaseCommand
from rocketry import Rocketry
from ._task import TaskMyImport

command_args = ()
command_options = {}

app = Rocketry(config={'task_execution': "async"})

@app.task("every 1 seconds")
async def task_my_import():
    await TaskMyImport(*command_args, **command_options).run()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--real-run',
            action='store_true',
            help="Import real data")

        parser.add_argument(
            '--scheduled',
            action='store_true',
            help="Schedule the execution of this command."
        )

    def handle(self, *args, **options):
        global command_args
        global command_options
        command_args = args
        command_options = options

        app.run()
