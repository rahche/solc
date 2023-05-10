"""
Program to emulate an analog input from
oxygen meter
"""
import RPi.GPIO as GPIO
import time

#mode
GPIO.setmode(GPIO.BOARD)

#PINS GPIO INPUT
INPUT_VALUE_1 = 11
INPUT_VALUE_2 = 13

#PINS GPIO SEVERE. OWING TO LIMITED SPACE
SEVERE_VALUE_1 = 16

# SETUP I/O PINS
GPIO.cleanup()
int_spo2_reading = -1;

# fixed variables
INT_NORMAL_SP02_START_RANGE = 95
INT_NORMAL_SP02_END_RANGE = 100

# MILD HYPOXEMIA
INT_MILD_HYPOXEMIA_START_RANGE = 91
INT_MILD_HYPOXEMIA_END_RANGE = 94
INT_MILD_OXYGEN_FLOW_RATE_LITRESPERMINUTE = 2

# MODERATE HPOXEMIA
INT_MODERATE_HYPOXEMIA_START_RANGE = 86
INT_MODERATE_HYPOXEMIA_END_RANGE = 90
INT_MODERATE_OXYGEN_FLOW_RATE_LITRESPERMINUTE = 4

# SEVERE HYPOXEMIA
INT_SEVERE_HYPOXEMIA_START_RANGE = 30
INT_SEVERE_HYPOXEMIA_END_RANGE = 85
INT_SEVERE_OXYGEN_FLOW_RATE_LITRESPERMINUTE = 6

GPIO.setup(INPUT_VALUE_1, GPIO.OUT)
GPIO.setup(INPUT_VALUE_2, GPIO.OUT)
GPIO.setup(SEVERE_VALUE_1, GPIO.OUT)

while int_spo2_reading != 0:

    # Step 1: Ask for SPO2 value
    int_spo2_reading = int(input("Please enter the SPO2 value between 30 and 100? Press 0 to exit: "))
    print("DEBUG: You entered: ", int_spo2_reading)

    if int_spo2_reading == 0:
        break
    else :
        GPIO.output(INPUT_VALUE_1, 1)
        GPIO.output(INPUT_VALUE_2, 1)
        GPIO.output(SEVERE_VALUE_1, 0)
    # Step 2: Process SPO2 level, Send signal to GPIO pins
    if int_spo2_reading >= INT_NORMAL_SP02_START_RANGE and int_spo2_reading <= INT_NORMAL_SP02_END_RANGE:
        print(int_spo2_reading, "Result: NORMAL. No oxygen required.")
#        GPIO.setup(INPUT_VALUE_1, GPIO.OUT)
#        GPIO.setup(INPUT_VALUE_2, GPIO.OUT)
        GPIO.output(INPUT_VALUE_1, 0)
        GPIO.output(INPUT_VALUE_2, 0)
    elif int_spo2_reading >= INT_MILD_HYPOXEMIA_START_RANGE and int_spo2_reading <= INT_MILD_HYPOXEMIA_END_RANGE:
        print(int_spo2_reading, "Result: MILD HYPOXEMIA. Changing Oxygen rate to ", INT_MILD_OXYGEN_FLOW_RATE_LITRESPERMINUTE, " Litres per minute")
#        GPIO.setup(INPUT_VALUE_1, GPIO.OUT)
#        GPIO.setup(INPUT_VALUE_2, GPIO.OUT)
        GPIO.output(INPUT_VALUE_1, 0)
        GPIO.output(INPUT_VALUE_2, 1)
    elif int_spo2_reading >= INT_MODERATE_HYPOXEMIA_START_RANGE and int_spo2_reading <= INT_MODERATE_HYPOXEMIA_END_RANGE:
        print(int_spo2_reading, "Result: MODERATE HYPOXEMIA. Changing Oxygen rate to ", INT_MODERATE_OXYGEN_FLOW_RATE_LITRESPERMINUTE, " Litres per minute")
#        GPIO.setup(INPUT_VALUE_1, GPIO.OUT)
#        GPIO.setup(INPUT_VALUE_2, GPIO.OUT)
        GPIO.output(INPUT_VALUE_1, 1)
        GPIO.output(INPUT_VALUE_2, 0)
    elif int_spo2_reading >= INT_SEVERE_HYPOXEMIA_START_RANGE and int_spo2_reading <= INT_SEVERE_HYPOXEMIA_END_RANGE:
        print(int_spo2_reading, "Result: SEVERE HYPOXEMIA. Changing Oxygen rate to ", INT_SEVERE_OXYGEN_FLOW_RATE_LITRESPERMINUTE, " Litres per minute")
#        GPIO.setup(INPUT_VALUE_1, GPIO.OUT)
#        GPIO.setup(INPUT_VALUE_2, GPIO.OUT)
#        GPIO.output(INPUT_VALUE_1, 1)
#        GPIO.output(INPUT_VALUE_2, 1)
#        GPIO.setup(SEVERE_VALUE_1, GPIO.OUT)
        GPIO.output(SEVERE_VALUE_1, 1)
    else :
        print("INVALID READING. Note: Press 0 to Exit")

# Step 3: Send cleanup to GPIO pins
print("*************************SOLC stopped. Thank you***************************")
GPIO.cleanup()