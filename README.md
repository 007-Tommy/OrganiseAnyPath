# OrganiseAnyPath

OrganiseAnyPath is a Python program designed to help organise files in a specified directory into categorized folders. It sorts files based on their extensions into predefined categories such as Images, Videos, Audio, Applications, Documents, and more.

## Features

- **Categorization**: Automatically sorts files into categories based on their file extensions.
- **Customizable Directories**: Users can modify the `directories` dictionary to add or modify categories and associated file extensions.
- **Conflict Detection**: Checks for conflicts between existing directories and the ones to be created, preventing unwanted directory overwrites.
- **Clean-up Process**: Deletes any folders it made that were not used, keeping your directory small and organised!

## Categories

The program categorizes files into the following default categories:

- Images (e.g., `.png`, `.jpg`, `.jpeg`)
- Videos (e.g., `.mp4`, `.avi`, `.mpeg`)
- Audio (e.g., `.mp3`, `.wav`, `.ogg`)
- Applications (e.g., `.exe`, `.apk`, `.jar`)
- Documents (e.g., `.txt`, `.pdf`, `.docx`)
- Compressed (e.g., `.zip`, `.rar`, `.7z`)
- Code (e.g., `.py`, `.java`, `.js`)
- Presentations (e.g., `.ppt`, `.pptx`)
- Spreadsheets (e.g., `.xls`, `.xlsx`)
- Fonts (e.g., `.ttf`, `.otf`)
- Torrents (`.torrent`)
- Rainmeter (`.rmskin`)
- Anki decks (`.apkg`)
- Other (anything else!)

## Usage

1. **Set up**: First, the program will ask you to specify the path where your files are located. This is where the program will organise your files.
2. **Conflicts**: The program checks if there are any folders that might conflict with the new ones it plans to create and if it finds any, depending on your choice, will either combine or rename conflicting folders.
3. **Organising**: The program will create folders for each category and move your files into the appropriate folder.
4. **Clean-up**: Any unused folders created by the program are deleted, for maximum cleanliness!

## Customization

You can customize the categories and associated file extensions by editing the `directories` dictionary in the program.

## Requirements

- Python 3.x
- `os` and `shutil` libraries (standard Python libraries)

## Disclaimer

Please use this program with caution. Always back up your files before running the program, especially if you are organising important directories.

## License

This program is provided "as is", without warranty of any kind. You are free to modify and distribute it as you see fit.
