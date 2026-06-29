from pathlib import Path
from datetime import datetime, timedelta


folder = Path("/home/wonder/Downloads")
max_age = timedelta(days=3)


def main():
    now = datetime.now()


    for item in folder.iterdir():
        if not item.is_file():
            continue
        
        file_time = datetime.fromtimestamp(item.stat().st_atime)
        age = now - file_time

        if age > max_age:
            item.unlink()
            print(f"Удален: {item}")


if __name__ == "__main__":
    main()