import sys

class TaskMyImport:
    def __init__(self, *args, **options):
        self.args = args
        self.options = options
    
    async def run(self):
        real_run = self.options.get('real_run')

        if real_run:
            print("real run")
        else:
            print("fake run")

        if not self.options.get('scheduled'):
            sys.exit(0)
