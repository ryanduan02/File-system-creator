set -euo pipefail

PY="/usr/bin/python3"
SCRIPT="$HOME/Code/File-system-creator/main.py"

for FOLDER in "$@"; do
  "$PY" "$SCRIPT" "$FOLDER" --name "my_project"
done
