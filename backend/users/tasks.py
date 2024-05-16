from django.core import management

from purrfect_pix import celery_app


@celery_app.task
def clearsessions():
    management.call_command("clearsessions")
