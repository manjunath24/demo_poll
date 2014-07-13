from django.db import models
from django.contrib.auth.models import User


class PollQuestion(models.Model):
	name = models.CharField(max_length=250)
	pub_date = models.DateTimeField(max_length=200)

	def __unicode__(self):
		return self.name

 
class PollChoice(models.Model):
	poll = models.ForeignKey(PollQuestion)
	Choice_name = models.CharField(max_length=200)
	no_of_votes = models.IntegerField(default=0)

	def __unicode__(self):
	    return self.Choice_name		


class VoteTracker(models.Model):
	poll = models.ForeignKey(PollQuestion)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return '%s-%s' % (self.poll, self.user)