import os
import sys
import time

# Typing effect
def typing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)
    print()

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Clear screen
os.system("clear")

print(GREEN + """
 █████╗ ███╗   ███╗██╗████████╗   ██╗   ██╗████████╗
██╔══██╗████╗ ████║██║╚══██╔══╝   ╚██╗ ██╔╝╚══██╔══╝
███████║██╔████╔██║██║   ██║        ╚████╔╝    ██║
██╔══██║██║╚██╔╝██║██║   ██║         ╚██╔╝     ██║
██║  ██║██║ ╚═╝ ██║██║   ██║          ██║      ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝          ╚═╝      ╚═╝

        >>> AMIT YT DOWNLOADER PRO <<<
""" + RESET)

typing(CYAN + "Initializing system..." + RESET)
time.sleep(1)

# ✅ SAVE PATH (BEST for Gallery)
save_path = "/storage/emulated/0/YT VIDEO"

if not os.path.exists(save_path):
    os.makedirs(save_path)

typing(GREEN + "[✔] Storage Ready" + RESET)

while True:
    print(MAGENTA + "\n====================================" + RESET)

    link = input(CYAN + "[+] Enter YouTube / Facebook: " + RESET)

    if link.lower() == "exit":
        typing(RED + "\n[✖] Exiting..." + RESET)
        break

    typing(YELLOW + "\n[⚡] Fetching video info..." + RESET)
    time.sleep(1)

    typing(YELLOW + "[⚡] Downloading HIGH QUALITY video." + RESET)

    # ✅ SMART FORMAT (High Quality + Compatible)
    command = f'''yt-dlp -f "bv*[vcodec^=avc1]+ba[acodec^=mp4a]/b[ext=mp4]" \
--merge-output-format mp4 \
-o "{save_path}/%(title)s.%(ext)s" "{link}"'''

    result = os.system(command)

    if result != 0:
        typing(RED + "\n[✖] Download Failed! Check link or internet." + RESET)
        continue

    # ✅ Force full media scan (Gallery fix)
    os.system('am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///storage/emulated/0/')

    typing(GREEN + "\n[✔] Download Complete!" + RESET)
    typing(CYAN + f"[📁] Saved in: {save_path}" + RESET)

    choice = input(YELLOW + "\n[?] Download another? (y/n): " + RESET)

    if choice.lower() != 'y':
        typing(RED + "\n[✖] Session Ended 😎" + RESET)
        break

print(GREEN + "\n>>> Powered by AMIT YT 🔥 <<<\n" + RESET)
