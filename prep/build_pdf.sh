#!/usr/bin/env bash
set -euo pipefail
PREP_ROOT="$(cd "$(dirname "$0")" && pwd)"
PREP_PYTHON="${PREP_PYTHON:-/Users/hmzarc/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3}"
exec "$PREP_PYTHON" "$PREP_ROOT/build_pdf.py"
