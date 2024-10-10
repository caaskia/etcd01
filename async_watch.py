import asyncio
import logging
import subprocess

import aetcd

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


async def watch_callback(event):
    # Check the kind of event and process accordingly
    if event.kind == aetcd.rtypes.EventKind.PUT:
        if event.kv.key == b"rec-service":
            if event.kv.value == b"start":
                print("Starting process...")
                # subprocess.Popen(['your_process_command'])  # Запускает процесс
                response = subprocess.getoutput("ip a")
                logger.info(response)
            elif event.kv.value == b"stop":
                print("Stop process...")
                # Here, you could add logic to stop your process if needed


async def main():
    client = aetcd.Client()

    # Start watching the 'rec-service' key
    watch = await client.watch(b"rec-service")  # Await the watch coroutine

    print('Watching for "rec-service"...')
    async for event in watch:
        await watch_callback(event)  # Call the callback for each event


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopping watch...")
