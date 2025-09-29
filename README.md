# Kinetic Controls

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-in%20development-orange.svg)

A Python application that allows you to control your computer's media, volume, and system functions using hand gestures through your webcam. It leverages real-time computer vision to provide a futuristic, touchless interface for your machine.



---

## Features

* **Real-time Hand Tracking:** Utilizes the MediaPipe library for fast and accurate detection of hand landmarks.
* **Kinetic Mode:** An activation-based system to prevent accidental commands.
* **Dynamic Controls:**
    * **Volume:** Adjust by moving your index finger up or down.
    * **Zoom:** Control zoom levels by changing the distance between your thumb and index finger.
* **Media & Navigation:**
    * Play/Pause media.
    * Navigate to the next/previous track or tab using a unique fist-based gesture.
* **System Commands:** Put your computer to sleep with a simple, distinct gesture.

---

## Installation

This project requires **Python 3.10 or newer**.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ADPer0705/gesture-controls.git
    cd gesture-controls
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Linux/macOS
    python3.10 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install .
    ```

---

## Usage

Once the installation is complete, run the main application from the root directory:

```bash
python src/main.py
```

Ensure your webcam is uncovered and you are in a well-lit area for best performance. Press `q` to close the application window.

---

## Gesture Reference
A detailed guide to all available gestures and how to perform them can be found in the **[Gesture Documentation](https://github.com/ADPer0705/gesture-controls/blob/main/docs/gestures.md)**.

---

## Configuration

You can customize core settings, such as the default camera index and gesture sensitivity thresholds, by modifying the `config/settings.yaml` file.

---

## Contributing

Contributions, issues, and feature requests are welcome! Please feel free to check the issues page to see if you can help out.

### Committing & pushing

If you'd like to make changes and push them back to your fork or this repository, a simple workflow is:

```bash
# create a new branch for your work
git checkout -b my-feature

# make changes, then stage and commit
git add .
git commit -m "Describe your changes"

# push the branch to GitHub
git push -u origin my-feature
```

---

## License

Distributed under the MIT License.