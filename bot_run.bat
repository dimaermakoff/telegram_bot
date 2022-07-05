@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5542785678:AAFx4K8qVleVYLRuKBbOZqGwGLQUxSZiriw

python bot_telegram.py

pause