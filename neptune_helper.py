
from os import getenv

from boto3.session import Session
from neptune_python_utils.gremlin_utils import GremlinUtils
from neptune_python_utils.endpoints import Endpoints

def iam_connect():
    """
    Creates a connection using IAM authorization.
    The function needs the following env vars to be defined:
    AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN, AWS_REGION
    and NEPTUNE_ENDPOINT.

    Returns:
    A 'g' object that can be used to run queries against
    a Neptune db, for instance:

    g = neptune_iam_connect()

    g.V().limit(10).valueMap().toList()
   """
    access_key = getenv('AWS_ACCESS_KEY_ID', '')
    secret_key = getenv('AWS_SECRET_ACCESS_KEY', '')
    region =     getenv('AWS_REGION', '')
    session_token = getenv('AWS_SESSION_TOKEN', '')
    neptune_endpoint =  getenv('NEPTUNE_ENDPOINT', '')
    GremlinUtils.init_statics(globals())
    session = Session(aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                aws_session_token=session_token,
                                region_name=region)
    credentials = session.get_credentials()
    endpoints = Endpoints(
    neptune_endpoint=neptune_endpoint,
    neptune_port=8182,
    region_name=region,
    credentials=credentials)
    gremlin_utils = GremlinUtils(endpoints)
    conn = gremlin_utils.remote_connection()
    g = gremlin_utils.traversal_source(connection=conn)
    return g
