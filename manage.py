#!/usr/bin/env python
import os
import sys
from pathlib import Path

import dotenv


def main():
    base_dir = Path(__file__).resolve().parent
    env_path = base_dir / '.env'

    if env_path.exists():
        dotenv.read_dotenv(str(env_path))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()