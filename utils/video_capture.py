import cv2
import numpy as np
import pyautogui
from datetime import datetime
from utils.myquiz import *
import os

def start_video_capture(name, violation_queue,stop_event):
    reference = None
    video = cv2.VideoCapture(0)
    # cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Live", 480, 270)

    movement_count = 0
    max_movements = 5
    last_movement_time = None
    movement_interval = 5

    while not stop_event.is_set():
        _, frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if reference is None:
            reference = gray
            continue

        diff = cv2.absdiff(reference, gray)
        thresh_frame = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
        cnts, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        movement_detected = False

        for c in cnts:
            if cv2.contourArea(c) < 10100:
                continue

            current_time = datetime.now()
            if last_movement_time is None or (current_time - last_movement_time).total_seconds() >= movement_interval:
                movement_detected = True
                last_movement_time = current_time
                cv2.putText(frame, 'MOVEMENT DETECTED!!', (10, 30), cv2.FONT_ITALIC, 1, (255, 0, 0), 1)
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if movement_detected:
            movement_count += 1
            violation_queue.put(movement_count)
            if movement_count > max_movements:
                print("Maximum movements exceeded. Exiting...")
                break

        cv2.putText(frame, f"Violations: {movement_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # cv2.imshow("Difference Frame", diff)
        cv2.imshow("Coloured frame", frame)
        # cv2.imshow("Binary frame", thresh_frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
