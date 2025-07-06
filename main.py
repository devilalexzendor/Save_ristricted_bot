# Copyright (c) 2025 devgagan : https://github.com/devgaganin.
# Licensed under the GNU General Public License v3.0.

import asyncio
import importlib
import os
import sys
import signal

from shared_client import start_client

stop_event = asyncio.Event()

async def load_and_run_plugins():
    await start_client()
    plugin_dir = "plugins"
    plugins = [f[:-3] for f in os.listdir(plugin_dir) if f.endswith(".py") and f != "__init__.py"]

    for plugin in plugins:
        module = importlib.import_module(f"plugins.{plugin}")
        if hasattr(module, f"run_{plugin}_plugin"):
            print(f"Running {plugin} plugin...")
            await getattr(module, f"run_{plugin}_plugin")()

async def main():
    try:
        await load_and_run_plugins()
        print("Bot is running. Waiting for stop signal...")
        await stop_event.wait()
    except asyncio.CancelledError:
        print("Main task cancelled. Shutting down gracefully...")
    except Exception as e:
        print("Error occurred in main():", e)
    finally:
        print("Bot is shutting down cleanly.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    def handle_shutdown(signum, frame):
        print(f"Received signal {signum}. Shutting down gracefully...")
        stop_event.set()

    # Catch SIGTERM and SIGINT (Heroku sends SIGTERM)
    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGINT, handle_shutdown)

    print("Starting clients ...")
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Shutting down from KeyboardInterrupt...")
    except Exception as e:
        print("Error in __main__:", e)
    finally:
        try:
            loop.close()
        except Exception:
            pass

    sys.exit(0)
