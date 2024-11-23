import tkinter as tk
import serial
import threading

class SerialReader:
    def __init__(self, port, baudrate):
        self.serial = serial.Serial(port, baudrate)
        self.running = True

    def read_data(self, callback):
        while self.running:
            line = self.serial.readline().decode('utf-8').strip()
            if line:
                callback(line)

    def stop(self):
        self.running = False
        self.serial.close()

def update_gui(data):
    adc1_value, adc2_value = data.split(" ADC2: ")
    adc1_value = adc1_value.split("ADC1: ")[1]
    adc1_label.config(text=f"ADC1: {adc1_value}")
    adc2_label.config(text=f"ADC2: {adc2_value}")

def start_reading():
    serial_reader = SerialReader('COM10', 115200)  # Remplace 'COM3' par le port série de ton ESP32-S3
    thread = threading.Thread(target=serial_reader.read_data, args=(update_gui,))
    thread.start()

    def on_closing():
        serial_reader.stop()
        thread.join()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

root = tk.Tk()
root.title("ESP32-S3 ADC Reader")

adc1_label = tk.Label(root, text="ADC1: ")
adc1_label.pack()

adc2_label = tk.Label(root, text="ADC2: ")
adc2_label.pack()

start_button = tk.Button(root, text="Start Reading", command=start_reading)
start_button.pack()

root.mainloop()
