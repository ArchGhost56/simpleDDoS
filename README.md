Below is the detailed README file for the ArchGhost56/simpleDDoS repository in English. This documentation was derived solely from the provided source code in simpleddos.py fileciteturn0file0.

──────────────────────────────
# ArchGhost56/simpleDDoS

A simple UDP flooding tool written in Python that demonstrates the basic principles of a DDoS attack. This repository contains a single Python script designed for educational purposes only. Use responsibly and only in controlled environments where you have permission.

---

## 🚀 Introduction

SimpleDDoS is a lightweight tool built using Python that sends a continuous stream of UDP packets to a target IP address on a specified port. Leveraging Python’s socket, time, and random libraries, the tool incrementally cycles through port numbers while transmitting random bytes, providing a straightforward example of how UDP-based flooding can be accomplished. The script uses terminal commands (including the "figlet" utility) to clearly display its state and progress. 

---

## ✨ Features

- **UDP Flooding:** Utilizes a UDP socket to send packets continuously to the target.
- **Dynamic Port Cycling:** Automatically increments the port number with each sent packet, resetting when reaching a high port value.
- **Terminal Art Integration:** Employs external tools (like figlet) to enhance terminal output aesthetics.
- **Lightweight and Simple:** Demonstrates the basics of creating a network traffic generator using Python.
- **Interactive Input:** Prompts the user for the target IP and initial port number.

---

## 📋 Requirements

| **Requirement**              | **Description**                                           |
|------------------------------|-----------------------------------------------------------|
| **Python Version**           | Python 2.x (the script uses Python 2 syntax)             |
| **Operating System**         | Linux/Unix systems (clear command and figlet are used)   |
| **Dependencies**             | - Python standard libraries: os, time, socket, random, datetime <br> - External utility: figlet                   |

*Note:* Ensure that the "figlet" command-line tool is installed and available in your system PATH.

---

## ⚙️ Installation

1. **Clone the Repository:**

   Open your terminal and run:
   ```
   git clone https://github.com/ArchGhost56/simpleDDoS.git
   ```
2. **Navigate to the Repository Directory:**
   ```
   cd simpleDDoS
   ```
3. **Install Figlet:**  
   On Debian-based systems:
   ```
   sudo apt-get install figlet
   ```
   On other systems, refer to your package manager’s instructions.

4. **Ensure Python 2 is installed:**  
   Check your Python version by running:
   ```
   python --version
   ```

---

## 🏃 Usage

1. **Run the Script:**  
   In the terminal, execute:
   ```
   python simpleddos.py
   ```
2. **Follow the Prompts:**

   - **TARGET IP:** Enter the target IP address.
   - **PORT:** Enter the desired starting port number.
   
   The script clears the screen and displays a series of visual banners (via figlet) before initiating the attack. It then proceeds to send UDP packets continuously, incrementing the port number with each sent packet. When the port number reaches 65534, it resets to 1, continuing the cycle indefinitely.

3. **Monitor the Output:**  
   The terminal will display a live count of the packets sent and the port being targeted for each transmission.

---

## ⚙️ Configuration

The tool was designed with simplicity in mind, and while there is minimal configuration, here’s how you can adjust it:

- **Packet Size:**  
  The size of the UDP packet is controlled by the line:
  ```
  bytes = random._urandom(1490)
  ```
  Change the value 1490 to modify the packet size.

- **Port Increment Logic:**  
  The script automatically increments the target port on every packet sent. To change the port cycling logic, modify the section within the `while True:` loop:
  ```
  port = port + 1
  if port == 65534:
      port = 1
  ```
- **Terminal Commands:**  
  Modify or remove calls to `os.system("clear")` and `os.system("figlet ...")` if you wish to change or standardize the terminal output.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, additional features, or bug fixes, please feel free to contribute:

- **Fork the Repository:**  
  Create your personal fork to experiment with changes.
- **Submit a Pull Request:**  
  When your changes are ready, open a pull request with a clear description of your modifications.
- **Open Issues:**  
  If you encounter any bugs or have feature requests, please open an issue detailing your findings.

Please adhere to the code style present in the original file and ensure that your changes align with the overall simplicity and educational nature of the project.

---
