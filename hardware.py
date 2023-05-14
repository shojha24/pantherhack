import cv2
import time
import datetime
import os
import requests
import base64
import pygame
import random

cap = cv2.VideoCapture(0)
pygame.init()
pygame.mixer.music.set_volume(0.5)


def convert_to_64(img_path):
    with open(img_path, 'rb') as f:
        img_data = f.read()
        encoded_img = base64.b64encode(img_data).decode('utf-8')
        
    return encoded_img

def camera_feed():
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite(f'curr.png', frame)
    return 'curr.png'

while True:
    encoded_img = convert_to_64(camera_feed())
    
    url = 'http://9169-69-119-107-111.ngrok-free.app/get_img'
    
    now = datetime.datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M:%S')
              
    response = requests.get(url, json={"image": encoded_img, "time": date_time})
        
    print(response.status_code, response.content)
    
    """if random.randint(0, 5) == 3:
        pygame.mixer.music.load("arhan.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass"""
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(1)

cap.release()
cv2.destroyAllWindows()