from __future__ import annotations

import json
from pathlib import Path

import typer

JSONL = Path(__file__).parent / "sweap_eval_full_v2.jsonl"


def main(instance_id: str) -> None:
    for line in JSONL.read_text().splitlines():
        entry = json.loads(line)
        if entry["instance_id"] == instance_id:
            files: list[str] = json.loads(entry["selected_test_files_to_run"])
            typer.echo("\n".join(files))
            return
    raise typer.BadParameter(f"Instance not found: {instance_id}")


if __name__ == "__main__":
    typer.run(main)
