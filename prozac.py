import cv2
import numpy as np
import pyautogui
import win32api
import serial
import dxcam
from colorama import Fore, Style
from time import sleep

# Settings
COM_PORT = "COM5"  # The COM port number for your Arduino. This can be found in the Device Manager.
X_FOV = 100  # Field of view for the X-axis.
Y_FOV = 100  # Field of view for the Y-axis.
AIM_KEY = 0x02  # Key code for aim task. See https://t.ly/qtrot for full key codes.
TRIGGER_KEY = 0x12  # Key code for trigger task. See https://t.ly/qtrot for full key codes.
X_SPEED = 0.5  # Speed of mouse movement along the X-axis. Lower values make it slower.
Y_SPEED = 0.5  # Speed of mouse movement along the Y-axis. Lower values make it slower.
AIM_OFFSET = 7 #Higher value will make it aim lower
LOWER_COLOR = [140, 120, 180]
UPPER_COLOR = [160, 200, 255]
camera = dxcam.create(output_idx=0, output_color="BGR") # Initialize the camera with settings

class Prozac:
    def listen(self):
        while True:
            if win32api.GetAsyncKeyState(AIM_KEY) < 0:
                self.run("aim")
            if win32api.GetAsyncKeyState(TRIGGER_KEY) < 0:
                self.run("click")

    def run(self, task):
        hsv = cv2.cvtColor(Capture().get_screen(), cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array(LOWER_COLOR), np.array(UPPER_COLOR))
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(mask, kernel, iterations=5)
        thresh = cv2.threshold(dilated, 60, 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if contours:
            screen_center = (X_FOV // 2, Y_FOV // 2)
            min_distance = float('inf')
            closest_contour = None

            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                center = (x + w // 2, y + h // 2)
                distance = ((center[0] - screen_center[0]) ** 2 + (center[1] - screen_center[1]) ** 2) ** 0.5

                if distance < min_distance:
                    min_distance = distance
                    closest_contour = contour

            x, y, w, h = cv2.boundingRect(closest_contour)
            cX = x + w // 2
            top_most_y = y + AIM_OFFSET

            x_offset = cX - screen_center[0]
            y_offset = top_most_y - screen_center[1]

            if task == "aim":
                Mouse().move(x_offset * X_SPEED, y_offset * Y_SPEED)

            if task == "click":
                if abs(x_offset) <= 3 and abs(y_offset) <= 7: #Dirty implementation of a trigger bot. This may be refined later.
                    Mouse().click()

class Mouse:
    def __init__(self):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 0
        self.serial_port.port = COM_PORT
        try:
            self.serial_port.open()
        except serial.SerialException:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Failed to connect because the specified COM port was not found.")
            sleep(10)

    def move(self, x, y):
        self.serial_port.write(f'{x},{y}\n'.encode())

    def click(self):
       self.serial_port.write('CLICK\n'.encode())

class Capture:
    def __init__(self):
        monitor_size = pyautogui.size()
        self.region = self.calculate_region(monitor_size)

    def calculate_region(self, monitor_size):
        x_center = monitor_size.width // 2
        y_center = monitor_size.height // 2
        left = x_center - X_FOV // 2
        top = y_center - Y_FOV // 2
        right = left + X_FOV
        bottom = top + Y_FOV
        return left, top, right, bottom

    def get_screen(self):
        while True:
            screenshot = camera.grab(region=self.region)
            if screenshot is not None:
                return np.array(screenshot)
