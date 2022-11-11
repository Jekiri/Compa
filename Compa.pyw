#Default python modules
import random
import math
import time
import subprocess
import sys
import os
#Additional python modules
import tkinter as tk
from tkinter import font
from tkinter import StringVar
import psutil
import winreg
import steamfront
import customtkinter
from playsound import playsound
import webbrowser
import pyautogui


## Flag values -> 0 = Not purchased //// 1 = Purchased



#/------------------------------ToDo:-------------------------------------\
# V.2 Changes
#   Remove Play, Nap & Feed buttons
#   Add animation selection to 'Play' button
#   Remove 'Nap' button, replace with new feature ()
#   Remove 'Feed' button, replace with new feature ()
#/------------------------------End of ToDo:-------------------------------------\


sys.stdout = open("Logs\\outputlog.txt", "r+")
sys.stderr = open("Logs\\errorlog.txt", "r+")

tama_title = r"""
 ________  ________  _____ ______   ________  ________          ___      ___    _____     
|\   ____\|\   __  \|\   _ \  _   \|\   __  \|\   __  \        |\  \    /  /|  / __  \    
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \       \ \  \  /  / /  \/_|\  \   
 \ \  \    \ \  \\\  \ \  \\|__| \  \ \   ____\ \   __  \       \ \  \/  / /  \|/ \ \  \  
  \ \  \____\ \  \\\  \ \  \    \ \  \ \  \___|\ \  \ \  \       \ \    / /__      \ \  \ 
   \ \_______\ \_______\ \__\    \ \__\ \__\    \ \__\ \__\       \ \__/ /\__\      \ \__\
    \|_______|\|_______|\|__|     \|__|\|__|     \|__|\|__|        \|__|/\|__|       \|__|
    
"""





# /------------------------------Start of loading screen-------------------------------------\


def button_disable():
    with open("Brain\\Bin\\nameraw.txt", "r") as f:
        ndata = f.read()
        if ndata != "":
            buttonS.configure(state=tk.DISABLED)
            name_input.configure(state=tk.DISABLED)
        else:
            print("Waiting for name")


def name_finder():
    with open("Brain\\Bin\\nameraw.txt", "r") as f:
        global ndata
        ndata = f.read()
        if ndata != "":
            f.close()
            print('Name:'+ str(ndata))
            loadingscreen.destroy()
        else: 
            f.close()
            notificaiton = customtkinter.CTkLabel(loadingscreen, text="Please enter a name")
            notificaiton.pack()
            loadingscreen.update()
            name_checker()




def name_checker():
    global name_input
    with open("Brain\\Bin\\nameraw.txt", "r+") as f:
        global ndata
        ndata = f.read()
        if ndata == "":
            ndata = name_input.get()
            f.write(str(ndata))
            f.close()
            print('Name:'+ str(ndata))
        elif ndata != "":
            name_finder()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

loadingscreen = customtkinter.CTk()
loadingscreen.geometry("700x350")
loadingscreen.title("Compa-loader")
#loadingscreen.iconbitmap("Brain\\Bin\\icon.ico")
label = customtkinter.CTkLabel(loadingscreen, text=tama_title)
label.configure(font=("Courier", 10))
label.pack()



# /------------------------------Loading bar------------------------------\

loading_bar1 = """
Loading…
█▒▒▒▒▒▒▒▒▒

"""
loading_bar2 = """
Loading…
███▒▒▒▒▒▒▒

"""

loading_bar3 = """
Loading…
█████▒▒▒▒▒

"""
loading_bar4 = """
Loading…
███████▒▒▒

"""

loading_bar5 = """
Loading…
██████████

"""


#Loading bar display
loading_display2 = tk.StringVar(loadingscreen)
loading_display2.set((loading_bar1))

name_input = customtkinter.CTkEntry()
name_input.pack()
buttonS = customtkinter.CTkButton(loadingscreen, text="Submit", command=name_checker)
buttonS.pack()

spin = customtkinter.CTkLabel(loadingscreen, textvariable=loading_display2)
spin.pack()

button_disable()
buttonS.after(5000, name_finder)


def loading_bar():
    loading_display2.set((loading_bar2))
    loadingscreen.update()
    loadingscreen.after(1000 , loading_bar2f)

def loading_bar2f():
    loading_display2.set((loading_bar3))
    loadingscreen.update()
    loadingscreen.after(1000 , loading_bar3f)

def loading_bar3f():
    loading_display2.set((loading_bar4))
    loadingscreen.update()
    loadingscreen.after(1000 , loading_bar4f)

def loading_bar4f():    
    loading_display2.set((loading_bar5))
    loadingscreen.update()

    
# \------------------------------End of Loading bar------------------------------/


#close window after 4 ms, and run task function
loadingscreen.after(600, loading_bar)
#loading screen loop
loadingscreen.mainloop()

#Debug message
print(tama_title)
print("Loading...")
print("------------ Start up cycle -----------")





# \------------------------------End of loading screen-------------------------------------/



# /------------------------------Start of Main Window-------------------------------------\

#Tkinter wndow
def to_VIP_or_to_not_VIP():
    with open("Brain\\Flags\\flag8.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag8 is 1 - VIP title active")
        main_window.title("[VIP] - " + ndata)
    else:
        main_window.title(ndata)

main_window = customtkinter.CTk()
to_VIP_or_to_not_VIP()
main_window.geometry("400x300")




#Variables - Body
body_displaySP = """ (シ_ _)シ """, """ 人(_ _*) """, """ (ﾉ*･ω･)ﾉ """, """ (♡´౪`♡) """, """ ♡ඩ⌔ඩ♡ """
body_displayP = """ 〵(^ o ^)〴 """, """ ٩(^ᴗ^)۶ """, """ (づ｡◕‿‿◕｡)づ """, """ ༼ つ ◕_◕ ༽つ """, """ ᕦ(ò_óˇ)ᕤ """, """ ໒( ♥ ◡ ♥ )७ ~♪ """, """ ヽ(⌐■_■)ノ♪♬ """, """ ᕙ༼ ͝°益° ༽ᕗ """, """ o͡͡͡╮༼ ʘ̆ ۝ ʘ̆ ༽╭o͡͡͡ """, """ ୧☉□☉୨ """, """ (ง˙o˙)ว """
body_displayH = """ (≧∀≦) """, """ (☯ ᴥ ☯) """, """ (ᵔᴥᵔ) """, """ (ღ˘⌣˘ღ) """, """ ಠ‿↼ """, """ ʘ‿ʘ """, """ ☜(⌒▽⌒)☞ """, """ ƪ(˘⌣˘)ʃ """, """ (｡◕‿‿◕｡) """, """ ~(˘▾˘~) """, """ \ (•◡•) / """, """ ✧♡(◕‿◕✿) """, """ (.❁‿❁.) """, """ (・◠ 。◠・) """, """ (˵◡‿◡⑅) """, """ （＾∀＾） """
body_displayS = """ ᕙ(⇀‸↼‶)ᕗ """, """ (´・ω・`) """, """ (´・ω・`) """, """ ◔̯◔ """, """ ｡゜(｀Д´)゜｡ """, """ ｡ﾟ(ﾟ´(00)`ﾟ)ﾟ｡ """, """ ༼ つ ಥ_ಥ ༽つ """, """ ༼ಢ_ಢ༽ """, """ (ಥ﹏ಥ) """, """ ٩◔̯◔۶ """, """ (｡•́︿•̀｡) """, """ (⌣́_⌣̀) """, """ (ﾟ∩ﾟ) """, """ (╯︵╰,) """, """ ┴┬┴|_•`) """, """ (╥╯ᗝ╰╥) """
body_displayL = """ ¯\_ಠ_ಠ_/¯ """
body_displayE = """ ╰(𝓞Д𝓞)╯ """
body_displayD = """ ▬▬[]══༼ ಥ۝ಥ ༽══ﺤ """
#/------------------------------Body Actions-------------------------------------\
body_displayEating = """ 且_(ﾟ◇ﾟ；)ノﾞ """
body_displayEating2 = """ ~旦_(^O^ ) """
body_displayEating3 = """ (っ˘ڡ˘ς) """
body_displayPlaying = """ ︵‿︵‿︵‿ヽ(°□° )ノ"""
body_displayPlaying2 = """ ︵‿︵‿︵ヽ(òᴗó)ᔐ‿︵  """
body_displayPlaying3 = """ ︵‿︵‿ᔐ(òᴗó)ヽ︵‿ """
body_displayPlaying4 = """ ︵‿ヽ(òᴗó)ᔐ︵‿︵‿︵ """
body_displayPlaying5 = """ ＼(>o<)／︵‿︵‿︵‿︵"""
body_displaySleeping = """ ]▓▓[ꒉ¦) """
body_displaySleeping2 = """ ]▓▓[ꀦ¦) """
body_displaySleeping3 = """ ⌈▓͟⌉ꆟ)ꍞ """
body_display = tk.StringVar(main_window)
body_display.set((body_displayL))


#Variables
mood = 0 #Placeholder for mood increase
mood_display = tk.StringVar(main_window)
mood_increasev = False
generation = 0
generation_display = tk.StringVar(main_window)
age = 0
age_display = tk.StringVar(main_window)
pumped = None
happy = None
sad = None
enlightened = None


# /------------------------------Start of checkers-------------------------------------\
def mood_checker():
    global mood
    with open("Brain\\Bin\\moodraw.txt") as f:
        mdata = f.read()
        moodr = int(mdata)
        mood = moodr
        f.close()

        if mood < 0:
            mood = 50
            mood_file = open("Brain\\Bin\\moodraw.txt", "r+")
            mood_file.write(str(mood))
            mood_file.close()
            int(mood)

def gen_checker():
    global generation

    with open("Brain\\Bin\\generationraw.txt") as f:
        global gdata
        gdata = f.read()
        genr = int(gdata)
        generation = genr
        f.close()
        if generation == 0:
            generation = 1
            generation_file = open("Brain\\Bin\\generationraw.txt", "r+")
            generation_file.write(str(generation))
            generation_file.close()
            generation_display.set(("Gen: " + str(generation)))
        else:
            generation_display.set(("Gen: " + str(generation)))
    

        
        


def age_checker():
    with open("Brain\\Bin\\ageraw.txt") as f:
        global adata
        adata = f.read()
        age = adata
        f.close()
        age_display.set(("Age: " + str(age)))
        int(age)


def age_increaser():
    age = int(adata)
    age = age + 1
    age_file = open("Brain\\Bin\\ageraw.txt", "r+")
    age_file.write(str(age))
    age_file.close()
    int(age)
    w4.after(1500000, age_increaser)




# /------------------------------End of checkers-------------------------------------\\





#/------------------------------Start of mood function-------------------------------------\

mood_checker()


def mood_function(mood):
    global pumped
    global happy
    global sad
    global enlightened
    global mood_increasev
    global generation
    global points
    #save mood to file
    gen_checker()
    age_checker()
    mood_file = open("Brain\\Bin\\moodraw.txt", "r+")
    mood_file.write(str(mood))
    mood_file.close()
    age = open("Brain\\Bin\\ageraw.txt", "r")
    age = age.read()
    points =  open("Brain\\Bin\\pointsraw.txt", "r")
    points = points.read()

    def popup_window():
        popup = customtkinter.CTk()
        x = main_window.winfo_x()
        y = main_window.winfo_y()
        popup.geometry("420x400+" + str(x) + "+" + str(y))
        popup.resizable(False, False)
        popup.overrideredirect(True)
        def close():
            button_sound()
            popup.destroy()
            main_window.destroy()
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen("python3 Compa.pyw", startupinfo=startupinfo)
        with open ("Brain\\Bin\\nameraw.txt") as f:
            name = f.read()
            f.close()
        label = customtkinter.CTkLabel(popup, text="Max mood achieved..\nCongratulations!\n\nPoints have been awarded. Mood reset to Happy.\n"+ name +" will now restart!")
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        B1 = customtkinter.CTkButton(popup, text="Sweet!", command=close)
        B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        popup.mainloop()

    print("-------------- New cycle --------------")
    print('Name:'+ ndata)
    print("Mood:"+ str(mood))
    print('Age:'+ str(age))
    print("Generation:"+ str(generation))
    print("Points: " + str(points))
    print("-------------- End of cycle --------------")
    print("-------------- Updates --------------")
    int(mood)
    if mood_increasev == False:
        if mood != 0:
            if mood >= 600:
                sad = False
                happy = False
                pumped = False
                enlightened = True
                mood_display.set("Mood: " + "Enlightened")
                print("Max mood achieved, points awarded. Mood reset to Happy")
                mood = 200
                mood_file = open("Brain\\Bin\\moodraw.txt", "r+")
                mood_file.write(str(mood))
                mood_file.close()
                print("Updated Mood:"+ str(mood))
                points = int(points)
                earn_points_bulk()
                popup_window()
            elif mood >= 500 and mood < 600:
                sad = False
                happy = False
                pumped = False
                enlightened = True
                mood_display.set("Mood: " + "Enlightened")
                print(str(ndata)+" is enlightened")
                mood = mood - 1
                print("Updated Mood:"+ str(mood))
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
            elif mood >= 300 and mood < 500:
                sad = False
                happy = False
                enlightened = False
                pumped = True
                mood_display.set("Mood: " + "Pumped")
                mood = mood - 5
                print("Updated Mood:"+ str(mood))
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
            elif mood <= 100 and mood > 0:
                pumped = False
                happy = False
                enlightened = False
                sad = True
                mood_display.set("Mood: " + "Sad")
                mood = mood - 1
                print("Updated Mood:"+ str(mood))
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
            else:
                sad = False
                pumped = False
                enlightened = False
                happy = True
                mood_display.set("Mood: " + "Happy")
                mood = mood - 3
                print("Updated Mood:"+ str(mood))
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
        else:
            mood_display.set("Mood: " + "Dead")
            sad = False
            pumped = False
            happy = False
            enlightened = False
            generation = generation + 1
            generation_file = open("Brain\\Bin\\generationraw.txt", "r+")
            generation_file.write(str(generation))
            generation_file.close()
            int(generation)
            mood = mood - 1
            print("Updated Mood:"+ str(mood))
            mood = 200 #Reset mood
            print("Updated Mood:"+ str(mood))
            main_window.after(30000, mood_function, mood)
    elif mood_increasev == True:
        if mood != 0:
            if mood >= 600:
                sad = False
                happy = False
                pumped = False
                enlightened = True
                mood_display.set("Mood: " + "Enlightened")
                print("Max mood achieved, points awarded. Mood reset to Happy")
                mood = 200
                mood_file = open("Brain\\Bin\\moodraw.txt", "r+")
                mood_file.write(str(mood))
                mood_file.close()
                print("Updated Mood:"+ str(mood))
                earn_points_bulk()
                popup = customtkinter.CTk()
                x = main_window.winfo_x()
                y = main_window.winfo_y()
                popup.geometry("420x400+" + str(x) + "+" + str(y))
                popup.resizable(False, False)
                popup.overrideredirect(True)
                def close():
                    button_sound()
                    popup.destroy()
                    main_window.destroy()
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    subprocess.Popen("python3 Compa.pyw", startupinfo=startupinfo)
                with open ("Brain\\Bin\\nameraw.txt") as f:
                    name = f.read()
                    f.close()
                label = customtkinter.CTkLabel(popup, text="Max mood achieved..\nCongratulations!\n\nPoints have been awarded. Mood reset to Happy.\n"+ name +" will now restart!")
                label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
                B1 = customtkinter.CTkButton(popup, text="Sweet!", command=close)
                B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
                mood_increasev = False
                popup.mainloop()
            elif mood >= 500 and mood < 600:
                sad = False
                happy = False
                pumped = False
                enlightened = True
                mood_display.set("Mood(+): " + "Enlightened")
                print(str(ndata)+" is enlightened")
                mood = mood + 1
                print("Updated Mood(+):"+ str(mood))
                earn_points_single(10)
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
                mood_increasev = False
            elif mood >= 300 and mood < 500:
                sad = False
                happy = False
                enlightened = False
                pumped = True
                mood_display.set("Mood(+): " + "Pumped")
                mood = mood + 3
                print("Updated Mood(+):"+ str(mood))
                earn_points_single(5)
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
                mood_increasev = False
            elif mood <= 100 and mood > 0:
                pumped = False
                happy = False
                enlightened = False
                sad = True
                mood_display.set("Mood(+): " + "Sad")
                mood = mood + random.randint(5,10)
                print("Updated Mood(+):"+ str(mood))
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
                mood_increasev = False
            else:
                sad = False
                pumped = False
                enlightened = False
                happy = True
                mood_display.set("Mood(+): " + "Happy")
                mood = mood + 5
                print("Updated Mood(+):"+ str(mood))
                earn_points_single(3)
                main_window.update()
                main_window.after(25000, mood_function, mood)
                main_window.after(20000, app_checker)
                mood_increasev = False
        else:
            mood_display.set("Mood: " + "Dead")
            sad = False
            pumped = False
            happy = False
            enlightened = False
            generation = generation + 1
            generation_file = open("Brain\\Bin\\generationraw.txt", "r+")
            generation_file.write(str(generation))
            generation_file.close()
            int(generation)
            mood = mood - 1 #This is to make sure the mood doesn't go up again
            print("Updated Mood:"+ str(mood))
            mood = 200 #Reset mood
            print("Updated Mood(+):"+ str(mood) +"Mood reset to Happy")
            main_window.after(30000, mood_function, mood)
    else:
        mood_display.set("Mood: " + "Error")
        print("Error, something went seriously wrong.\nPlease restart the program and contact the developer if the problem persists.")


#/------------------------------Start of mood increasers -------------------------------------\

def Mincreaser_G():
    global mood_increasev
    mood_increasev = True
    print("Mood increased")


#/------------------------------End of mood increasers -------------------------------------\


#/------------------------------Start of app checker-------------------------------------\

def clear_app_linker():
    clear_app_linker_file = open("Brain\\AppLinker\\linked_app.txt", "r+")
    clear_app_linker_file.write("")
    clear_app_linker_file.close()
    clear_app_linker_file2 = open("Brain\\AppLinker\\linked_app2.txt", "r+")
    clear_app_linker_file2.write("")
    clear_app_linker_file2.close()


def submit_linked_app():
    print("App link button clicked")
    app_checker_placeholder1()
    app_checker_placeholder2()





app_linker_unlocked = False
window_open = False

def quit_command_applinker():
    playsound("Sounds\\button.mp3", block=False)
    app_linker.destroy()

def app_link_window():
    global window_open
    global app_linker
    window_open = True
    app_linker = customtkinter.CTk()
    app_linker.title("App Linker")
    x = main_window.winfo_x()
    y = main_window.winfo_y()
    app_linker.geometry("420x400+" + str(x) + "+" + str(y))
    app_linker.resizable(False, False)
    app_linker.overrideredirect(True)
    global app_namep
    app_name1 = customtkinter.CTkLabel(app_linker, text="Linked app:")
    app_name1.place(x=0, y=10)
    app_namep = customtkinter.CTkEntry(app_linker)
    app_namep.place(x=10, y=50, width=200, height=30)
    global app_namep2
    app_name2 = customtkinter.CTkLabel(app_linker, text="2nd linked app:")
    app_name2.place(x=8, y=100)
    app_namep2 = customtkinter.CTkEntry(app_linker)
    app_namep2.place(x=10, y=140, width=200, height=30)
    clear_button = customtkinter.CTkButton(app_linker, text="Clear", command=clear_app_linker)
    clear_button.place(relx=0.25, rely=0.7, anchor=tk.CENTER)
    submit_button = customtkinter.CTkButton(app_linker, text="Submit", command=submit_linked_app)
    submit_button.place(relx=0.75, rely=0.7, anchor=tk.CENTER)
    quit_button = customtkinter.CTkButton(app_linker, text="Close", command=quit_command_applinker)
    quit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    app_linker.mainloop()




def app_checker_word():
    if "word.exe" in (i.name() for i in psutil.process_iter()):
        print("word is running")
        Mincreaser_G()
    else:
        print("word is not running")

game_open = False

def app_checker_steam():
    global game_open
    global game
    if "steam.exe" in (i.name() for i in psutil.process_iter()):
        try:
            #get registry key appID for steamgame and check if it is running
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
            appidS = winreg.QueryValueEx(key, 'RunningAppID')[0]
            #turn appID into string
            client = steamfront.Client()
            game = client.getApp(appid = appidS)
            Mincreaser_G()
            print(game.name + " is running")
            game_open = True
        except:
            print("Steam game is not running")
            game_open = False
    else:
        print("Steam is not running")

def app_checker_placeholder1():
    app_name_file = open("Brain\\AppLinker\\linked_app.txt", "r")
    app_name_file_c = app_name_file.read()
    app_name_file.close()
    
    if app_name_file_c == "" and window_open == True:
        try:
            app_name = app_namep.get()
            app_name = app_name.lower().strip()
            if app_name in (i.name() for i in psutil.process_iter()): #Will not add the app if it is not running but will save for future opening's
                app_name_file = open("Brain\\AppLinker\\linked_app.txt", "r+")
                app_name_file.write(app_name)
                app_name_file.close()
                print("App 1 linked successfully")
            else:
                print("App 1 not found within running processes")
        except:
            print("No App_1 linked")
    else:
        app_name = app_name_file_c
        if app_name in (i.name() for i in psutil.process_iter()):
            print(app_name + " is running")
            Mincreaser_G()
        else:
            print("App 1 linked but not running")


def app_checker_placeholder2():
    global window_open
    app_name_file2 = open("Brain\\AppLinker\\linked_app2.txt", "r")
    app_name_file2_c = app_name_file2.read()
    app_name_file2.close()

    if app_name_file2_c == "" and window_open == True:
        try:
            app_name2 = app_namep2.get()
            app_name2 = app_name2.lower().strip()
            if app_name2 in (i.name() for i in psutil.process_iter()): #Will not add the app if it is not running but will save for future opening's
                    app_name_file2 = open("Brain\\AppLinker\\linked_app2.txt", "r+")
                    app_name_file2.write(app_name2)
                    app_name_file2.close()
                    print("App 2 linked successfully")
                    Mincreaser_G()
                    window_open = False
            else:
                print("App_2 not found within running processes")
        except:
            print("No App_2 linked")
    else:
        app_name2 = app_name_file2_c
        if app_name2 in (i.name() for i in psutil.process_iter()):
            print(app_name2 + " is running")
            Mincreaser_G()

        else:
            print("No App_2 linked")


def app_checker():
    app_checker_word()
    app_checker_steam()
    app_checker_placeholder1()
    app_checker_placeholder2()

    
#/------------------------------End of app checker-------------------------------------\

# \------------------------------End of mood function-------------------------------------/

#/------------------------------Start of points function-------------------------------------\


points = open("Brain\\Bin\\pointsraw.txt", "r")
points = points.read()


    
def earn_points_bulk():
    global points
    points = int(points)
    points = points + 300
    points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
    points_file.write(str(points))
    points_file.close()
    print("Updated Points: " + str(points))
        

def earn_points_single(amount):
    global points
    points = int(points)
    points = points + amount
    points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
    points_file.write(str(points))
    points_file.close()
    print("Updated Points: " + str(points))


def earn_points():
    try:
        global points
        points = int(points)
        points = points + 1
        points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
        points_file.write(str(points))
        points_file.close()
        print("Updated Points: " + str(points))
        
    except ZeroDivisionError:
        pass
    
    #1/2 hour timer
    main_window.after(1800000, earn_points) #1800000 ms = 30 minutes

    

#/------------------------------End of points function-------------------------------------\

# \------------------------------Start of points shop window-------------------------------------/

def flag_checker():
    global app_linker_unlocked
    with open("Brain\\AppLinker\\flag.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag1 is 1 - App linker active")
        app_linker_unlocked = True
    else:
        print("Flag is 0")

def flag_checkerB():
    button_sound()
    with open("Brain\\AppLinker\\flag.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        app_link_window()
    else:
        print("Flag is 0")

def flag_checker2():
    global green_compa_unlocked
    with open("Brain\\Flags\\flag2.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag2 is 1 - Green compa active")
        green_compa_unlocked = True
        w2.configure(fg="#009f66")
    else:
        print("Flag2 is 0")


def flag_checker2B():
    global green_compa_unlocked
    feature_window.destroy()
    button_sound()
    with open("Brain\\Flags\\flag2.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag2 is 1 - Green compa active")
        green_compa_unlocked = True
        w2.configure(fg="#009f66")
    else:
        print("Flag2 is 0")

def flag_checker3():
    global purple_compa_unlocked
    with open("Brain\\Flags\\flag3.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag3 is 1 - Purple compa active")
        purple_compa_unlocked = True
        w2.configure(fg="#a200a7")
    else:
        print("Flag3 is 0")

def flag_checker3B():
    global purple_compa_unlocked
    feature_window.destroy()
    button_sound()
    with open("Brain\\Flags\\flag3.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag3 is 1 - Purple compa active")
        purple_compa_unlocked = True
        w2.configure(fg="#a200a7")
    else:
        print("Flag3 is 0")

def flag_checker4():
    global blue_compa_unlocked
    with open("Brain\\Flags\\flag4.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag4 is 1 - Blue compa active")
        blue_compa_unlocked = True
        w2.configure(fg="#3c8ad1")
    else:
        print("Flag4 is 0")

def flag_checker4B():
    global blue_compa_unlocked
    feature_window.destroy()
    button_sound()
    with open("Brain\\Flags\\flag4.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag4 is 1 - Blue compa active")
        blue_compa_unlocked = True
        w2.configure(fg="#3c8ad1")
    else:
        print("Flag4 is 0")

def flag_checker5():
    global feeder_unlocked
    with open("Brain\\Flags\\flag5.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag5 is 1 - Feeder active")
        feeder_unlocked = True
    else:
        print("Flag5 is 0")

def flag_checker5B():
    reward_sound()
    with open("Brain\\Flags\\flag5.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        earn_points_single(3)
        Mincreaser_G()
        print("Mmmm Num-Num-Num...3 points have been awarded.")
        button1_3_action()
        
    else:
        print("Flag5 is 0")

def flag_checker6():
    global playing_unlocked
    with open("Brain\\Flags\\flag6.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag6 is 1 - Playing button active")
        playing_unlocked = True
    else:
        print("Flag6 is 0")


def flag_checker6B():
    reward_sound()
    with open("Brain\\Flags\\flag6.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        earn_points_single(5)
        Mincreaser_G()
        print("Yay!! I love swimming! *SPLISH* *SPLASH* Woooo!! *SPLISH* *SPLISH* --> 5 points awarded")
        button2_3_action()
    else:
        print("Flag6 is 0")


def flag_checker7():
    global sleeping_unlocked
    with open("Brain\\Flags\\flag7.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag7 is 1 - Nap button active")
        sleeping_unlocked = True
    else:
        print("Flag7 is 0")

def flag_checker7B():
    reward_sound()
    with open("Brain\\Flags\\flag7.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        Mincreaser_G()
        print("ZZZZZZZzzzzzzzz......ZZZZZZZzzzzzzzz......")
        button3_3_action()
    else:
        print("Flag7 is 0")

def flag_checker8():
    global VIP_unlocked
    with open("Brain\\Flags\\flag8.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag8 is 1 - VIP button active")
        VIP_unlocked = True
        w2.configure(fg="#15EEE6")
    else:
        print("Flag8 is 0")

def flag_checker8B():
    global VIP_unlocked
    button_sound()
    with open("Brain\\Flags\\flag8.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        VIP_unlocked = True
        popup = customtkinter.CTk()
        x = main_window.winfo_x()
        y = main_window.winfo_y()
        popup.geometry("420x400+" + str(x) + "+" + str(y))
        popup.resizable(False, False)
        popup.overrideredirect(True)
        def yes():
            print("Flag8 is 1 - VIP button active")
            w2.configure(fg="#15EEE6")
            button_sound()
            popup.destroy()
            feature_window.destroy()
            main_window.destroy()
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen("python3 Compa.pyw", startupinfo=startupinfo)
        
        def no():
            button_sound()
            popup.destroy()


        label = customtkinter.CTkLabel(popup, text="Restart Compa?\nA restart is required when activating VIP.")
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        B1 = customtkinter.CTkButton(popup, text="Yes", command=yes)
        B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        B2 = customtkinter.CTkButton(popup, text="No", command=no)
        B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        popup.update()
        popup.mainloop()

    else:
        print("Flag8 is 0")

def flag_checker9():
    global game_wiki_unlocked
    with open("Brain\\Flags\\flag9.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag9 is 1 - Wiki button active")
        game_wiki_unlocked = True
    else:
        print("Flag9 is 0")

def flag_checker9B():
    global game_wiki_unlocked
    button_sound()
    with open("Brain\\Flags\\flag9.txt", "r") as f:
        flag = f.read()
        f.close()
    if flag == "1":
        print("Flag9 is 1 - Wiki button active")
        game_wiki_unlocked = True
        button3_action()
    else:
        print("Flag9 is 0")

green_compa_unlocked = False
purple_compa_unlocked = False
blue_compa_unlocked = False
feeder_unlocked = False
playing_unlocked = False
sleeping_unlocked = False
VIP_unlocked = False
game_wiki_unlocked = False

def button1_active():
    global app_linker_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 200
        cost_display.set("Cost:"+str(cost))
        if points >= cost: 
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global app_linker_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                app_linker_unlocked = True
                #save flag to file
                with open("Brain\\AppLinker\\flag.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()


            label = customtkinter.CTkLabel(popup, text="Purchase Applinker feature?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))


def button2_active():
    global VIP_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 800
        cost_display.set("Cost:"+str(cost))
        if points >= cost: 
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global VIP_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                VIP_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag8.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()


            def close():
                button_sound()
                popup.destroy()

            
            label = customtkinter.CTkLabel(popup, text="Purchase VIP?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))


def button3_active():
    global game_wiki_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 300
        cost_display.set("Cost:"+str(cost))
        if points >= cost: 
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global game_wiki_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                game_wiki_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag9.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()

            
            label = customtkinter.CTkLabel(popup, text="Purchase GameWiki feature?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))

def button3_action():
    global game
    button_sound()
    if game_wiki_unlocked == True and game_open == True:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        if os.path.exists(chrome_path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("https://www.google.com/search?q="+ game.name + " wiki")
            # Will auto open first webpage result
            time.sleep(2)
            pyautogui.press('tab', presses=19)
            pyautogui.press('enter')
        elif os.path.exists(brave_path):
            webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
            webbrowser.get('brave').open("https://search.brave.com/search?q="+ game.name + " wiki")
        else:
            webbrowser.open("https://www.google.com/search?q="+ game.name + " wiki")
    else:
        print("Game wiki feature not unlocked or no game open.")

def button1_2_active():
    global green_compa_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 75
        cost_display.set("Cost:"+str(cost))
        if points >= cost:
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global green_compa_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                w2.configure(fg="#009f66")
                points_window_display.set("You have unlocked the ability to turn you Compa green.")
                green_compa_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag2.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()

            
            label = customtkinter.CTkLabel(popup, text="Purchase Green Compa?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))

def button2_2_active():
    global purple_compa_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 75
        cost_display.set("Cost:"+str(cost))
        if points >= cost:
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global purple_compa_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                w2.configure(fg="#a200a7")
                points_window_display.set("You have unlocked the ability to turn you Compa purple.")
                purple_compa_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag3.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()
            
            label = customtkinter.CTkLabel(popup, text="Purchase Purple Compa?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))

def button3_2_active():
    global blue_compa_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 75
        cost_display.set("Cost:"+str(cost))
        if points >= cost:
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global blue_compa_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                w2.configure(fg="#3c8ad1")
                points_window_display.set("You have unlocked the ability to turn you Compa blue.")
                blue_compa_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag4.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()

            
            label = customtkinter.CTkLabel(popup, text="Purchase Blue Compa?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))


def button1_3_active():
    global feeder_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 75
        cost_display.set("Cost:"+str(cost))
        if points >= cost:
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global feeder_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                points_window_display.set("You have unlocked the ability to feed your Compa.")
                feeder_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag5.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()
            
            label = customtkinter.CTkLabel(popup, text="Purchase Feed feature?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))


def button1_3_action():
    global feature_window
    global eating
    eating = True
    feature_window.destroy()
    body_display.set(body_displayEating)
    main_window.after(1300, button1_3_action_after)

def button1_3_action_after():
    body_display.set(body_displayEating2)
    main_window.after(1300, button1_3_action_after2)

def button1_3_action_after2():
    body_display.set(body_displayEating3)
    main_window.after(1300, button1_3_action_after3)

def button1_3_action_after3():
    if eating == True:
        body_display.set(body_displayEating2)
        main_window.after(1200, button1_3_action_after4)
    else:
        print("Eating animation cancelled.")

def button1_3_action_after4():
    body_display.set(body_displayEating3)


def button2_3_active():
    global playing_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 75
        cost_display.set("Cost:"+str(cost))
        if points >= cost:
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global playing_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                points_window_display.set("You have unlocked the ability to play with your Compa.")
                playing_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag6.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()

            
            label = customtkinter.CTkLabel(popup, text="Purchase Play feature?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))


def button2_3_action():
    global feature_window
    global playing
    playing = True
    feature_window.destroy()
    body_display.set(body_displayPlaying)
    main_window.after(1300, button2_3_action_after)

def button2_3_action_after():
    global playing
    playing = True
    body_display.set(body_displayPlaying2)
    main_window.after(1300, button2_3_action_after2)

def button2_3_action_after2():
    global playing
    playing = True
    body_display.set(body_displayPlaying3)
    main_window.after(1300, button2_3_action_after3)

def button2_3_action_after3():
    global playing
    playing = True
    body_display.set(body_displayPlaying4)
    main_window.after(1300, button2_3_action_after4)

def button2_3_action_after4():
    global playing
    playing = True
    body_display.set(body_displayPlaying5)


def button3_3_active():
    global sleeping_unlocked
    button_sound()
    with open("Brain\\Bin\\pointsraw.txt", "r") as points_file:
        points = points_file.read()
        points_file.close()
        points = int(points)
        cost = 75
        cost_display.set("Cost:"+str(cost))
        if points >= cost:
            popup = customtkinter.CTk()
            popup.title("Would you like to purchase this feature?")
            x = main_window.winfo_x()
            y = main_window.winfo_y()
            popup.geometry("420x400+" + str(x) + "+" + str(y))
            popup.resizable(False, False)
            popup.overrideredirect(True)
            def bought():
                button_sound()
                global sleeping_unlocked
                global points
                points = points - cost
                points_file = open("Brain\\Bin\\pointsraw.txt", "r+")
                points_file.write(str(points))
                points_file.close()
                points_window_display.set("You have unlocked the ability to sleep.")
                sleeping_unlocked = True
                #save flag to file
                with open("Brain\\Flags\\flag7.txt", "r+") as flag_file:
                    flag_file.write("1")
                    flag_file.close()
                popup.destroy()

            def close():
                button_sound()
                popup.destroy()

            
            label = customtkinter.CTkLabel(popup, text="Purchase Sleep feature?")
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            cost_display_popup = customtkinter.CTkLabel(popup, text="Cost: "+str(cost))
            cost_display_popup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            B1 = customtkinter.CTkButton(popup, text="Yes", command=bought)
            B1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            B2 = customtkinter.CTkButton(popup, text="No", command=close)
            B2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
            popup.update()
            popup.mainloop()
        else:
            print("Not enough points")
            cost_display.set("Not enough points! -- Cost:"+str(cost))



def button3_3_action():
    global feature_window
    global sleeping
    sleeping = True
    feature_window.destroy()
    body_display.set(body_displaySleeping)
    main_window.after(1300, button3_3_action_after)

def button3_3_action_after():
    global sleeping
    sleeping = True
    body_display.set(body_displaySleeping2)
    main_window.after(1300, button3_3_action_after2)


def button3_3_action_after2():
    global sleeping
    body_display.set(body_displaySleeping3)
    main_window.after(1300, button3_3_action_after3)

def button3_3_action_after3():
    body_display.set(body_displaySleeping)
    main_window.after(1300, button3_3_action_after4)

def button3_3_action_after4():
    body_display.set(body_displaySleeping2)
    main_window.after(1300, button3_3_action_after5)

def button3_3_action_after5():
    body_display.set(body_displaySleeping3)

def points_shop():
    global points_window
    button_sound()
    global points_window_display
    global cost_display
    points_window = customtkinter.CTk()
    points_window.title("Points Shop")
    x = main_window.winfo_x()
    y = main_window.winfo_y()
    points_window.geometry("420x400+" + str(x) + "+" + str(y))
    points_window.resizable(False, False)
    points_window.overrideredirect(True)

    points_window_display = customtkinter.StringVar(points_window)
    points_window_display.set("Welcome to the points shop.\nHere you can purchase new features for your Compa!")
    points_window_display_label = customtkinter.CTkLabel(points_window, textvariable=points_window_display)
    points_window_display_label.configure(font=("Courier", 10))
    points_window_display_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    points_string = customtkinter.StringVar(points_window)
    points_label = customtkinter.CTkLabel(points_window, textvariable=points_string)
    points_label.configure(font=("Courier", 10))
    points_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    cost_display = customtkinter.StringVar(points_window)
    cost_display.set("Cost: N/A")
    cost_display_label = customtkinter.CTkLabel(points_window, textvariable=cost_display)
    cost_display_label.configure(font=("Courier", 10))
    cost_display_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


    
    button1 = customtkinter.CTkButton(points_window, text="App linker", command=button1_active)
    button1.place(relx=0.17, rely=0.5, anchor=tk.CENTER)
    button2 = customtkinter.CTkButton(points_window, text="VIP", command=button2_active)
    button2.place(relx=0.17, rely=0.6, anchor=tk.CENTER)
    button3 = customtkinter.CTkButton(points_window, text="Game Wiki", command=button3_active)
    button3.place(relx=0.17, rely=0.7, anchor=tk.CENTER)
    button1_2 = customtkinter.CTkButton(points_window, text="Green Compa", command=button1_2_active)
    button1_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button2_2 = customtkinter.CTkButton(points_window, text="Purple Compa", command=button2_2_active)
    button2_2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    button3_2 = customtkinter.CTkButton(points_window, text="Blue Compa", command=button3_2_active)
    button3_2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    button1_3 = customtkinter.CTkButton(points_window, text="Feeder", command=button1_3_active)
    button1_3.place(relx=0.83, rely=0.5, anchor=tk.CENTER)
    button2_3 = customtkinter.CTkButton(points_window, text="Play", command=button2_3_active)
    button2_3.place(relx=0.83, rely=0.6, anchor=tk.CENTER)
    button3_3 = customtkinter.CTkButton(points_window, text="Nap time", command=button3_3_active)
    button3_3.place(relx=0.83, rely=0.7, anchor=tk.CENTER)

    def quit_button_pointswindow():
        button_sound()
        points_window.destroy()

    closebutton = customtkinter.CTkButton(points_window, text="Close", command=quit_button_pointswindow)
    closebutton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def update_display():
        points_window_display.set("Welcome to the points shop.\nHere you can purchase new features for your Compa!")
        cost_display.set("Cost: N/A")
        points_window.after(10000, update_display)

    def points_label_refresher():
        with open("Brain\\Bin\\pointsraw.txt", "r") as points_file2:
            points = points_file2.read()
            points_file2.close()
            points = int(points)
            points_string.set("Points: " + str(points))
            points_window.after(1000, points_label_refresher)

    def applinker_button_checker():
        if app_linker_unlocked == True:
            button1.configure(state=tk.DISABLED)
        else:
            button1.configure(state=tk.NORMAL)
        points_window.after(100, applinker_button_checker)
    
    def VIP_button_checker():
        if VIP_unlocked == True:
            button2.configure(state=tk.DISABLED)
        else:
            button2.configure(state=tk.NORMAL)
        points_window.after(100, VIP_button_checker)

    def game_wiki_button_checker():
        if game_wiki_unlocked == True:
            button3.configure(state=tk.DISABLED)
        else:
            button3.configure(state=tk.NORMAL)
        points_window.after(100, game_wiki_button_checker)

    def green_button_checker():
        if green_compa_unlocked == True:
            button1_2.configure(state=tk.DISABLED)
        else:
            button1_2.configure(state=tk.NORMAL)
        points_window.after(100, green_button_checker)

    def purple_button_checker():
        if purple_compa_unlocked == True:
            button2_2.configure(state=tk.DISABLED)
        else:
            button2_2.configure(state=tk.NORMAL)
        points_window.after(100, purple_button_checker)

    def blue_button_checker():
        if blue_compa_unlocked == True:
            button3_2.configure(state=tk.DISABLED)
        else:
            button3_2.configure(state=tk.NORMAL)
        points_window.after(100, blue_button_checker)

    def feeder_button_checker():
        if feeder_unlocked == True:
            button1_3.configure(state=tk.DISABLED)
        else:
            button1_3.configure(state=tk.NORMAL)
        points_window.after(100, feeder_button_checker)
    def play_button_checker():
        if playing_unlocked == True:
            button2_3.configure(state=tk.DISABLED)
        else:
            button2_3.configure(state=tk.NORMAL)
        points_window.after(100, play_button_checker)
    def nap_button_checker():
        if sleeping_unlocked == True:
            button3_3.configure(state=tk.DISABLED)
        else:
            button3_3.configure(state=tk.NORMAL)
        points_window.after(100, nap_button_checker)


    button1.after(10000, update_display)
    button1_2.after(10000, update_display)
    button2_2.after(10000, update_display)
    button3_2.after(10000, update_display)
    points_window.after(100, points_label_refresher)
    points_window.after(100, applinker_button_checker)
    points_window.after(100, VIP_button_checker)
    points_window.after(100, game_wiki_button_checker)
    points_window.after(100, green_button_checker)
    points_window.after(100, purple_button_checker)
    points_window.after(100, blue_button_checker)
    points_window.after(100, feeder_button_checker)
    points_window.after(100, play_button_checker)
    points_window.after(100, nap_button_checker)
    points_window.mainloop()

#/------------------------------End of points shop window-------------------------------------\

#/------------------------------Start of Feature window-------------------------------------\

def button_sound():
    playsound("Sounds\\button.mp3", block=False)

def reward_sound():
    playsound("Sounds\\happy.mp3", block=False)

def feature_window():
    global feature_window
    button_sound()
    feature_window = customtkinter.CTk()
    feature_window.title("Features")
    x = main_window.winfo_x()
    y = main_window.winfo_y()
    feature_window.geometry("420x400+" + str(x) + "+" + str(y))
    feature_window.resizable(False, False)
    feature_window.overrideredirect(True)

    feature_window_display = customtkinter.StringVar(feature_window)
    feature_window_display.set("Welcome to the features window.\n\nPlease select the feature you would like to use.")
    feature_window_display_label = customtkinter.CTkLabel(feature_window, textvariable=feature_window_display)
    feature_window_display_label.configure(font=("Courier", 10))
    feature_window_display_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    Applinkbutton = customtkinter.CTkButton(feature_window, text="App linker", command=flag_checkerB)
    Applinkbutton.place(relx=0.17, rely=0.5, anchor=tk.CENTER)
    button2 = customtkinter.CTkButton(feature_window, text="VIP", command=flag_checker8B)
    button2.place(relx=0.17, rely=0.6, anchor=tk.CENTER)
    button3 = customtkinter.CTkButton(feature_window, text="Game Wiki", command=flag_checker9B)
    button3.place(relx=0.17, rely=0.7, anchor=tk.CENTER)
    button1_2 = customtkinter.CTkButton(feature_window, text="Green Compa", command=flag_checker2B)
    button1_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button2_2 = customtkinter.CTkButton(feature_window, text="Purple Compa", command=flag_checker3B)
    button2_2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    button3_2 = customtkinter.CTkButton(feature_window, text="Blue Compa", command=flag_checker4B)
    button3_2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    button1_3 = customtkinter.CTkButton(feature_window, text="Feed", command=flag_checker5B)
    button1_3.place(relx=0.83, rely=0.5, anchor=tk.CENTER)
    button2_3 = customtkinter.CTkButton(feature_window, text="Play", command=flag_checker6B)
    button2_3.place(relx=0.83, rely=0.6, anchor=tk.CENTER)
    button3_3 = customtkinter.CTkButton(feature_window, text="Nap", command=flag_checker7B)
    button3_3.place(relx=0.83, rely=0.7, anchor=tk.CENTER)


    def quit_command_featurewindow():
        playsound("Sounds\\button.mp3", block=False)
        feature_window.destroy()

    closebutton = customtkinter.CTkButton(feature_window, text="Close", command=quit_command_featurewindow)
    closebutton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


    def button_checker():
        if app_linker_unlocked == True:
            Applinkbutton.configure(state=tk.NORMAL)
            feature_window.after(1000, button_checker)
        else:
            Applinkbutton.configure(state=tk.DISABLED)

    def vip_button_checker():
        if VIP_unlocked == True:
            button2.configure(state=tk.NORMAL)
            feature_window.after(1000, vip_button_checker)
        else:
            button2.configure(state=tk.DISABLED)

    def game_wiki_button_checker():
        if game_wiki_unlocked == True:
            button3.configure(state=tk.NORMAL)
            feature_window.after(1000, game_wiki_button_checker)
        else:
            button3.configure(state=tk.DISABLED)

    def green_button_checker():
        if green_compa_unlocked == True:
            button1_2.configure(state=tk.NORMAL)
            feature_window.after(1000, green_button_checker)
        else:
            button1_2.configure(state=tk.DISABLED)
    def purple_button_checker():
        if purple_compa_unlocked == True:
            button2_2.configure(state=tk.NORMAL)
            feature_window.after(1000, purple_button_checker)
        else:
            button2_2.configure(state=tk.DISABLED)
    def blue_button_checker():
        if blue_compa_unlocked == True:
            button3_2.configure(state=tk.NORMAL)
            feature_window.after(1000, blue_button_checker)
        else:
            button3_2.configure(state=tk.DISABLED)

    def feeder_button_checker():
        if feeder_unlocked == True and eating == False:
            button1_3.configure(state=tk.NORMAL)
            feature_window.after(1000, feeder_button_checker)
        elif feeder_unlocked == True and eating == True:
            button1_3.configure(state=tk.DISABLED)
            feature_window.after(30000, feeder_button_checker) #30000ms = 30s
        else:
            button1_3.configure(state=tk.DISABLED)

    def play_button_checker():
        if playing_unlocked == True and playing == False:
            button2_3.configure(state=tk.NORMAL)
            feature_window.after(1000, play_button_checker)
        elif playing_unlocked == True and playing == True:
            button2_3.configure(state=tk.DISABLED)
            feature_window.after(30000, play_button_checker) #30000ms = 30s
        else:
            button2_3.configure(state=tk.DISABLED)

    def nap_button_checker():
        if sleeping_unlocked == True and sleeping == False:
            button3_3.configure(state=tk.NORMAL)
            feature_window.after(1000, nap_button_checker)
        elif sleeping_unlocked == True and sleeping == True:
            button3_3.configure(state=tk.DISABLED)
            feature_window.after(30000, nap_button_checker) #30000ms = 30s
        else:
            button3_3.configure(state=tk.DISABLED)


    feature_window.after(100, button_checker)
    feature_window.after(100, vip_button_checker)
    feature_window.after(100, game_wiki_button_checker)
    feature_window.after(100, green_button_checker)
    feature_window.after(100, purple_button_checker)
    feature_window.after(100, blue_button_checker)
    feature_window.after(100, feeder_button_checker)
    feature_window.after(100, play_button_checker)
    feature_window.after(100, nap_button_checker)
    feature_window.mainloop()
 


#/------------------------------End of Feature window-------------------------------------\
eating = False
playing = False
sleeping = False
#/------------------------------Start of body function-------------------------------------\

def body_function():
    global eating
    global playing
    global sleeping
    if enlightened == True and eating == False and playing == False and sleeping == False:
        body_display.set(random.choice(body_displaySP))
        main_window.update()
        main_window.after(12500, body_function)
    elif pumped == True and eating == False and playing == False and sleeping == False:
        body_display.set(random.choice(body_displayP))
        main_window.update()
        main_window.after(12500, body_function)
    elif sad == True and eating == False and playing == False and sleeping == False:
        body_display.set(random.choice(body_displayS))
        main_window.update()
        main_window.after(12500, body_function)
    elif happy == True and eating == False and playing == False and sleeping == False:
        body_display.set(random.choice(body_displayH))
        main_window.update()
        main_window.after(12500, body_function)
    elif eating == True or playing == True or sleeping == True:
        eating = False
        playing = False
        sleeping = False
        main_window.update()
        main_window.after(5000, body_function)
    elif enlightened == False and pumped == False and sad == False and happy == False:
        body_display.set(body_displayD)
        main_window.update()
        main_window.after(12500, body_function)
    else:
        body_display.set(body_displayE)
        main_window.update()
        main_window.after(12500, body_function)


# \------------------------------End of body function-------------------------------------/

def startup_noise():
    playsound("Sounds\\startup.wav", block=False)


def quit_command():
    playsound("Sounds\\close.wav", block=False)
    time.sleep(1)
    sys.stdout.close()
    sys.stderr.close()
    main_window.destroy()

#Tkinter Frame
w1=customtkinter.CTkLabel(main_window, text="")
w1.pack()
w2=customtkinter.CTkLabel(main_window, textvariable=body_display)
w2.configure(font=("Courier", 30))
w2.pack()
w25=customtkinter.CTkLabel(main_window, text="")
w25.pack()
w3=customtkinter.CTkLabel(main_window, textvariable=mood_display)
w3.configure(font=("Courier", 10))
w3.pack()
w4 = customtkinter.CTkLabel(main_window, textvariable=age_display)
w4.configure(font=("Courier", 10))
w4.pack()
w5=customtkinter.CTkLabel(main_window, textvariable=generation_display)
w5.configure(font=("Courier", 10))
w5.pack()
w6=customtkinter.CTkLabel(main_window, text="")
w6.pack()
MoodButton=customtkinter.CTkButton(main_window, command=feature_window, text="Features", text_color_disabled="red")
MoodButton.place(relx=0.3, rely=0.75, anchor=tk.CENTER)
ShopButton = customtkinter.CTkButton(main_window, command=points_shop, text="Points Shop")
ShopButton.place(relx=0.7, rely=0.75, anchor=tk.CENTER)
quitbutton=customtkinter.CTkButton(main_window, command=quit_command, text="Quit")
quitbutton.place(relx= 0.5, rely=0.9, anchor=tk.CENTER)


mood_display.set("Mood: " + "Calculating...")
age_display.set("Age: " + "Calculating...")
generation_display.set("Generation:" + "Calculating...")
w3.after(5001, startup_noise)
w3.after(5000, mood_function, mood)
w4.after(1500000, age_increaser) #1500000 ms = 25 minutes
main_window.after(1800000, earn_points) #1800000 ms = 30 minutes
main_window.after(5000, body_function)

app_checker()
flag_checker()
flag_checker2()
flag_checker3()
flag_checker4()
flag_checker5()
flag_checker6()
flag_checker7()
flag_checker8()
flag_checker9()
#Tkinter window loop
main_window.mainloop()

# \------------------------------End of Main Window-------------------------------------/
