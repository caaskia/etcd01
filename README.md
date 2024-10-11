# Etcd01

# Async etcd  Watcher and Subprocess Manager

This project is an asynchronous watcher for etcd using the `aetcd` client library. It listens for changes in a specific etcd key (`rec-service`), and based on the value (`start` or `stop`), it triggers or stops a subprocess. The script also includes a dummy work task to demonstrate concurrent task execution.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Asynchronous etcd key watcher using `aetcd`.
- Triggers subprocess execution based on the value of a specific etcd key.
- Logs events and subprocess output using Python’s logging module.
- Handles errors and allows graceful task cancellation.
- Includes an example of a dummy task running concurrently with the etcd watcher.

---


## Installation
sudo apt install etcd-server

uv pip uninstall protobuf
uv pip install protobuf==3.20.3


### Prerequisites

- Python 3.7+
- etcd instance (v3.0+)

### Clone the Repository

```bash
git clone https://github.com/yourusername/etcd-watcher-subprocess.git
cd etcd-watcher-subprocess

