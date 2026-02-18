import socket

def check_rtsp_port(ip, port=554, timeout=2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((ip, port)) == 0

if __name__ == "__main__":
    print("[*] RTSP Discovery Module loaded.")
