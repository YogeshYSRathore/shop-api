#!/usr/bin/env bash
set -euo pipefail
# 1. tests + coverage report
python -m pytest --cov --cov-report=xml -q
# 2. scan and WAIT for the quality gate (non-zero exit if it fails)
docker run --rm \
  -e SONAR_HOST_URL="${SONAR_HOST_URL:-http://host.docker.internal:9000}" \
  -e SONAR_TOKEN \
  -v "$PWD:/usr/src" \
  sonarsource/sonar-scanner-cli \
  -Dsonar.qualitygate.wait=true -Dsonar.qualitygate.timeout=300