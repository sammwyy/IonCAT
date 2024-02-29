# 🐱‍👤 IonCAT

Input/Output Network Catapult (IonCAT) is a Multi layered network stress tool. It is capable of sending large amounts of traffic to a target, which can be used to exhaust the target's resources. IonCAT is a powerful and flexible HTTP/HTTPS, TCP/UDP, and ICMP. It can be used to generate and send packets to a target, and it can be used to test the target's network performance.

This tool was created for educational purposes only. I do not take any responsibility for the misuse of this tool.

## 💻 Setup

```bash
# Clone the repository.
git clone https://github.com/sammwyy/ioncat

# Go to the repository.
cd ioncat

# Install the requirements.
pip install -r requirements.txt
```

## 📚 Usage

```bash
python ioncat <options> COMMAND <flags>
```

**Options:**

| Option | Short | Description | type | Default |
| ------ | ----- | ----------- | :--: | :-----: |
| `--headless` | `<none>` | Headless mode (no colors or format) | bool | False |
| `--proxies` | `<none>` | File with proxies to use | str | `data/proxies.txt` |
| `--unsafe` | `<none>` | Allow non-proxy connections | bool | False |

> You must use options before command.

**Commands:**

| Command | Description | Options |
| ------- | ----------- | ------- | ------- |
| `fastclose` | Fast open/close streams to the target | `method`, `threads`, `uas` |
| `http` | HTTP/HTTPS flood | `bypass`, `method`,`random-body`, `threads`, `uas` |
| `slowloris` | A lot of low traffic established connections | `bypass`, `method`, `sockets`, `threads`, `uas` |

**Flags:**

| Flag | Short | Description | type | Default |
| ------ | ----- | ----------- | :--: | :-----: |
| `--bypass` | `-b` | Mimics a real browser and bypass WAFs | bool | False |
| `--method` | `-m` | HTTP method to use | str | GET |
| `--random-body` | `-r` | Randomizes the body of the request | bool | False |
| `--sockets` | `-s` | Simultaneous connections | int | 64 |
| `--threads` | `-t` | Number of threads to use | int | (System cpu cores) |
| `--uas` | `-u` | File with random user-agents to use | str | `data/user-agents.txt` |

> Note: All flags are optional. You must use flags after the command.

## 🤝 Contributing

Contributions, issues and feature requests are welcome!
Feel free to check [issues page](https://github.com/sammwyy/ioncat/issues).

## ❤️ Show your support

Give a ⭐️ if this project helped you! Or buy me a coffee-latte 🙌 [Ko-fi](https://ko-fi.com/sammwy)

## 📝 License

Copyright © 2024 [Sammwy](https://github.com/sammwyy).
This project is [MIT](LICENSE) licensed.
