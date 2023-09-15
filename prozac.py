
import cv2
import numpy as np
import pyautogui
import win32api
import serial
import dxcam

#Settings
COM_PORT = "COM5" #com port number of your arduino, can be found in device manager.
X_FOV = 100 #field of veiw for the x axis.
Y_FOV = 100 #same thing but for the y axis.
AIM_KEY = 0x02 #Check https://t.ly/qtrot for full key-codes.
X_SPEED = 1  #speed of the mouse movement, lower = slower.
Y_SPEED = 0.3  #same thing but for the y axis.
LOWER_COLOR = np.array([140, 110, 150]) 
UPPER_COLOR = np.array([150, 195, 255])
 
class Prozac:

    def listen(self):
        while True:
            if win32api.GetAsyncKeyState(AIM_KEY) < 0:
                self.run()
                
    def run(self):
        hsv = cv2.cvtColor(Capture().get_screen(), cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)
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
            center = (x + w // 2, y + h // 2)
            cX = center[0]
            cY = y + (h * 0.2)
            cYcenter = center[1] - Y_FOV // 2
            x_diff = cX - X_FOV // 2
            y_diff = cY - Y_FOV // 2

            Mouse().move(x_diff * X_SPEED, y_diff * Y_SPEED)

class Mouse:
    def __init__(self):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 0
        self.serial_port.port = COM_PORT
        self.serial_port.open()

    def move(self, x, y):
        self.serial_port.write(f'M{x},{y}\n'.encode())
        while self.serial_port.in_waiting == 0:
            pass
        self.serial_port.read(self.serial_port.in_waiting)

camera = dxcam.create(output_idx=0, output_color="BGR")

class Capture:
    def __init__(self):
        Monitor_Size = pyautogui.size()
        X_CENTER = Monitor_Size.width // 2
        Y_CENTER = Monitor_Size.height // 2
        left = X_CENTER - X_FOV // 2
        top = Y_CENTER - Y_FOV // 2
        right = left + X_FOV
        bottom = top + Y_FOV
        self.region = (left, top, right, bottom)

    def get_screen(self):
        while True:
            screenshot = camera.grab(region=self.region)
            if screenshot is None:
                continue
            return np.array(screenshot)
