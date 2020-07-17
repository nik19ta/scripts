from sh import mv, mkdir, ls


for line in ls().splitlines():
    end = line.split('.')[int(len(line.split('.')) - 1)]
    if len(line.split('.')) > 1:
        try:
            print(ls(f'./{end}'))
            mv(line, f"./{end}")
        except:
            print(mkdir(f"{end}"))
            mv(line, f"./{end}")
