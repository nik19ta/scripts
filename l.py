from sh import ls, pwd, git, rm
from sys import argv


try: command = argv[1].lower()
except: command = False



def out_w(text):
    print("\033[37m{}".format(text))

try: git_data = git("diff", "--name-only")
except: git_data = ''
try: git_untracked = str(git("status").split('(use "git add <file>..." to include in what will be committed)')[1].split('no changes added to commit (use "git add" and/or "git commit -a")')[0])
except: git_untracked = ''
try: git_modified = str(git("status").split('(use "git reset HEAD <file>..." to unstage)')[1].split('Changes not staged for commit:')[0])
except: git_modified = ''
try: gitignore = str(git("status").split('(use "git add <file>..." to include in what will be committed)')[1].split('no changes added to commit (use "git add" and/or "git commit -a")')[0])
except: gitignore = ''


if command == "-a":
    files = ls("-la").splitlines()
else:
    files = ls("-l").splitlines()

if git_data:

    if command == "-d":
        rmc = True

        for line in files:
            mylist = [x for x in line.split(' ') if x]

            if len(mylist) > 2:
                if mylist[8] == '.' or mylist[8] == '..':
                    pass
                else:
                    if mylist[8] in git_untracked: 
                        rm("-rf", mylist[8])
                        out_w(f'file \033[33m{mylist[8]} удалён')
                        rmc = False
        
        if rmc:
            print('\033[33mНет файлов которые нужно удалить')

    else:
        try: gitignore = open('.gitignore')
        except: gitignore = ''


        print(f'Путь: {pwd()}\033[32mОбноружен git ')
        print(' ')

        for line in files:
            mylist = [x for x in line.split(' ') if x]

            if len(mylist) > 2:
                if mylist[8] == '.' or mylist[8] == '..':
                    pass
                else:
                    if mylist[8] in gitignore:
                        out_w(f'\033[31m:gitignore \033[37m{mylist[6].title()} {mylist[7]}, file:\033[31m{mylist[8]} ')
                        continue
                    if mylist[8] in git_data: 
                        out_w(f'\033[31m:modified  \033[37m{mylist[6].title()} {mylist[7]}, file:\033[31m{mylist[8]} ')
                        continue
                    elif '.git' in mylist[8]: 
                        out_w(f'\033[94m:git file \033[37m {mylist[6].title()} {mylist[7]}, file:\033[94m{mylist[8]}')
                        continue
                    elif mylist[8] in git_untracked: 
                        out_w(f'\033[33m:untracked \033[37m{mylist[6].title()} {mylist[7]}, file:\033[33m{mylist[8]}')
                        continue
                    elif mylist[8] in git_modified: 
                        out_w(f'\033[32m:modified \033[37m {mylist[6].title()} {mylist[7]}, file:\033[32m{mylist[8]}')
                        continue
                    else:
                        out_w(f'\033[36m:commited \033[37m {mylist[6].title()} {mylist[7]}, file:\033[36m{mylist[8]}')
else:

    print(' ')
    print(f'Путь: {pwd()}\033[31mGit не обноружен ')
    print(' ')
    for line in files:
        mylist = [x for x in line.split(' ') if x]

        if len(mylist) > 2:
            out_w(f'Сreated: {mylist[6].title()} {mylist[7]}, file: {mylist[8]}')
