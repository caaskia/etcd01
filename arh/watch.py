import etcd3
import subprocess
import time


def watch_callback(event):
    # Iterate through each event in the WatchResponse
    for ev in event.events:
        if ev.key == b"start-requested":
            print("Starting process...")
            # subprocess.Popen(['your_process_command'])  # Запускает процесс


if __name__ == "__main__":
    client = etcd3.client()

    # Add a watch callback for the key 'start-requested'
    watch_id = client.add_watch_callback(b"start-requested", watch_callback)

    try:
        print('Watching for "start-requested"...')
        while True:
            time.sleep(1)  # Sleep to reduce CPU usage in the infinite loop
    except KeyboardInterrupt:
        print("Stopping watch...")
        client.cancel_watch(watch_id)
