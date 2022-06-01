#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """
**Menu Bantuan Admin**

`/pause` atau `/cpause`
• Untuk menjeda streaming di Voicechat.

`/resume` atau `/cresume`
• Untuk melanjutkan streaming yang dijeda.

`/mute` atau `/cmute`
• Untuk membisukan streaming di Voicechat.

`/unmute` atau `/cunmute`
• Untuk membunyikan streaming di Voicechat.

`/skip` atau `/cskip`
• Untuk melewati streaming di Voicechat.

`/stop` atau `/cstop`
• Untuk menghentikan streaming di Voicechat.

`/shuffle` atau `/cshuffle`
• Untuk mengacak antrian aktif.

`/skip` atau `/cskip` - (angka)
• Untuk melewati streaming secara spesifik.

`/loop` atau `/cloop` - (angka)
• Untuk melakukan pengulangan streaming yang diputar.

`/auth` - balas pesan atau username
• Untuk menambahkan pengguna menjadi Pengguna Resmi.

`/unauth` - balas pesan atau username 
• Untuk menghapus pengguna dari Daftar Pengguna Resmi.

`/authusers`
• Untuk memeriksa pengguna yang masuk dalam Daftar Pengguna Resmi.
"""


HELP_2 = """
** Menu Bantuan Streaming**

`/play` - Judul atau tautan
• Untuk memutar musik ataupun video di Voicechat.

`/vplay` - Judul atau tautan 
• Untuk memutar video di Voicechat.

`/cplay` - Judul atau tautan 
• Untuk memutar streaming di Voicechat saluran.

`/channelplay` - ID Channel
• Untuk menghubungkan grup anda dengan Voicechat channel.

`/playlist`
• Untuk mengecek daftar putar yang anda simpan di Server Bot.

`/deleteplaylist`
• Untuk menghapus track yang ada di daftar putar yang anda simpan di Server Bot.

`/play`
• Untuk memutar track di daftar putar yang anda simpan di server, untuk memainkan Top 10 Lagu Trend di server, untuk mengatur mode pemutaran.

`/seek` - Waktu dalam detik
• Untuk melewati durasi sesuai perintah.

`/restart`
• Untuk memulai ulang bot jika terjadi bug.
"""


HELP_3 = """
**Panduan Dasar**

• Tambahkan bot ini ke grup atau channel dan berikan izin admin.
• Cek menu `/help` untuk mendapatkan informasi perintah.
• Jika akun asisten tidak bergabung otomatis silahkan hubungi @justcontactbot.
• Jika akun asisten tidak bergabung di Voicechat, lakukan `/restart` untuk me-refresh.

• Kamu dapat memutar musik dalam dua **mode pencarian** i.e. Mode Langsung dan Mode Sebaris.\n\nUbah mode melalui /playmode"
• Kamu dapat memutar musik dalam dua **jenis bermain** i.e. Mode Semua Orang dan Mode Admin.\n\nUbah mode melalui /playmode"
• Kamu Anda dapat memutar musik di **saluran** juga.\n\nMengatur channel_id melalui /channelplay dan bermain melalui /cplay "
• Non Admin juga dapat menggunakan perintah admin dengan menambahkannya ke** DAFTAR PENGGUNA AUTH**. \nTambahkan pengguna mana pun ke daftar autentikasi dengan /auth , hapus dengan /unauth dan periksa pengguna autentik melalui /authusers"
• Bot memiliki fitur yang disebut **Modus Bersih**.\nIni menghapus pesan bot setelah 5 Menit dan memastikan obrolan Anda tetap bersih.\n\nEnable atau disable mode bersih dari /settings [__Enabled by default__]"
• Kamu bisa bermain **Spotify** trek dan daftar putar juga.\n\nMulai bermain sekarang dengan /play [Tautan Spotify]"
• Kamu bisa bermain **Apple Musik** trek dan daftar putar juga.\n\nMulai bermain sekarang dengan /play [Tautan Apple]"
• Kamu bisa bermain **Musik Resso** trek dan daftar putar juga.\n\nMulai bermain sekarang dengan /play [Tautan Resso]"
• Kamu bisa bermain **Sound Cloud** trek dan daftar putar juga.\n\nMulai bermain sekarang dengan /play [Tautan SoundCloud]"
• Kamu bisa bermain **Videos** dalam obrolan suara melalui /vplay [Nama Video] atau /play -v [Nama Video]"
• Anda dapat mengatur **Kualitas Audio** obrolan suara ke Rendah, Sedang atau Tinggi.\n\nTetapkan kualitas melalui /settings"
• Anda dapat mengatur **Kualitas video** obrolan suara ke Rendah, Sedang atau Tinggi.\n\nTetapkan kualitas melalui /settings"
• Anda dapat memeriksa **Statistik** di bot seperti Top 10 Lagu yang Dimainkan.\n\nDapatkan Statistik: /gstats "
• Anda dapat memeriksa **Statistik Grup** di bot seperti Top 10 Lagu yang Dimainkan.\n\nDapatkan Statistik: /gstats "
• Anda sekarang dapat membisukan musik yang diputar di obrolan suara.\n\nMemerintah: /mute"
• Kamu bisa membisukan dan membunyikan streaming. Gunakan perintah `/mute` atau `/unmute`
• Kamu bisa mencari lirik musik. Gunakan perintah `/lyrics` - Judul.
• Kamu bisa mengunduh musik di YouTube Server. Gunakan perintah `/song` - Judul atau tautan.
• Bot menyimpan semua track yang pernah diputar di semua grup pengguna. Gunakan perintah `/play`.
• Kamu bisa mengacak antrian yang berlangsung. Gunakan perintah `/shuffle`.
• Kamu bisa melihat antrian yang sedang berlangsung. Gunakan perintah `/queue`.
• Kamu bisa merubah bahasa sesuai selera. Gunakan perintah `/lang`.
• Kamu bisa melakukan perintah stream secara paksa, itu akan menghentikan track yang berjalan sementara. Gunakan perintah `/playforce` - Judul.
"""

HELP_4 = """
**Fitur Canggih**

`/stats`
• Untuk membuka statistik server bot.

`/lyrics` - Judul
• Untuk mencari lirik musik sesuai kueri.

`/song` - Judul atau tautan 
• Untuk mengunduh lagu melalui server YouTube.

`/queue` atau `/cqueue`
• Untuk memeriksa antrian yang sedang berlangsung.

`/start`
• Untuk memulai bot.

`/help`
• Untuk membuka penjelasan perintah.

`/ping`
• Untuk melakukan pinging server bot.

`/settings`
• Untuk mengatur setelan bot.

`/speedtest`
• Untuk melakukan tes kecepatan di web server.

`/set` - Waktu dalam detik + Nama jadwal
• Untuk membuat sesi reminder berbasis teks.

`/helptag`
• Untuk membuka penjelasan perintah mention member.
"""
