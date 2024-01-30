# Count-Files-By-Type

 Steps through a directory and outputs a count of each filetype inside.

Gets a folder via drag-and-drop. Counts the number of files
for each file extension, and displays it to the terminal.
Optionally outputs a text file with the totals to [USER]/Downloads

## Build info

Windows

```bash
pyinstaller -F -n "Count Files By Type" --icon=.\icon\count.ico .\countfiles\main.py
```

Remove -F if one-file causes issues with Windows

```bash
pyinstaller  -F -n "Count Files By Type" ./countfiles/main.py
```
