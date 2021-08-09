from os import getenv

from neptune_python_utils.gremlin_utils import GremlinUtils
from neptune_python_utils.endpoints import Endpoints


def get_neptune_iam_connection(neptune_host, neptune_port=8182):
    """Returns a Neptune connection using IAM authentication. It expects valid
    AWS credentials and the environment variable ``AWS_REGION``.

    Example:

        from neptune_helper import get_neptune_iam_connection
        from gremlin_python.process.anonymous_traversal import traversal

        conn = get_neptune_iam_connection("neptune.example.com", 8182)
        g = traversal().withRemote(conn)
    """
    region = getenv('AWS_REGION', None)
    if region is None:
        raise EnvVarNotSetError('AWS_REGION')

    endpoints = Endpoints(
        neptune_endpoint=neptune_host,
        neptune_port=neptune_port,
        region_name=region,
    )
    gremlin_utils = GremlinUtils(endpoints)
    return gremlin_utils.remote_connection()


class EnvVarNotSetError(Exception):
    """It is returned when an environment variable was not set."""

    def __init__(self, name=None):
        msg = 'environment variable not set'
        if name is not None:
            msg = f'environment variable not set: {name}'

        super().__init__(msg)

        self.name = name
