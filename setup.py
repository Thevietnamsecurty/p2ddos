nhập hệ điều hành

in("""
\x1b[38;2;255;20;147m 
   _                     _  ___ _____ ___           __      ___      __                  _____            _ 
  /_\  _ __   ___  _ __ / |/ _ \___  / _ \/\   /\/\ \ \    /   \___ / _| __ _  ___ ___  /__   \___   ___ | |
 //_\\| '_ \ / _ \| '_ \| | (_) | / / (_) \ \ / /  \/ /   / /\ / _ \ |_ / _` |/ __/ _ \   / /\/ _ \ / _ \| |
/  _  \ | | | (_) | | | | |\__, |/ / \__, |\ V / /\  /   / /_//  __/  _| (_| | (_|  __/  / / | (_) | (_) | |
\_/ \_/_| |_|\___/|_| |_|_|  /_//_/    /_/  \_/\_\ \/   /___,' \___|_|  \__,_|\___\___|  \/   \___/ \___/|_|
                                                                                                            

\x1b[38;2;255;20;147m
\x1b[38;2;255;20;147m\x1b[38;2;0;255;58m>(thiết lập)
""")

print("""[0] pip\n[1] pip3\nBạn dùng cái nào?""")

c = đầu vào(">>>:")
nếu c == "0":
    os.system("pip cài đặt cloudcraper")
    os.system("pip cài vớ")
    os.system("pip cài pysocks")
    os.system("pip cài đặt colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip cài đặt httpx")

yêu tinh c == "1":
    os.system("pip3 cài đặt cloudcraper")
    os.system("vớ cài đặt pip3")
    os.system("pip3 cài pysocks")
    os.system("pip3 cài đặt colorama")
    os.system("cài đặt pip3 không bị phát hiện_chromedriver")
    os.system("pip3 cài đặt httpx")
nếu os.name == "nt":
    đi qua
khác:
    os.system("wget ​​https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

in ("Xong.")