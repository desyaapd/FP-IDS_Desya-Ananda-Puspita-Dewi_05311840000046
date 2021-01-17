#!/usr/bin/python3

# Import Library yang diperlukan
import subprocess # Untuk menjalankan fungsi subprocess
from time import sleep, time # Untuk menjalankan fungsi sleep
from datetime import datetime # Untuk menjalankan fungsi date
from twilio.rest import Client # Untuk menjalankan fungsi twilio

# Menampilkan banner program
print ("""
  ____       _       _        _ _                _       
 |  _ \  ___| |_ ___| | _____(_) |    ___   __ _(_)_ __  
 | | | |/ _ \ __/ _ \ |/ / __| | |   / _ \ / _` | | '_ \ 
 | |_| |  __/ ||  __/   <\__ \ | |__| (_) | (_| | | | | |
 |____/ \___|\__\___|_|\_\___/_|_____\___/ \__, |_|_| |_| FP-046
                                           |___/         
""")

# Set sid dan auth token akun twilio user, lihat di https://www.twilio.com/console
account_sid = 'TWILIO_ACCOUNT_SID' # TWILIO_ACCOUNT_SID
auth_token = 'TWILIO_AUTH_TOKEN' # TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

# Fungsi intruder berisi syntax send message twilio 
def intruder():

    message = client.messages.create( 
                                body="\U0001F6E1 Ada penyusup!", # Pesan notifikasi yang ingin dikirim
                                from_='whatsapp:+14155238886', # Nomor whatsapp bot twilio   
                                to='whatsapp:+WA_NUMBER' # Nomor whatsapp user
                            )
    print("[!] Notifikasi terkirim") # Menandakan notifikasi berhasil terkirim
    sleep(5) # Program dijeda selama 5 detik

# Fungsi scan berisi pendeteksi login attempts pada device
def scan():

    # While akan menjalankan fungsi terus menerus hingga user melakukan keyboard interupt (ctrl + c) 
    while True :
        output = subprocess.check_output('lastb -s -5sec', shell=True) # Menyimpan output dari perintah lastb ke variabel "output". lastb menampilkan informasi percobaan login yang mencurigakan
        conv = str(output) # Mengubah tipe data pada variabel "output" menjadi string, kemudian menyimpannya ke variabel "conv"
        timevalue = datetime.now() # Melihat waktu saat ini
        dt_string = timevalue.strftime("%H:%M") # Menyimpan data waktu tadi ke variabel "dt_string" dengan format jam:menit

        # Mengecek apakah selama 5 detik terakhir terdapat percobaan login yang mencurigakan
        if dt_string in conv: # Jika string pada variabel "dt_string" terdapat pada variabel "conv", maka...
            print ("[!] Terdeteksi!") # terdeteksi percobaan login yang mencurigakan
            intruder() # Fungsi notifikasi twilio dijalankan
        else: # Jika pernyataan tadi salah, maka...
            #print ("[o] Aman") # Device terpantau aman
            sleep(5) # Program dijeda selama 5 detik
            


# Fungsi utama berisi pemanggilan fungsi scan
if __name__ == "__main__":
    scan()
