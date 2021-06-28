# graph-notebook

This Dockerfile builds an [aws/graph-notebook] environment. It provides an easy
way to interact with graph databases using Jupyter notebooks.

Apart from the required dependencies for running the [aws/graph-notebook],
the Dockerfile also installs the [aws/neptune-python-utils] module in order to
allow notebooks to connect to Neptune using Python and AWS IAM credentials.

## Using neptune-python-utils

Following you can find an example about how to use IAM credentials authorization
together with [gremlin python] in a notebook served from this docker image.

1. Run the docker image passing in the env vars with your AWS "credentials" and the Neptune endpoint:
```bash
docker run --rm -e NEPTUNE_ENDPOINT=${neptune.endpoint.example.com} -e AWS_ACCESS_KEY_ID  -e AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN \
-e AWS_REGION="eu-west-1" \
-p 8888:8888 \
graph-notebook:1.0.0 /notebooks
```
2. Execute the following code in a Notebook served from the container:
```python
import os
from datetime import datetime, timedelta
from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
import boto3
from gremlin_python.process.traversal import Cardinality
from neptune_python_utils.gremlin_utils import GremlinUtils
from neptune_python_utils.endpoints import Endpoints
access_key = os.getenv('AWS_ACCESS_KEY_ID', '')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY', '')
region = os.getenv('AWS_REGION', '')
session_token = os.getenv('AWS_SESSION_TOKEN', '')
neptune_endpoint =  os.getenv('NEPTUNE_ENDPOINT', '')
GremlinUtils.init_statics(globals())
session = boto3.session.Session(aws_access_key_id=access_key,
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
```
3. After that, you can use the ```conn``` object to issue Gremlin queries:
```python
g = gremlin_utils.traversal_source(connection=conn)
g.V().limit(10).valueMap().toList()
```

[aws/graph-notebook]: https://github.com/aws/graph-notebook
[aws/neptune-python-utils]: https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils
[gremlin python]: https://tinkerpop.apache.org/docs/current/reference/#gremlin-python
