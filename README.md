# Smart Oxygen Level Controller (SOLC)



## Table of Contents

1. Background
2. Motivation for SOLC
3. About the Authors
4. Solution Overview
5. Detailed Working and Output
6. Conclusion
7. Exhibits



## Background

 In Dec 2019, the world saw the start of the COVID-19 epidemic, which grew into a pandemic. The corona virus was first detected in China and spread across the world. In 2022 it mutated into Omicron virus. This virus targets the lungs primarily and leads to difficulty in breathing. As part of the treatment Medical agencies actively monitor the blood oxygen levels for percent saturation of oxygen in blood (SPO2 levels) to decide on treatment. Based on the severity of the infection, a COVID-19 patient might be provided an external source of Oxygen to avoid respiratory failure. This led to an unprecedented demand for Oxygen cylinders, which most countries struggled to meet resulting in large number of deaths.

# Motivation for SOLC

 Smart Oxygen Level Controller (SOLC) was motivated by the fact that it was possible to better utilize or optimize oxygen consumption thereby making it available for more Covid 19 patients. Additionally, freeing up continuous medical supervision by doctors and nurses to vary the oxygen flow, resulting in benefits to patients, who would not have received medical care. 

## About the Authors

#### Rahul Chenny

#### Ananya Chenny Rahul

#### Dhruv Chenny Rahul



## Solution Overview

 SOLC is a logic gate driven controller that regulates the flow of oxygen to meet a patient’s needs. Based on the input it can automatically increase or decrease oxygen flow and hence is dynamic by design and leads to apt Oxygen usage. 

![01_SolutionOverview](/Users/rachenny/git_clone/solc/images/01_SolutionOverview.png)

​                                                        *Figure 1: Overview of the system*

## Building Blocks

 

**Input:** A Pulse Oximeter acts as a sensor to continuously measure the SPO2 levels of the patient and provides the input to the next stage Process. Typically, the oximeter is clipped to a patient’s index finger to detect the SPO2 level and send the detected value. 
 *Note*: In this project a *Raspberry Pi 3* has been used to *simulate* a pulse oximeter. A *python* program processes the input values and generates the output for processing.

 

**Process**: The Smart Oxygen Level Controller (SOLC) process the digital inputs from the Oximeter (Raspberry Pi 3) and sends the output to activate the right control levels in the regulator. An input value of “0 0” results in the processing such that an output value of 1 is sent to the “Level 0” of the regulator. 

 

**Output**: The Regulator is a digital device connected to both SOLC and the Oxygen cylinder. Pre-calibrated  levels are activated to ensure the right level i.e. flow of oxygen Liters per minute (or hour). Based on SOLC output one of the regulator levels i.e. 0, 1, 2 and 3 will be activated. 
 *Note*: In this project the 4 color Light Emitting Diodes (LEDs) represent different levels on the regulator. The table show below associates the input to process to a digital 1 signal that goes to the corresponding LED.

|      | **Input (SP02 Range)** | **Process (Diagnosis)** | **Regulator  (Activate Level for flow)** |
| ---- | ---------------------- | ----------------------- | ---------------------------------------- |
| 1    | >=95 <=100             | **Normal**              | **Level  0** - Stop flow                 |
| 2    | >=91 <=94              | **Mild Hypoxemia**      | **Level  1**: 2 Litres per minute        |
| 3    | >=86 <=90              | **Moderate**            | **Level  2**: 4 Litres per minute        |
| 4    | >=30 < 85              | **Severe**              | **Level  3**: 6 Litres per minute        |

## Detailed Working and Output

 The figure below depicts the physical components of the solution.

<img src="/Users/rachenny/git_clone/solc/images/02_End_to_end_Solution.png" alt="02_End_to_end_Solution" style="zoom:200%;" />

​                                                                    *Figure 2: End to End Solution*

| **Component Name**: **Raspberry Pi 3 (Oximeter)**            |
| ------------------------------------------------------------ |
| **#1** (refer to Figure 2) It is a minicomputer with Linux operating system. It  also runs a python program in a continuous loop that enables a user to enter  the SPO2 levels. Once a user enters a value, it checks if the entry is valid  i.e. between >=30 and <=100.   Based on the value entered  it sets the value of the General Purpose input Output (GPIO) pins as shown in  **#2** (refer to Figure 2) either to **0,0** or **0,1** or **1,0**  or **1,1**. Each GPIO pin can be set to either send an output or receive  an input. The **physical pins** used for this project are # 11 (or GPIO  17) and # 13 (or GPIO 27) and are set  to Output value 0 or 1. Please see **solc.py** for the complete Python  Program |

![02_GPIO_ConnectivityToGates](/Users/rachenny/git_clone/solc/images/03_GPIO_ConnectivityToGates.png)

​                                                            *Figure 3: GPIO connectivity to Gates*



| **Component Name**: **SOLC**                                 |
| ------------------------------------------------------------ |
| The GPIO output serves as  the input to SOLC. The design of SOLC processes the inputs to ensure the  right Level of the regulator gets activated. SOLC uses the following Logic  Gates  <br />**NOT Gate** –  **#3** (refer to Figure 2) SOLC uses a count of 4 NOT gates  that are built into Integrated Chip (IC) SN54HC04. It takes one input and  inverts the value.   <br />**AND Gate** – SOLC also uses 3 AND gates that are built  into the IC 74HC08. It’s has 4 or Quad AND Gates built into the chip. For  each Gate it accepts 2 inputs and has one output. Its placement is shown in  **#4** (refer to Figure 2) in the figure above. Please see **Exhibit 1** for Pin  Configuration for both the gates.       <br /> The diagram below shows how the Logic gates are interconnected. Please see **Exhibit 2** for Pin  Connectivity Map.  Explanation of the  scenario noted above:  <br />**Input**: Value of 96 (SPO2) is sent. The Python program  analyses the range and sends a 0,0 via GPIO Pins across SOLC <br /> **Process**: In the first set of Logic Gates the 0, 0 are processed by the  NOT Gates resulting in the value of 1,1.  These 1,1 values are provided as input to the AND Gate and the output of 1 is  sent to the Level 0 of the regulator. Since an SPO2 of 96 is normal therefore  the regulator stops the Oxygen supply and   provides normal air to the patient. <br />**Output**: In the absence of a real digital regulator, the  Green LED lights up.     For the remaining gates,  the AND Gates receives values of 1,0 or 0,1 or 00 (Not shown) and hence the  output the AND Gate is 0. This means Regulator level 1, 2 and 3 receive a 0  value. |

<img src="/Users/rachenny/git_clone/solc/images/04_GPIO_SOLC.png" alt="04_GPIO_SOLC" style="zoom:250%;" />

​                                            *Figure 4: Logic Gate Connection*

| **Component Name** : **LEDs (Regulator Inputs)**             |
| ------------------------------------------------------------ |
| **#5** (refer to Figure 2) Shows 4 LEDs on the right side in  the picture. Each LED represents a level on the regulator. Based on the SOLC  output only one LED lights up, which in reality would activate or enable a specific  level in the regulator i.e. other Level inputs would receive 0. |

## **Conclusion**

SOLC is a cheap yet effective solution for conserving oxygen. Its benefits include

- **Cost**: The total cost of SOLC was less than INR 100/- (Excluding the cost of Rasberry Pi)
- **Simplicity**: It uses commonly available Logic Gates.
- **Accuracy**:  The present solution can be realized with higher accuracy by using AND gates with more number of inputs can be used. 

## Exhibits

#### **Exhibit 1**: Pin  Configuration 

**NOT Gate** (IC SN54HC04)

<img src="/Users/rachenny/git_clone/solc/images/05_NOT_Gate.png" alt="05_NOT_Gate" style="zoom:150%;" />

**AND Gate** (IC 74HC08)

<img src="/Users/rachenny/git_clone/solc/images/06_AND_Gate.png" alt="06_AND_Gate" style="zoom:150%;" />

#### **Exhibit 2**: Pin  Connectivity

<img src="/Users/rachenny/git_clone/solc/images/07_Pin_Connectivity.png" alt="07_Pin_Connectivity" style="zoom:200%;" />

As an illustration, **Pin  11** or GPIO 17 connects with **Pin 1** of NOT Gate, which connects with **Pin 1** of AND Gate. The output is tapped from **Pin 3** and sent to the LED.