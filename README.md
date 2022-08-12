# graph-notebook

This Dockerfile builds an [aws/graph-notebook] environment. It provides an easy
way to interact with graph databases using Jupyter notebooks.

Apart from the required dependencies for running the [aws/graph-notebook] the
Dockerfile also installs the [aws/neptune-python-utils] module together with a
helper function that allows notebooks to connect to Neptune using Python and AWS
IAM credentials.

## Using neptune-python-utils

Run the docker image passing the environment variables corresponding to your
"AWS variables", Neptune's host and Neptune's port:

```
docker run --rm -ti -p 8888:8888 \
    -e AWS_ACCESS_KEY_ID  -e AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN \
    -e AWS_REGION="eu-west-1" \
    adevinta/graph-notebook-docker:v1.0.0
```

Alternatively you can share your local notebooks using the `-v` flag, for
instance:

```
docker run --rm -ti -p 8888:8888 \
    -v $PWD:/notebooks \
    -e AWS_ACCESS_KEY_ID  -e AWS_SECRET_ACCESS_KEY -e AWS_SESSION_TOKEN \
    -e AWS_REGION="eu-west-1" \
    adevinta/graph-notebook-docker:v1.0.0
```

Then, execute the following code in a Notebook served from the container:

```python
from neptune_helper import get_neptune_iam_connection
from gremlin_python.process.anonymous_traversal import traversal
conn = get_neptune_iam_connection("neptune.example.com", 8182)
g = traversal().withRemote(conn)
```

After that, you can use the `g` object to issue Gremlin queries:

```python
g.V().limit(10).valueMap().toList()
```

## Python dependencies

Both direct and transitive dependencies must be pinned. In order to do that we
use [pip-compile]. After modifying the file `requirements.in`, you must run the
following command to update `requirements.txt`:

```
script/pip-compile requirements.in requirements.txt
```

## Versioning

We use [semantic-versioning] for releases. Each release in git has its
corresponding tag in this [dockerhub repository].

## Contributing

**This project is in an early stage, we are not accepting external
contributions yet.**

To contribute, please read the contribution guidelines in [CONTRIBUTING.md].


[aws/graph-notebook]: https://github.com/aws/graph-notebook
[aws/neptune-python-utils]: https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils
[pip-compile]: https://pypi.org/project/pip-tools/
[semantic-versioning]: https://semver.org/spec/v2.0.0.html
[dockerhub repository]: https://hub.docker.com/r/adevinta/graph-notebook-docker
[CONTRIBUTING.md]: CONTRIBUTING.md
