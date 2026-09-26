# Foltz WBS 🔔

![Python](https://img.shields.io/badge/Python-3-blue) ![Requests](https://img.shields.io/badge/requests-2.32-green) ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Termux-orange) ![License](https://img.shields.io/badge/license-MIT-yellow)

**Foltz WBS** is an interactive Python tool to manage and use webhooks efficiently: add, list, verify and delete webhooks, plus send bulk messages to the configured webhooks.

**Language:** [Português](README.md) • English (this file) • [Español](README.es.md)

## Summary

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Structure](#structure)
- [Getting started](#getting-started)
- [How to use](#how-to-use)
- [Customization](#customization)
- [License](#license)
- [Contact](#contact)

## Features

- Add new webhooks
- Delete existing webhooks
- List all saved webhooks
- Verify that webhooks are working
- Send bulk messages to webhooks
- Custom ASCII banners
- Typewriter effect in the terminal

## Prerequisites

- **Python 3.x** installed
- **pip** to install dependencies (`colored`, `requests`)

## Structure

```
FoltzWBS/
├── LICENSE
├── README.md
└── foltz-wbs/
    ├── main.py                  # main script (interactive menu)
    ├── requirements.txt         # dependencies (colored, requests)
    ├── install_requirements.bat # installs dependencies (Windows)
    ├── start.bat                # starts the program (Windows)
    ├── webhooks.txt             # saved webhooks
    └── ascii_banners/           # customizable banners
```

## Getting started

Follow these steps to install and use Foltz WBS on your system.

### Installation

#### Windows

1. **Clone the repository:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   ```

2. **Install dependencies:**

   Run the `install_requirements.bat` file:

   ```bash
   install_requirements.bat
   ```

3. **Start the script:**

   Run the `start.bat` file:

   ```bash
   start.bat
   ```

#### Linux

1. **Clone the repository:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**

   ```bash
   python main.py
   ```

#### Termux

1. **Install Python and Git:**

   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

2. **Clone the repository and install dependencies:**

   ```bash
   git clone https://github.com/foltzbr/FoltzWBS.git
   cd FoltzWBS/foltz-wbs
   pip install -r requirements.txt
   ```

3. **Run the script:**

   ```bash
   python main.py
   ```

## How to use

1. **Start Foltz WBS.**
2. **Pick an option from the menu:**
   - **Add Webhook**: add a new webhook URL (saved in `webhooks.txt`).
   - **Delete Webhook**: remove an existing webhook.
   - **List Webhooks**: see all saved webhooks.
   - **Verify Webhooks**: check that webhooks are working.
   - **Send Messages**: send bulk messages to webhooks.

## `.bat` files

- **`install_requirements.bat`**: installs the required libraries (`colored`, `requests`).
- **`start.bat`**: starts the main script.

## Customization

- **Banners**: customize banners by editing the files in `ascii_banners/`.
- **Text effect**: adjust the typewriter effect in the script as you like.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Questions or suggestions:

- **Foltz** - [GitHub](https://github.com/foltzbr)
