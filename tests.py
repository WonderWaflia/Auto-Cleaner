from pathlib import Path

folder = Path("/home/wonder/Downloads")

def create_nedw_trash(col):
    for i in range(col):
        file = folder / f"hello.txt{i}"

        file.write_text("Привет, файл создан через Python", encoding="utf-8")


create_nedw_trash(3)