from sh import ls, pwd, git

def out_w(text):
    print("\033[37m{}".format(text))

try: git_data = git("diff", "--name-only")
except: git_data = False
try: git_untracked = str(git("status").split('(use "git add <file>..." to include in what will be committed)')[1].split('no changes added to commit (use "git add" and/or "git commit -a")')[0])
except: git_untracked = False
try: git_modified = str(git("status").split('(use "git reset HEAD <file>..." to unstage)')[1].split('Changes not staged for commit:')[0])
except: git_modified = False


if git_data:

    print(f'Путь: {pwd()}\033[32mОбноружен git ')
    print(' ')
    for line in ls("-l").splitlines():
        mylist = [x for x in line.split(' ') if x]

        if len(mylist) > 2:
            try: 
                if mylist[8] in git_data: 
                    out_w(f'\033[31m:modified  \033[37m{mylist[6].title()} {mylist[7]}, file:\033[31m{mylist[8]} ')
                    continue

            except: pass
            try: 
                if mylist[8] in git_untracked: 
                    out_w(f'\033[33m:untracked \033[37m{mylist[6].title()} {mylist[7]}, file:\033[33m{mylist[8]}')
                    continue
            except: pass
            try: 
                if mylist[8] in git_modified: 
                    out_w(f'\033[32m:modified \033[37m {mylist[6].title()} {mylist[7]}, file:\033[32m{mylist[8]}')
                    continue
            except: pass
            try: 
                out_w(f'\033[36m:commited \033[37m {mylist[6].title()} {mylist[7]}, file:\033[36m{mylist[8]}')
                continue
            except: pass
else:

    print(' ')
    print(f'Путь: {pwd()}\033[31mGit не обноружен ')
    print(' ')
    for line in ls("-l").splitlines():
        mylist = [x for x in line.split(' ') if x]

        if len(mylist) > 2:
            out_w(f'Сreated: {mylist[6].title()} {mylist[7]}, file: {mylist[8]}')
