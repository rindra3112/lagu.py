import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nGedene cintaku luar biasa", 0.12),
        ("Jelas paling tulus sak dunia", 0.11),
        ("Walau kadang gawe aku kelaran", 0.13),
        ("opo wae tak tabrak yang menjadi penghalang\n", 0.08),
        ("tresno tekan matiku mung sampean", 0.11),
        ("raono muntire lehku berjuang", 0.12),
        ("kudu dadi siji ora urusan", 0.11),
        ("sampai pada tujuan tuhan mohon izinkan\n", 0.09),
    ]
    
    delays = [0.3, 4.0, 7.5, 9.0, 12.0, 15.0, 19.0, 20.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()