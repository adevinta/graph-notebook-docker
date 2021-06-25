# graph-notebook

This Dockerfile builds an [aws/graph-notebook] environment. It provides an easy
way to interact with graph databases using Jupyter notebooks.

Apart from to the required dependencies for running the [aws/graph-notebook],
the Dockerfile also install the [aws/neptune-python-utils] module in order to
allow to connect to Neptune using IAM credentials.

[aws/graph-notebook]: https://github.com/aws/graph-notebook
[aws/neptune-python-utils]: https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils
