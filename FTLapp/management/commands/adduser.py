from django.core.management.base import BaseCommand, CommandError
from FTLapp.models import *

class Command(BaseCommand):
	## help text for the command
	help = 'add the user to the database'

	## method of a class used to add arguments
	def add_arguments(self, parser):
		parser.add_argument('id', type=str, help='Indicates the unique ID to be given to the user')
		parser.add_argument('real_name', type=str, help='Indicates the real name of the user')
		parser.add_argument('tz', type=str, help='Indicates the tz of the user')
		parser.add_argument('--start_time', nargs='+', type=str, help='Indicates the starting time of the activity of the user')
		parser.add_argument('--end_time', nargs='+', type=str, help='Indicates the ending time of the activity of the user')

	## method of a class used to handle command and acknowedge
	def handle(self, *args, **kwargs):
				
		if User.objects.filter(id=kwargs['id']).exists():
			raise CommandError('User "%s" already exist, Please try to add with different id' % kwargs['id'])

		else:
			User.objects.create(id=kwargs['id'],real_name=kwargs['real_name'],tz=kwargs['tz'])
			user_instance = User.objects.get(id=kwargs['id'])
			if type(kwargs['start_time'])==list and type(kwargs['end_time'])==list:
				for start_time,end_time in zip(kwargs['end_time'],kwargs['end_time']):
					ActivityPeriod.objects.create(start_time=start_time,end_time=end_time,user_id=user_instance)
			else:
				ActivityPeriod.objects.create(start_time=kwargs['start_time'],end_time=kwargs['end_time'],user_id=user_instance)

		

		self.stdout.write(self.style.SUCCESS('Successfully created user "%s"' % kwargs['id']))