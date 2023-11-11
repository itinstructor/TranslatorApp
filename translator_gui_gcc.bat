cd c:\temp

python -m nuitka ^
    --onefile ^
    --mingw64 ^
    --lto=no ^
    --plugin-enable=tk-inter ^
    --windows-disable-console ^
    --windows-icon-from-ico=translate.ico ^
    translator.py
pause
