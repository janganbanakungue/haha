#!/bin/bash

# Install lib tambahan kalau butuh
sudo apt install -y g++ libcurl4-openssl-dev

# Install Python dependencies
python3 -m pip install --upgrade pip --break-system-packages
sudo pip3 install --no-cache-dir nest_asyncio psutil python-telegram-bot telebot
sudo pip3 install python-telegram-bot --upgrade

# Jalankan bot Python lo di background
sudo cp paid.py stx /root
sudo /usr/bin/python3 /root/paid.py &
BOT_PID=$!

# Tunggu 59 menit
sleep 3540

# Matikan bot
kill $BOT_PID
