#!/bin/bash

# Jalankan file python bot kamu
python3 paid.py &  # ganti dengan file bot kamu
BOT_PID=$!

# Tunggu 59 menit
sleep 3540

# Matikan bot
kill $BOT_PID

# Kirim pesan ke Telegram kalau mau restart (optional)
curl -s -X POST https://api.telegram.org/bot7932562452:AAHllBiuVC_bT_wpbHHoHn-VuTiJOLL1bCg/sendMessage \
 -d chat_id=7316824198 \
 -d text="Bot mau restart sekarang..."

# Jalankan ulang workflow via GitHub API
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GH_PAT" \
  https://api.github.com/repos/$GH_REPO/actions/workflows/bot.yml/dispatches \
  -d '{"ref":"main"}'
