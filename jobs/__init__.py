from nautobot.core.celery import register_jobs
from .api_test_job import CoreSiteDesign

register_jobs(CoreSiteDesign)
