from django.db import models

## User model with respective details
class User(models.Model):
	id = models.CharField(max_length=15,primary_key=True)
	real_name = models.CharField(max_length=20)
	tz = models.CharField(max_length=20)

	def __str__(self):
		return self.real_name

## User activity preiod model with respective details by coonecting with user
class ActivityPeriod(models.Model):
	user_id = models.ForeignKey(User,related_name='user_obj',on_delete=models.CASCADE)
	start_time = models.CharField(max_length=20)
	end_time = models.CharField(max_length=20)

	def __str__(self):
		period = str(self.user_id)+" -  "+self.start_time+" to "+self.end_time
		return period
