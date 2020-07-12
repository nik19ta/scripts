#!/bin/bash

if [ -n "$1" ]; then
    if test -e $1     # Используем команду test
    then
      echo "------------------------------"
      echo "Запускаю файл: $1 в A VS Code";
      echo "------------------------------"
      open $1 -a Visual\ Studio\ Code.app
    else
      echo "Файла $1 не существует."


      echo "Создать файл Y/n к катологе: `pwd`"
      read doing #здесь мы читаем в переменную $doing со стандартного ввода

      case $doing in
      y)
      > $1
      open $1 -a Visual\ Studio\ Code.app
      ;;
      n)
      exit 0
      ;;
      *)
      exit 0
      esac #окончание оператора case.
    fi
else
    echo "--------------------------------------"
    echo "Запускаю VS Code";
    echo "--------------------------------------"
    open Visual\ Studio\ Code.app
fi
