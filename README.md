# Count-Files-By-Type

 Steps through a directory and outputs a count of each filetype inside.

* Gets directory containing the files.
	* Checks for directory to be passed with terminal command. (sys.argv[1])
	* Asks for a directory via input/drag-and-drop if not found in terminal command.
* Walks through the directory and subdirectories and generates a dictionary of extensions and their counts.
* Displays the totals for each extension to the console.
* (Optionally) Outputs a file ("file_counts.txt") to the User's Downloads folder with the extensions and counts.

```bash
$ python3 countfiles
```

## Build info

```bash
pyinstaller -F -n "Count Files By Type" --icon=.\countfiles\icon\count.ico .\countfiles\countfiles.py
```

Remove -F if one-file causes issues with Windows
