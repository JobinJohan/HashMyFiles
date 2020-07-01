# HashMyFiles
Little software that computes the SHA-256 hash of all files contained in a directory. To run the programm use:

```bash
python hash.py <directory> <fileContainingExceptions>
```

### where:
* \<directory\> is the path of the folder you want to scan (subdirectories included)
* \<fileContainingExceptions\> is the file that contains all files/folders that should not be scanned. Each file/folder is separated by a comma i.e: myFile.extension,myFile2.extension,myFile3.extension,myFolder,myFolder2

### Example
```bash
python hash.py . exception.txt
```

### Explanations
#### The previous command starts the programm and displays the main menu:

Choose your mode:
1. Scan all directories, subdirectories and compute the SHA-256 hash of each file 
2. Check the modification
3. Exit

#### Enter 1 or 2 or 3. Here is the description of each mode

1. This produces a file called "output.json" that contains all files/folders of the given path and their hash
```text
{"exception.txt": "6545d3eacf694ec9851ee633b25428a79b0e3cf8bbebca99af415cdf4d25d2e6", 
"hash.py": "fe955dee2b6e05de247df4246e7d861c222e8bcaff24e1ef3d1846d259279e58", 
"readme.txt": "322d52e73ebe2bf7a9a462145830d4aaa099d5e7f35f2c5cac212273c72219fe"}
```

2) Enter the path of the file that contains all hash (i.e output.json) and this will display all modification, deletion and creation of all the files in the given <\directory\>

```text
{'exception.txt': 'File not modified: 6545d3eacf694ec9851ee633b25428a79b0e3cf8bbebca99af415cdf4d25d2e6', 'hash.py': 'File modified: previous hash:fe955dee2b6e05de247df4246e7d861c222e8bcaff24e1ef3d1846d259279e58 current hash: 2457f7763813f1605cb04280e052f20cad7da916fdc7c4c9cf4cd63e943b0647', 
'readme.txt': 'File not modified: 322d52e73ebe2bf7a9a462145830d4aaa099d5e7f35f2c5cac212273c72219fe'}
````

3) It simply closes the program

	
