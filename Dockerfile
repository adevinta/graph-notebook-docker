FROM python:3.9.13-slim-bullseye as python-base


FROM python-base as pip-compile
ARG PIP_TOOLS_VERSION=6.5.1
RUN pip install "pip-tools==${PIP_TOOLS_VERSION}"
ENTRYPOINT ["pip-compile"]


FROM python-base as amazon-neptune-tools
ARG AMAZON_NEPTUNE_TOOLS_VERSION=1.12
RUN apt-get update && apt-get install --no-install-recommends -y git
RUN git clone --depth 1 --branch "amazon-neptune-tools-${AMAZON_NEPTUNE_TOOLS_VERSION}" https://github.com/awslabs/amazon-neptune-tools /amazon-neptune-tools


FROM python-base

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

RUN jupyter nbextension enable --py --sys-prefix graph_notebook.widgets
RUN python -m graph_notebook.static_resources.install && \
    python -m graph_notebook.nbextensions.install

RUN mkdir /notebooks
RUN python -m graph_notebook.notebooks.install --destination /notebooks

RUN groupadd jupyter && useradd -g jupyter -m -s /bin/bash jupyter
RUN chown -R jupyter:jupyter /notebooks

WORKDIR /notebooks

USER jupyter

COPY --from=amazon-neptune-tools \
    /amazon-neptune-tools/neptune-python-utils/neptune_python_utils \
    /home/jupyter/neptune_python_utils
COPY neptune_helper.py /home/jupyter

ENV PYTHONPATH="/home/jupyter"

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888"]

CMD ["/notebooks"]
