The scanned files will be automatically saved in the “E” directory with the name dat-w.txt change this section to adjust:

if __name__ == "__main__":
    wifi_data = get_wifi_passwords()
    save_to_file(wifi_data, 'E', 'dat-w.txt')
