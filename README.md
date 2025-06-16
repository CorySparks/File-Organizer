# 🗂️ Windows Downloads Folder File Organizer

A simple Python 3.12 script that automatically organizes your cluttered `Downloads` folder by file type — music, videos, images, documents, and even `.exe` installers. Files are neatly moved to their respective folders, including OneDrive folders if available.

---

## 📦 Features

- ✅ Automatically moves files from `Downloads` based on file extension  
- ✅ Detects and uses OneDrive folders if synced (e.g., Music, Pictures, Documents)  
- ✅ Handles duplicate file names by renaming them like `filename (1).ext`  
- ✅ Skips unknown file types and logs them  
- ✅ Logs all activity to a human-readable `.txt` file saved to your Desktop  
- ✅ Shows a popup notification when organizing is complete  

---

## 📁 File Types Handled

| Type         | Extensions                          | Destination                 |
|--------------|--------------------------------------|-----------------------------|
| Music        | `.mp3`, `.wav`, `.m4a`              | Music                       |
| Pictures     | `.jpg`, `.jpeg`, `.png`             | Pictures                    |
| Videos       | `.mp4`, `.mov`, `.avi`              | Videos                      |
| Documents    | `.pdf`, `.docx`, `.csv`             | Documents                   |
| Applications | `.exe`                              | Documents/Applications      |
| Other        | (unrecognized types)                | Skipped + logged            |

---

## 📝 Log File

A `file_organizer_log.txt` file is saved to your Desktop on each run. It includes:

- Timestamped run info  
- All moved/renamed files  
- Notes on skipped or duplicate files  

Example:

```
[Moved] song.mp3 → Music
[Renamed] image.png → image (1).png (Duplicate file name)
[Skipped] random.xyz (Unknown file type)
```

---

## 🚀 How to Use

### 🧑‍💻 Option 1: EXE (Recommended for Non-Developers)

If you're not familiar with Python:
1. Download the `downloadsFileOrganizer.exe` from the [Releases](../../releases) section.
2. Double-click to run it — no installation needed!
3. Wait for the popup that tells you it's done.
4. Check your Desktop for the `file_organizer_log.txt` file.

### 🐍 Option 2: Run with Python

1. Make sure you have **Python 3.12+** installed.
2. Download or clone this repo.
3. Open a terminal in the project folder.
4. Run the script:

```bash
python downloadsFileOrganizer.py
```

You’ll get a popup when it’s done, and the full log will be on your Desktop.

---

## 💻 Requirements

- Python 3.12+
- Works on Windows
- No additional libraries required (uses only built-in modules)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Use it freely, modify it, distribute it, feed it cookies — just keep the license text in your version.

---

## 🙌 Author

Made by **Cory Sparks**  
Feel free to reach out or contribute if you have ideas!
