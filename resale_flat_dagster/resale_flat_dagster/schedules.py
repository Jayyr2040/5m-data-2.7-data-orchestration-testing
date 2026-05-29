"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
from dagster_dbt import build_schedule_from_dbt_selection

from .assets import resale_flat_dbt_assets

materialize_dbt_job_schedule = build_schedule_from_dbt_selection(
    [resale_flat_dbt_assets],
    job_name="materialize_dbt_models",
    cron_schedule="0 0 * * *", # Enter your preferred cron schedule here.
    dbt_select="fqn:*",
)

# Access the job object created by the schedule
materialize_dbt_job = materialize_dbt_job_schedule.job

schedules = [materialize_dbt_job_schedule]
jobs = [materialize_dbt_job]