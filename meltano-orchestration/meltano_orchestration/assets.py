# assets.py
from dagster import asset, AssetExecutionContext, PipesSubprocessClient

@asset
def pipeline_meltano(context: AssetExecutionContext, pipes_subprocess_client: PipesSubprocessClient):
    """
    Runs meltano using Dagster Pipes for better logging and observability.
    """
    return pipes_subprocess_client.run(
        command=["meltano", "run", "tap-postgres", "target-bigquery"],
        context=context,
        cwd = '/mnt/c/Users/taiji/DS2026/S2_Big_Data/5m-data-2.6-data-pipelines-orchestration/meltano-resale'
    ).get_results()

@asset(deps=[pipeline_meltano])
def pipeline_dbt_run(context: AssetExecutionContext, pipes_subprocess_client: PipesSubprocessClient):
    """
    Runs dbt build using Dagster Pipes.
    """
    return pipes_subprocess_client.run(
        command=["dbt", "build"],
        context=context,
        cwd = '/mnt/c/Users/taiji/DS2026/S2_Big_Data/5m-data-2.6-data-pipelines-orchestration/resale_flat'
    ).get_results()

