# TextifyRTF
Лёгкий инструмент на Python для расшифровки Unicode-последовательностей в файлах формата RTF (Rich Text Format), таких как \uc0\u1072, в читаемый текст. Утилита принимает ввод от пользователя, обрабатывает его и сохраняет результат в файл RTF (output.doc).

## Возможности
* Расшифровка Unicode-последовательностей RTF (например, \uc0\u1072 → а).
* Вывод результатов в консоль и RTF-файл.
  

## Установка
1. Склонируйте репозиторий: 
```bash
git clone https://github.com/KinzyabaevVadim/TextifyRTF.git
```
2. Запустить скрипт:
```bash
python main.py
```

3. Проверьте расшифрованный результат в консоли и в файле output.doc

## Пример работы программы:

 Ввод:
```bash
\uc0\u1050 \uc0\u1080 \uc0\u1085 \uc0\u1079 \uc0\u1100 \uc0\u1073 \uc0\u1072 \uc0\u1077 \uc0\u1074
```

Вывод:
``` bash
Оригинальная строка: '\uc0\u1050 \uc0\u1080 \uc0\u1085 \uc0\u1079 \uc0\u1100 \uc0\u1073 \uc0\u1072 \uc0\u1077 \uc0\u1074' | Расшифрованный текст: 'Кинзябаев'
```

Работа программы:


![Code_XDHDWPVvXw](https://github.com/user-attachments/assets/d18e133b-cf7b-440e-8298-deaed7540d8e)
