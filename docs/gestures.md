# Kinetic Control Gestures (v1.0)

Welcome to the documentation for the Kinetic Control system. This guide outlines the single-handed (right-hand) gestures used to interact with the system, built around a dynamic and intuitive "Kinetic Mode."

## Core Philosophy

The system is designed to be both powerful and deliberate. It avoids accidental commands by requiring the user to first enter an active state (`Kinetic Mode`). Once active, the system interprets fine-motor movements and distinct poses as commands.

---

## 1. Activation: Entering Kinetic Mode

This is the gateway to all other controls.

* **Gesture:** 🖐️ **Palm Facing Camera**
* **Action:** Hold your open palm towards the camera for one second.
* **Result:** Activates `Kinetic Mode`. A UI indicator will confirm the system is now listening for commands. The mode remains active for 5 seconds and the timer resets after each successful command.

---

## 2. Dynamic Controls

These gestures rely on smooth, continuous motion tracking while in `Kinetic Mode`.

### Volume Control 🔊
* **Gesture:** 👆 **Index Finger Vertical Movement**
    * **Move Up:** Raises the system volume.
    * **Move Down:** Lowers the system volume.
* **Note:** The control is based on the *velocity* of the movement, not the absolute position on screen, allowing for fluid adjustments.

### Zoom Control 🔍
* **Gesture:** 🤏 **Thumb & Index Finger Distance**
    * **Pull Apart:** Zooms in.
    * **Pinch Together:** Zooms out.
* **Note:** This action is initiated by starting with the thumb and index finger close together. The system maps the normalized distance between them to a precise zoom level.

---

## 3. Static Poses & Navigation

These are distinct, static hand shapes used for common actions within `Kinetic Mode`.

* **Pause Media:** ✊ **Closed Fist**
* **Play / Resume Media:** 👍 **Thumbs Up**

### Navigation Sub-Mode
This special mode is used for cycling through tracks, tabs, or workspaces.

1.  **Engage Navigation:** 👊 **Show the Back of Your Fist** to the camera. The system will confirm entry into this sub-mode.
2.  **Navigate Right / Next:** 👍 **Extend Thumb to the Right**.
3.  **Navigate Left / Previous:** **Extend Pinky to the Left**.

---

## 4. Standalone & Universal Commands

These gestures work outside of the standard `Kinetic Mode`.

### Initiate Sleep ("I'll be back") 😴
* **Gesture:** 🤙 **"Call Me" Sign**
* **Action:** Triggers a 5-second countdown to put the system to sleep. This command can be given at any time.

### Universal Cancel ("Escape Hatch") 🛑
* **Gesture:** ✋ **Flat Palm (Stop Sign)**
* **Action:** Immediately exits `Kinetic Mode` or any sub-mode and cancels any active countdowns (like Sleep). Use this as a universal "stop listening" command.