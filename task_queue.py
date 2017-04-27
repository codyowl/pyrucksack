from celery import Celery
from pyrucksack import backup_directory_creator, backup_creator
from settings import TIME
#for making cronbased jobs
from celery.task.schedules import crontab
from celery.decorators import periodic_task

celery = Celery('tasks', broker='redis://localhost:6379/0')

# @celery.task
# def backup_task_queue(project_directory, destination, symlinks=False, ignore=None):
#     pass


def get_hour_and_minute(time):
	hour = time.split(':')[0]
	minute = time.split(':')[1]
	return hour, minute
	
def task_queue_creator(time):
	for t in time:
		hour, minute = get_hour_and_minute(t)
		@periodic_task(run_every=crontab(hour=hour, minute=minute, day_of_week="*"))
		def every_day_backup_task_queue(time):
			pass

