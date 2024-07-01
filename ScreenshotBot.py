# Name: Rusho Binnabi
# Date: 6/24/2024
# Project: Screenshot Bot
# Contact Information: RushoBinnabi12@yahoo.com

# this ScreenshotBot file uses the pyautogui and the tkinter libraries to take screenshots.

import pyautogui
import tkinter


# this saveScreenshot() function has the functionality for taking screenshots.
def saveScreenshot():
    pyautogui.screenshot(inputFileName.get() + ".jpg") # adds the .jpg extension to the end of the file so that users don't have to.
    confirmationLabel = tkinter.Label(main, text="Screenshot Saved!", pady=8)
    confirmationLabel.pack()
    confirmationLabel.config(justify='center')


# this is the code to set up the GUI for taking screenshots.

main = tkinter.Tk()
main.title("Screenshot Bot")
main.geometry("500x150")

label = tkinter.Label(main, text="Enter filename:", pady=8)
label.pack()
label.config(justify='center')

inputFileName = tkinter.Entry(main, width=25)
inputFileName.pack(pady=10)

confirmationButton = tkinter.Button(main, text="Save Screenshot", width=14, command=lambda: saveScreenshot())
confirmationButton.pack()
confirmationButton.config(justify='center')

main.mainloop()
