#!/usr/bin/env python3
"""Backward-compatible entrypoint for website_to_csv_extractor.py."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    target = Path(__file__).with_name("website_to_csv_extractor.py")
    runpy.run_path(str(target), run_name="__main__")
