from django import template

from poll_app.models import PollQuestion, VoteTracker

register = template.Library()

@register.filter('percentage')
def percentage(vote, poll_id):
	poll = PollQuestion.objects.get(id=poll_id)
	vote_percentage = float(vote) / float(poll.votetracker_set.count())
	return int(vote_percentage * 100)
