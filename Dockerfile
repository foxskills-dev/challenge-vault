FROM ubuntu:24.04

ARG RUNNER_CONFIG

WORKDIR /builder

COPY fs_lib/build/* .
RUN chmod +x base.sh

RUN ./base.sh $RUNNER_CONFIG

COPY build/sshkey /home/appuser/.ssh/vault_key
RUN chown appuser:appgroup /home/appuser/.ssh/vault_key
RUN chmod 600 /home/appuser/.ssh/vault_key

USER appuser

WORKDIR /runner
COPY fs_lib fs_lib
ENTRYPOINT ["/runner/venv/bin/python3", "fs_lib/container/entrypoint.py"]