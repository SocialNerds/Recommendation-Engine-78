FROM tensorflow/tensorflow:latest-py3-jupyter

# Get user id and group id from arguments
ARG UID
ARG GID

# Create user.
RUN groupadd -r serveruser -g $GID && useradd -ms /bin/bash serveruser -u $UID -g $GID
RUN chown -R serveruser:serveruser /home/serveruser

# Install some packages.
RUN pip install keras h5py tb-nightly scikit-learn pandas tensorrec

WORKDIR /home/serveruser/ai

EXPOSE 8888 6006 8000

USER serveruser
