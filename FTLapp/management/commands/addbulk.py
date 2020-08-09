from django.core.management.base import BaseCommand
from FTLapp.models import *
from datetime import datetime

class Command(BaseCommand):
	## help text for the command
    help = 'Create bulk of dummy users'

    ## method of a class used to add arguments
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created with random values')

    ## method of a class used to handle command and acknowedge
    def handle(self, *args, **kwargs):        
        db_count = User.objects.all().count()
        total = kwargs['total']
        for i in range(total):
            User.objects.create(id='W07QCRPA2'+str(db_count), real_name='dummyuser'+str(db_count), tz='dummytz'+str(db_count))
            user_obj = User.objects.get(id='W07QCRPA2'+str(db_count))
            ActivityPeriod.objects.create(start_time=datetime.today().ctime(),end_time=datetime.today().ctime(),user_id=user_obj)
            db_count += 1

        self.stdout.write(self.style.SUCCESS('Successfully created %d users ' % total))
