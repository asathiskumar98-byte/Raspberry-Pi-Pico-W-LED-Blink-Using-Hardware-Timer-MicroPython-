# ⏱ Raspberry Pi Pico W – LED Blink Using Hardware Timer (MicroPython)

Demonstrates periodic LED blinking using **hardware timers** instead of software delays.  
This allows the Pico to multitask while the LED toggles automatically.

---

## ⚙️ Hardware Setup
| Component | Pico Pin | Description |
|------------|-----------|-------------|
| LED | GPIO16 | Output |
| GND | GND | Ground |

---

## 🧠 Concept
The **`machine.Timer`** module triggers a callback at fixed intervals.  
Here, it toggles the LED every 1 second (`period=1000 ms`).

---

## 🚀 Run the Code
1. Open **Thonny IDE**  
2. Copy this code to your Pico W as `main.py`  
3. The LED blinks once per second without using `sleep()`  

---

## 💡 Try Next
- Change blink rate by adjusting `period`  
- Use two timers to blink two LEDs asynchronously  
- Combine with sensors for event-based feedback
