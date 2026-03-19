#!/usr/bin/env python3

import argparse
import csv
import sys
from pathlib import Path


def _reader(path: Path):
    handle = path.open("r", newline="", encoding="utf-8")
    return handle, csv.DictReader(handle)


def project_csv(input_path: Path, output_path: Path, columns: list[str]) -> int:
    src, reader = _reader(input_path)
    try:
        if reader.fieldnames is None:
            return 1

        missing = [col for col in columns if col not in reader.fieldnames]
        if missing:
            print(
                f"missing columns in {input_path}: {', '.join(missing)}",
                file=sys.stderr,
            )
            return 1

        if str(output_path) == "-":
            dst = sys.stdout
            writer = csv.DictWriter(dst, fieldnames=columns, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in reader:
                writer.writerow({col: row[col] for col in columns})
            sys.stdout.flush()
        else:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with output_path.open("w", newline="", encoding="utf-8") as dst:
                writer = csv.DictWriter(dst, fieldnames=columns, quoting=csv.QUOTE_ALL)
                writer.writeheader()
                for row in reader:
                    writer.writerow({col: row[col] for col in columns})
    finally:
        src.close()

    return 0


def filter_csv(input_path: Path, output_path: Path, column: str, value: str) -> int:
    src, reader = _reader(input_path)
    try:
        if reader.fieldnames is None or column not in reader.fieldnames:
            return 1

        output_path.parent.mkdir(parents=True, exist_ok=True)
        matched = 0
        with output_path.open("w", newline="", encoding="utf-8") as dst:
            writer = csv.DictWriter(
                dst, fieldnames=reader.fieldnames, quoting=csv.QUOTE_ALL
            )
            writer.writeheader()
            for row in reader:
                if row[column] == value:
                    writer.writerow(row)
                    matched += 1

        if matched == 0:
            output_path.unlink(missing_ok=True)
            return 1
    finally:
        src.close()

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    project = subparsers.add_parser("project")
    project.add_argument("--input", required=True, type=Path)
    project.add_argument("--output", required=True, type=Path)
    project.add_argument("--columns", required=True)

    flt = subparsers.add_parser("filter")
    flt.add_argument("--input", required=True, type=Path)
    flt.add_argument("--output", required=True, type=Path)
    flt.add_argument("--column", required=True)
    flt.add_argument("--value", required=True)

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.command == "project":
        return project_csv(args.input, args.output, args.columns.split(","))

    return filter_csv(args.input, args.output, args.column, args.value)


if __name__ == "__main__":
    raise SystemExit(main())
