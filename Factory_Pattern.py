import tkinter as tk
from tkinter import Frame, filedialog, ttk
from tkinter.constants import BOTH, RAISED
import pandas as pd
import csv
import datetime
from datetime import datetime
from random import randint
import pathlib
import os
from dicttoxml import *



#### convert date function
def dateconversion(text):
    datetimeobject = datetime.strptime(text,'%Y/%d/%m')
    new_format = datetimeobject.strftime('%d.%m.%Y')
    return new_format

#### convert time function
def timeconversion(text):
    in_time = datetime.strptime(text,'%I:%M:%S %p')
    new_format = datetime.strftime(in_time, "%H:%M:%S")
    return new_format

#### convert speed function
def speedconversion(text):
    text = float(text) * 1.94384
    text = str(text) + "NM/H"
    return text

#### convert distance function
def distanceconversion(text):
    text = float(text) * 0.539957
    text = str(text) + "NM"
    return text


#### convert distance function
def data_conversion(df):
    converted = {}
    converted['DATE'] = df['DATE'].map(dateconversion)
    converted['TIME'] = df['TIME'].map(timeconversion)
    converted['SPEED'] = df['SPEED'].map(speedconversion)
    converted['DISTANCE'] = df['DISTANCE'].map(distanceconversion)
    converted['DESCR'] = df['DESCR']


    return converted


#### convert to xml function
def convert_row(row):
    return """
    <points>
        <point> 
            <date>%s</date>
            <time>%s</time> 
            <speed>%s</speed> 
            <distance>%s</distance> 
            <description>%s</description> 
        </point> 
    </points>""" % (row[0], row[1], row[2], row[3], row[4])




# upload button handler
def upload_clicked():
    apps.clear()
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir='/', title="Select file",
    filetypes=(("Text","*.txt"), ("Csv","*.csv")))
    apps.append(filename)
    for app in apps:
        
        label = tk.Label(frame, text="File: " + app)
        label.pack()


# execute button handler
def execute_file():
    for app in apps:
        file_extension = pathlib.Path(app).suffix
        if (file_extension==".txt"):
            print("////////////////////////////")
            df = pd.read_csv(app,delimiter="\t")
        elif(file_extension==".csv"):
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
            df = pd.read_csv(app,delimiter=",")

        
        dc = data_conversion(df)
        
        ##df.to_csv(fileout, index=False)
        ran = str(randint(0, 1000000000))
        if combo.get() == "CSV":
            fileout = "output_csv" + ran +".csv"
            dc.to_csv(fileout, encoding='utf-8', index=False)
    
        elif combo.get() == "XML":
            #fileout1 = "output" + ran + ".xml"
            #print(dc)
            #xml = dicttoxml(dc, custom_root='points', item_func=lambda x: 'point', attr_type=False)
            #dom = parseString(xml)
            #with open(fileout1, "wb") as outfile:
            #    outfile.write(dom.toprettyxml(encoding="UTF-8"))




        ###### convert to xml  
            with open('output'+ ran +'.xml', 'w') as out:
                out.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
                print(dc)
              #  for line in dc:
                  #  print(dc[line])
                    #out.write('\n'.join([convert_row(line) for line in dc]))
        
            
        ###### print success msg
        for widget in frame.winfo_children():
            widget.destroy()
        label = tk.Label(frame, text="The file was converted succefully!")
        label.pack()
            


root = tk.Tk()
apps = []

root.geometry('400x300')
root.resizable(False,False)
root.title('Design patterns project')



###### importing icons for buttons
upload_icon = tk.PhotoImage(file='./upload.png')
cursor_icon = tk.PhotoImage(file='./cursor.png')


###### creating the upload button
upload_button = tk.Button(
    root,
    image=upload_icon,
    text='Upload file',
    compound=tk.LEFT,
    command=upload_clicked
)
upload_button.pack(
    ipadx=5,
    ipady=2,
    expand=True
)


combo = ttk.Combobox(root, values=['CSV', 'XML'])
combo.pack()


###### creating the execute button
execute_button = tk.Button(
    root,
    image=cursor_icon,
    text='Execute program',
    compound=tk.LEFT,
    command=execute_file
)

execute_button.pack(
    ipadx=5,
    ipady=4,
    expand=True
)


###### creating the frame
frame = Frame(root, relief=RAISED, borderwidth=0.5)
frame.pack(fill=BOTH, expand=False)

root.mainloop()
