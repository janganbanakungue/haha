#!/bin/bash

# Install lib tambahan kalau butuh
sudo apt install -y g++ libcurl4-openssl-dev

# Install Python dependencies
python3 -m pip install --upgrade pip --break-system-packages
sudo pip3 install --no-cache-dir nest_asyncio psutil python-telegram-bot telebot
sudo pip3 install python-telegram-bot --upgrade

# Jalankan bot Python lo di background
sudo python3 paid.py &
BOT_PID=$!

# Tunggu 5 jam
sleep 18000

# Hentikan proses bot
kill $BOT_PID
