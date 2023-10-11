import filters as ft
import os
import time
import numpy as np
    
while True:
    os.system("cls")
    print("Welcome to FILTER DESIGNER TOOL (Electrónica 3) \n Select the type of filter you want to design: \n 1. Low-pass \n 2. High-pass \n 3. pass-band SK \n 4. pass-band MFB")
   
    try:
        sel=0
        sel=int(input("filter type: "))
        if sel == 1:
            os.system("cls")
            print("Your select Low-Pass Filter \n Insert the values for a1, b1, c1, c2, fc: ")
            fc=float(input("cut-off frequency in Hz: "))
            c1=float(input("capacitor 1: "))
            c2=float(input("capacitor 2: "))
            a1=float(input("Coef. a1: "))
            b1=float(input("Coef. b1: "))
            
            [r1,r2]=ft.low_pass(c1,c2,a1,b1,fc)
            os.system("cls")
            print("This is your filter design")
            print(f"R1 = [{int(r1)} Ohm's] | R2 = [{int(r2)} Ohm's]")
            print(f"C1 = [{np.format_float_scientific(c1)} F] | C2 = [{np.format_float_scientific(c2)} F]")
            print(f"Cut-off Frequency = [{np.format_float_scientific(fc,2)} Hz]")
            salir=input("Press enter for continue")
            
        if sel==2:
            os.system("cls")
            print("Your select High-Pass Filter \n Insert the values for a1, b1, c1, c2, fc: ")
            fc=float(input("cut-off frequency in Hz: "))
            c=float(input("capacitor: "))
            a1=float(input("Coef. a1: "))
            b1=float(input("Coef. b1: "))
            [r1,r2]=ft.high_pass(c,a1,b1,fc)
            
            os.system("cls")
            print("This is your filter design")
            print(f"R1 = [{int(r1)} Ohm's] | R2 = [{int(r2)} Ohm's]")
            print(f"C1 = [{np.format_float_scientific(c)} F]")
            print(f"Cut-off Frequency = [{np.format_float_scientific(fc,2)} Hz]")
            salir=input("Press enter for continue")
        if sel==3:
            print("Your select Pass-band Filter \n Insert the values for fm, C, Q, Ra: ")
            fm=float(input("Average frequency: "))
            c=float(input("Capacitors: "))
            q=float(input("Quality factor: "))
            ra=float(input("Ra: "))
            [r,rf,g,a]=ft.pass_band_just(fm,c,q,ra)
            os.system("cls")
            print("This is your filter design")
            print(f"R = [{int(r)} Ohm's]")
            print(f"Rf = [{int(rf)}] Ohm's")
            print(f"Ra = [{int(ra)} Ohm's]")
            print(f"C = [{np.format_float_scientific(c)} F]")
            print(f"average frequency = [{np.format_float_scientific(fm,2)} Hz]")
            print(f"G = [{g}]")
            print(f"A=[{a}]")
            print(f"Quality factor = [{q}]")
    
            salir=input("Press enter for continue")
        if sel == 4:
            print("Your select Pass-band Filter \n Insert the values for Fm, Am, C, Q: ")
            Fm=float(input("Average frequency: "))
            Am=float(input("Average gain: "))
            Q=float(input("Quality factor: "))
            C=float(input("Capacitor: "))
            [R2,R1,R3]=ft.pass_band_mfb(Am,Fm,C,Q)
            os.system("cls")
            print(f"Average frequency: {Fm}")
            print(f"Average gain: {Am}")
            print(f"Quality factor: {Q}")
            print(f"Capacitor: {C}")
            print(f"Resistencias | R1 = {R1} | R2 = {R2} | R3 = {R3} |")
            salir=input("Press enter for continue")
            
    except:
        print("You have entered an invalid acction")
        time.sleep(2)
        os.system("cls")
    
