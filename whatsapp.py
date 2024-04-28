import random
import pyautogui as pg
import time
import keyboard  # to detect keypress for termination

message = "bs hogya ab ye lo"

# Wait for 8 seconds for you to navigate to the WhatsApp chat
time.sleep(8)

try:
    for i in range(1000):  # send "I am sorry" 50 times
        pg.write(message)
        pg.press("enter")
        time.sleep(0)  # add a small delay to avoid detection as spam
        if keyboard.is_pressed('q'):  # Press 'q' to stop the loop
            print("Process terminated by user.")
            break
except Exception as e:
    print(f"An error occurred: {e}")


print("Execution complete.")

     
    
   