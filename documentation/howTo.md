# Matrix | Deployment & Installation Guide

This guide covers everything you need to know  on how to get the **Matrix Display** running on your own hardware. Choose one of the methods down below that suits you the best.

---

## Method 1: The Docker Route (Recommended)
*Best for Homelabs, Servers, and standard Raspberry Pi deployments.*

Because this project includes both a Python backend and a web frontend, Docker is the easiest way to spin it up without installing Python dependencies directly onto your machine.

**1. Clone the Repository**
```bash
git clone [https://github.com/REALSDEALS/matrix-display.git](https://github.com/REALSDEALS/matrix-display.git)
```

**2. Building the Docker Instance**
```bash
cd matrix-display
docker build -t matrix-display .
docker run -d -p 9090:5000 --name matrixdp matrix-display
```
After running these commands you should be able to visit the display in your browser, in case you have followed the instructions on: http://YOUR_LOCAL_MACHINE_IP:9090

## Method 2: Local Python

**1. Clone the Repository**
```bash
git clone [https://github.com/REALSDEALS/matrix-display.git](https://github.com/REALSDEALS/matrix-display.git)
```

**2. Move in to the Folder**
```bash
cd matrix-display
```

**3A. For Linux or MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

**3B. For Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**4. Starting the Script:**
For Linux or MacOS:
```bash
python3 app.py
```

For Windows:
```bash
python app.py
```
After running these commands you can visit the display in your webbrowser at: http://localhost:5000
- If you want to close the script, go to your terminal where you are running this from and do `ctrl+c`.

## Method 3: Kiosk Mode on Raspberry Pi Display
It is optimized for the 7-inch display*

If you want your Raspberry Pi to display the matrix, you can tell its default web browser to launch the app in full-screen, "Kiosk" mode on boot. This hides the URL bar, tabs, and mouse cursor so that you will have the matrix soley on your display.

Assuming you have the Docker container (Method 1) already running in the background on your Pi, open your Pi's terminal and run:

```bash
chromium-browser --kiosk http://localhost:9090
```
If you want to exit the kiosk mode = alt+F4 or Ctrl+W

**Autostart on Boot:**
If you would like to make it autostart on booting the Pi you could do the following:

```bash
nano ~/.config/lxsession/LXDE-pi/autostart
```

Add the following line to the bottom of the file:
- `@chromium-browser --kiosk http://localhost:9090`

And the last step is to save the file and to reboot your Pi.

#### GitHub Matrix by REALSDEALS, Licensed under MIT.