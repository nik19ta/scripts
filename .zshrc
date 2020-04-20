# Приветствие
echo Hi Nik

# Для мака
alias fileshow='defaults write com.apple.finder AppleShowAllFiles YES; killall Finder /System/Library/CoreServices/Finder.app'
alias filehide='defaults write com.apple.finder AppleShowAllFiles NO; killall Finder /System/Library/CoreServices/Finder.app'
# ПОдключение скрипта atom
alias atom='~/scripts/atom.sh'

alias ды='ls'
alias зцв='pwd'
alias тфтщ='nano'
alias ыщгксу='source'
alias св='cd'
alias l='ls -lhA'
alias la='ls -A'

# Своя настройка bash
PS1='%F{50}%B%n%B%F{90}%B%F{130}%3~%F{248} ❯ '
