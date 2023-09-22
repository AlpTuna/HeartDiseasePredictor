from os import error
import tkinter
from tkinter import Radiobutton, font
from tkinter.constants import E, W
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main

window = tkinter.Tk()
tkinter.Label(window, text='Welcome to Heart Disease Predicter').grid(row=0,column =0,sticky = W)

# Age
tkinter.Label(window, text='Enter your age: ').grid(row=1,column =0,sticky=W)
ageBox = tkinter.Entry(window)
ageBox.grid(row=1,column=1,sticky=W)

# Gender
genderVariable = IntVar()
tkinter.Label(window, text='Choose your gender: ').grid(row=2,column =0,sticky=W)

femaleButton = Radiobutton(window,text='Female', variable = genderVariable, value= 0)
femaleButton.grid(row=2,column=1,sticky=W)

maleButton = Radiobutton(window,text='Male', variable = genderVariable, value= 1)
maleButton.grid(row=2,column=1)

# Chest Pain Type
tkinter.Label(window, text='Chest Pain Type: ').grid(row=3,column =0,sticky=W)

chestPainTypeBox = ttk.Combobox(window, values = ['Typical Angina (TA)', 'Atypical Angina (ATA)',
                                                    'Non-Anginal Pain (NAP)', 'Asymptomatic (ASY)'])
chestPainTypeBox.grid(row=3,column =1,sticky=W)

# Resting Blood Pressure
tkinter.Label(window, text='Resting Blood Pressure (mm Hg): ').grid(row=4,column =0,sticky=W)
pressureBox = tkinter.Entry(window)
pressureBox.grid(row=4,column=1,sticky=W)

# Cholesterol
tkinter.Label(window, text='Cholesterol (mm/dl): ').grid(row=5,column =0,sticky=W)
cholesterolBox = tkinter.Entry(window)
cholesterolBox.grid(row=5,column=1,sticky=W)

# Fasting Blood Sugar
BSVariable = IntVar()
tkinter.Label(window, text='Fasting Blood Sugar').grid(row=6,column =0,sticky=W)

lowBSButton = Radiobutton(window,text='Lower than 120', variable = BSVariable, value= 0)
lowBSButton.grid(row = 6,column = 1,sticky= W)

highBSButton = Radiobutton(window,text='Higher than 120', variable = BSVariable, value= 1)
highBSButton.grid(row = 6,column = 1)

# Resting Electrocardiogram Results 
tkinter.Label(window, text='Resting Electrocardiogram Results: ').grid(row=7,column =0,sticky=W)

ECGBox = ttk.Combobox(window, values = ['Normal', 'ST(Having ST-T wave abnormality)',
                                        "LVH(showing probable or definite left ventricular hypertrophy by Estes' criteria)"],
                                        width=50)
ECGBox.grid(row=7,column=1,sticky=W)

# Maximum heart rate achieved
tkinter.Label(window, text='Maximum heart rate achieved:').grid(row=8,column =0,sticky=W)
heartRateBox = tkinter.Entry(window)
heartRateBox.grid(row=8,column =1,sticky=W)

# Exercise-induced angina
AnginaVariable = IntVar()
tkinter.Label(window, text='Exercise-Induced Angina:').grid(row=9,column =0,sticky=W)

noAnginaButton = Radiobutton(window,text='No', variable = AnginaVariable, value= 0)
noAnginaButton.grid(row = 9,column = 1,sticky= W)

yesAnginaButton = Radiobutton(window,text='Yes', variable = AnginaVariable, value= 1)
yesAnginaButton.grid(row = 9,column = 1)

# Oldpeak
tkinter.Label(window, text='Oldpeak (Numeric value measured in depression):').grid(row=10,column =0,sticky=W)
oldPeakBox = tkinter.Entry(window)
oldPeakBox.grid(row=10,column=1,sticky=W)

# The slope of the peak exercise ST segment
tkinter.Label(window, text='The slope of the peak exercise ST segment:').grid(row=11,column =0,sticky=W)
slopeTypeBox = ttk.Combobox(window, values = ['Up(Upslopping)', 'Flat(Flat)',
                                                    'Down(Downslopping)'])
slopeTypeBox.grid(row=11,column = 1,sticky=W)



ST_Slope_Encode = {'Down(Downslopping)': 0, 'Flat(Flat)' : 1, 'Up(Upslopping)': 2}
RestingECG_Encode = {"LVH(showing probable or definite left ventricular hypertrophy by Estes' criteria)": 0, 'Normal' : 1,
                        'ST(Having ST-T wave abnormality)' : 2}
ChestPainType_Encode =  {'Asymptomatic (ASY)': 0, 'Atypical Angina (ATA)' : 1, 'Non-Anginal Pain (NAP)' : 2,'Typical Angina (TA)':3}

class Patient(): # This class can later be used for creating profiles and saving them. Now it's not that important.
    def __init__(self,age,gender,PainType,BP,Cholesterol,BS,ECG,MHR,Angina,Oldpeak,Slope):
        self.age = age
        self.gender = gender
        self.PainType = PainType
        self.BP = BP
        self.Cholesterol = Cholesterol
        self.BS = BS
        self.ECG =ECG
        self.MHR = MHR
        self.Angina = Angina
        self.Oldpeak = Oldpeak
        self.Slope = Slope
    def MakePrediction(self):
        attributes = [self.age,self.BP,self.Cholesterol,self.BS,self.MHR,self.Oldpeak,self.gender,self.PainType,self.ECG,self.Angina,self.Slope]
        messagebox.showinfo(title = 'Result',message = main.Predict(attributes))


def CheckInputs():
    errorFound = True
    if not ageBox.get().isnumeric(): # Checks age
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to Age. Please enter a number.')
    elif not pressureBox.get().isnumeric(): # Checks Blood Pressure
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to Blood Pressure. Please enter a number.')
    elif not cholesterolBox.get().isnumeric(): # Checks Cholesterol
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to Cholesterol. Please enter a number.')
    elif not heartRateBox.get().isnumeric(): # Checks HeartRate
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to Maximum Heart Rate. Please enter a number.')
    elif not oldPeakBox.get().isnumeric(): # Checks Oldpeak
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to Oldpeak. Please enter a number.')
    elif chestPainTypeBox.get() not in ['Typical Angina (TA)', 'Atypical Angina (ATA)', 'Non-Anginal Pain (NAP)', 'Asymptomatic (ASY)']: # Checks ChestPainType
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to Chest Pain Type. Please choose one of the options.')
    elif ECGBox.get() not in ['Normal', 'ST(Having ST-T wave abnormality)', "LVH(showing probable or definite left ventricular hypertrophy by Estes' criteria)"]: # Checks ECG
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to ECG Results. Please choose one of the options.')
    elif slopeTypeBox.get() not in ['Up(Upslopping)', 'Flat(Flat)', 'Down(Downslopping)']: # Checks Slope
        messagebox.showerror(title = 'Invalid Input',message = 'You entered an invalid answer to The Slope. Please choose one of the options.')
    else:
        errorFound = False
    return errorFound

def GetInputs():
    if not CheckInputs(): # If there is an invalid input, this function will not be called.
        age = ageBox.get()
        gender = genderVariable.get()
        painType = chestPainTypeBox.get()
        painType_n = ChestPainType_Encode[painType] # Turns to numerical value
        BPressure = pressureBox.get()
        choles = cholesterolBox.get()
        BSugar = BSVariable.get()
        ECGResult = ECGBox.get()
        ECGResult_n = RestingECG_Encode[ECGResult]
        HRate = heartRateBox.get()
        anginaVar = AnginaVariable.get()
        oldPeakVar = oldPeakBox.get()
        slopeVar = slopeTypeBox.get()
        slopeVar_n = ST_Slope_Encode[slopeVar]

        print(age,gender,painType,BPressure,choles,BSugar,ECGResult,HRate,anginaVar,oldPeakVar,slopeVar,painType_n,ECGResult_n,slopeVar_n)

        

        newPatient = Patient(age,gender,painType_n,BPressure,choles,BSugar,ECGResult_n,HRate,anginaVar,oldPeakVar,slopeVar_n)
        newPatient.MakePrediction()

# Create the Predict Button
predictButton = Button(window,text='Predict',command=GetInputs)
predictButton.grid(row=12,column=0,sticky=W)

window.mainloop()