# ARP Spoofer

Lightweight Python scripts for ARP spoofing and network target scanning using Scapy.

## Requirements

- Python 3.x
- Scapy library
- Npcap (required on Windows for packet sniffing and sending)

## Installation Guide
### Quick Start:
```bash
git clone https://github.com/Samsharya/ARPspoofer.git && cd ARPspoofer && pip install -r requirements.txt && python ARPv2.py
```

### Step 1: Clone the Repository

Open your terminal or command prompt and clone the repository, or navigate to your project folder:

bash

```bash
git clone https://github.com/Samsharya/ARPspoofer.git
cd ARPspoofer
```

### Step 2: Install Dependencies

Install Scapy and other required dependencies using pip:

bash

```bash
pip install -r requirements.txt
```

**Note:** Windows users must download and install [Npcap](<https://npcap.com/>) with **"Support WinPcap API-compatible mode"** enabled so Scapy can interact with the network adapter.

---

## Usage

### Option 1: Lite Version (Manual Input)

Prompts you to enter the gateway and target IP addresses manually, fetches their MAC addresses, and starts the spoofing process.

bash

```bash
python ARP-spoofer-list.py
```

### Option 2: V2 (Auto Scan & Target Selection)

Automatically detects your gateway, scans the subnet for active hosts, highlights your own machine with `[me]`, allows you to select a target from a numbered list, and starts the spoofer.

bash

```bash
python ARPv2.py
```

---

## Disclaimer

This project is intended for educational purposes and authorized network testing only.
Do not use it on networks or devices without proper authorization.