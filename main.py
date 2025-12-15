from __future__ import annotations
from pathlib import Path

import argparse
import sys

def create_project(target_folder: Path, project_name: str) -> Path:
    target_folder = target_folder.expanduser().resolve()
    out_dir = target_folder / project_name
    out_dir.mkdir(parents=True, exist_ok=True)

    readme = out_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# {project_name.replace('_', ' ').title()}\n",
            encoding="utf-8",
        )
    return out_dir

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Create a simple project folder with a README.md.",
    )

    parser.add_argument(
        "target_folder",
        type=Path,
        help="Where to create the project directory",
    )
    parser.add_argument(
        "--name",
        default="my_project",
        help="Project folder name to create (default: my_project)",
    )

    args = parser.parse_args(argv)

    try:
        out_dir = create_project(args.target_folder, args.name)
    except OSError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Created: {out_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
