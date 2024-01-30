"""

Gets a folder via drag-and-drop. Counts the number of files 
for each file extension, and displays it to the terminal. 
Optionally outputs a text file with the totals to [USER]/Downloads

"""

__version__ = "1.0.0"

import os
import sys

from pathlib import Path

import dropfile
import art

DLS = Path().home() / 'Downloads'


def get_counts(fdir, fdict) -> None:
    """
    Walks through a passed directory and counts file 
    extensions, and adds the total counts to a dictionary.

    Args:
        fdir (str/pathlib.Path): Directory containing the files to count.
        fdict (dict): Dictionary to add the file counts to.
    """
    print(" Counting files...", end="")

    for _rt, _dirs, files in os.walk(fdir):
        for each in files:
            info = []
            info = each.split('.')
            fdict[info[-1].lower()] = fdict.setdefault(info[-1].lower(), 0) + 1

    print("Done.")


def display_totals(fdir, fdict) -> None:
    """
    Displays the file count totals to the console.

    Args:
        fdir (str/pathlib.Path): Directory containing the counted files.
        fdict (dict): Dictionary of file counts.
    """
    print(f"\n {fdir}\n File Counts:\n")
    for k, v in fdict.items():
        print(f" {k}: {v}")


def write_file(fdir, fdict) -> None:
    """
    Outputs file counts to a text file "file_counts.txt" 
    located in the User's Downloads folder.

    Args:
        fdir (str/pathlib.Path): Directory containing the counted files.
        fdict (dict): Dictionary of file counts.
    """
    with open(f'{DLS}/file_counts.txt', 'w') as f:
        f.write(f'{fdir}\n')
        f.write('File Counts:\n\n')
        for k, v in fdict.items():
            f.write(f'{k}: {v}\n')


def main() -> None:
    """
    Generates a empty dictionary to use, gets directory of files, 
    and calls the other needed functions. 
    """
    files = {}
    # Gets directory from terminal input if present, if not get from user
    try:
        directory = sys.argv[1]
    except IndexError:
        directory = dropfile.get()

    get_counts(directory, files)
    display_totals(directory, files)
    # Outputs list of file types to a text file in User's Downloads folder
    usersel = input("\n Output file? (y/n): ")
    if usersel.lower() == 'y':
        write_file(directory, files)


if __name__ == "__main__":
    art.display_ascii(__version__)
    print("\n Drop a folder to get a recursive count of file types it contains.")
    main()
