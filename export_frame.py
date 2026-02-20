import time

def dump_last_frame(channel_name):
    timestamp = int(time.time())
    print(f"[*] Exporting frame from {channel_name} at {timestamp}...")

if __name__ == "__main__":
    dump_last_frame("cam_01")
