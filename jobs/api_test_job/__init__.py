from nautobot.core.celery import register_jobs
from nautobot.dcim.models import Location
from nautobot.extras.jobs import get_task_logger, Job, ObjectVar, StringVar, IPNetworkVar

logger = get_task_logger(__name__)


class CoreSiteDesign(Job):
    """Create a core backbone site."""

    region = ObjectVar(
        label="Region",
        description="Region for the new backbone site",
        model=Location,
    )

    site_name = StringVar(regex=r"\w{3}\d+")

    site_prefix = IPNetworkVar(min_prefix_length=16, max_prefix_length=22)
    has_sensitive_variables = False

    class Meta:
        """Metadata needed to implement the backbone site design."""

        name = "Backbone Site Design"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        nautobot_version = ">=2"

name = "API Test Job"
register_jobs(CoreSiteDesign)
