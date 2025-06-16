from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import os

# Created by Cory Sparks
# =========================
# FOLDER UTILITIES
# =========================

def is_actively_synced(folder: Path) -> bool:
    known_sync_files = ["desktop.ini", ".sync", ".goutputstream"]
    for item in folder.iterdir():
        if item.name in known_sync_files or "OneDrive" in str(folder):
            return True
    return False

def get_folder(folder_name: str) -> Path:
    onedrive_path = os.environ.get("OneDrive")
    if onedrive_path:
        onedrive_folder = Path(onedrive_path) / folder_name
        if onedrive_folder.exists() and is_actively_synced(onedrive_folder):
            return onedrive_folder

    fallback = Path.home() / folder_name
    fallback.mkdir(parents=True, exist_ok=True)
    return fallback

# =========================
# LOGGING UTILITIES
# =========================

def init_log_file(log_path: Path, exe_target_folder: Path):
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write("\n" + "="*50 + "\n")
        f.write(f"All .exe files are now moved to: {exe_target_folder}\n")
        f.write("="*50 + "\n")
        f.write(f"📂 File Organizer Run - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*50 + "\n")

def log_action(log_path: Path, status: str, file_name: str, destination: str = None, note: str = None):
    with open(log_path, 'a', encoding='utf-8') as f:
        line = f"[{status}] {file_name}"
        if destination:
            line += f" → {destination}"
        if note:
            line += f" ({note})"
        f.write(line + "\n")

def show_log_popup(log_path: Path):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Download Organizer", f"✅ All done!\nA full log was saved to:\n\n{log_path}")
    root.destroy()

# =========================
# FILE ORGANIZER
# =========================

def move_file_with_rename(file: Path, target_folder: Path, log_path: Path):
    target_folder.mkdir(parents=True, exist_ok=True)
    destination = target_folder / file.name

    renamed = False
    if destination.exists():
        base = file.stem
        suffix = file.suffix
        counter = 1
        while True:
            new_name = f"{base} ({counter}){suffix}"
            destination = target_folder / new_name
            if not destination.exists():
                renamed = True
                break
            counter += 1

    file.rename(destination)
    print(f"{file.name} moved to {destination}")

    status = "Renamed" if renamed else "Moved"
    note = "Duplicate file name" if renamed else None
    log_action(log_path, status, file.name, destination.name, note)

# =========================
# MAIN SCRIPT
# =========================

downloads_folder = get_folder("Downloads")
documents_folder = get_folder("Documents")
pictures_folder = get_folder("Pictures")
music_folder = get_folder("Music")
videos_folder = get_folder("Videos")
application_folder = documents_folder / "Applications"
log_path = get_folder("Desktop") / "file_organizer_log.txt"

init_log_file(log_path, application_folder)

for file in downloads_folder.iterdir():
    if file.is_file():
        match file.suffix.lower():
            case ".mp3" | ".wav" | ".m4a":
                move_file_with_rename(file, music_folder, log_path)
            case ".jpg" | ".png" | ".jpeg":
                move_file_with_rename(file, pictures_folder, log_path)
            case ".mp4" | ".mov" | ".avi":
                move_file_with_rename(file, videos_folder, log_path)
            case ".pdf" | ".docx" | ".csv":
                move_file_with_rename(file, documents_folder, log_path)
            case ".exe":
                move_file_with_rename(file, application_folder, log_path)
            case _:
                print(f"Don't recognize that file type: {file.suffix}")
                log_action(log_path, "Skipped", file.name, note="Unknown file type")

show_log_popup(log_path)