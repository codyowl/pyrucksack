from celery import Celery
from pyrucksack import backup_directory_creator, backup_creator

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def backup_task_queue(project_directory, destination, symlinks=False, ignore=None):
    pass
