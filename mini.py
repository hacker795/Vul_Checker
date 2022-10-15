from tkinter import *
import shlex
from tkinter import filedialog
import time
import subprocess
import os
from PIL import Image, ImageTk

def startnmap():
	os.system("python3 cnmap.py")
	
def domain():
    file = open("process/ipsaved.txt", "w")
    value = subprocess.Popen("dig -f "+wordlist.get()+" +short", stdout=subprocess.PIPE, shell=True)
    (out, err) = value.communicate()
    n1=(str(out).replace("\\n", "\n")).replace("'","")
    finalOut=n1.replace("b", "")
    file.write(finalOut)
    file.close()
    
    ar1=[]
    ar2=[]
    f1 = open("process/ipsaved.txt", "r")
    while True:
        line = f1.readline()
        if not line:
            break
        else:
            ar1.append(line.strip())
    f1.close()
    f2 = open(wordlist.get(), "r")
    limit=0
    while True:
        line = f2.readline()
        if not line:
            break
        else:
            ar2.append(line.strip())
            limit+=1
    f2.close()
    fout = open("webip.txt", "w")
    count=1
    while True:
        if (count == limit):
            break
        else:
            fout.write(ar2[count]+" -> "+ar1[count]+"\n")
            count+=1
    fout.close()
    file = open("webip.txt", "r")
    data=file.read()
    file.close()

    domain=Tk()
    domain.title("Domains list")
    domain.geometry("450x100+580+430")
    e=("The ip addresses for",wordlist.get(),"are: ")
    label=Label(domain, text= e ).grid(row=0,column=0)
    text=Text(domain, wrap=WORD)
    text.insert(INSERT, data)
    text.grid()
    domain.mainloop()

def browse():
    global a
    global wordlist
    filename = filedialog.askopenfilename(initialdir = "/",

                                          title = "Select a File",

                                          filetypes = (("Text files",

                                                        "*.txt*"),

                                                       ("all files",

                                                        "*.*")))
    a=filename
    wordlist.set(a)


def onion():
	os.system('terminator -e "bash onionscan.sh"  ')

def webs():
	os.system('terminator -e "bash web.sh"    ')




def destroy():
	root.destroy()
def ip():
	text_file = open("process/ips.txt", "w")
	text_file.write(url.get())
	text_file.close()
	os.system('''dig -f process/ips.txt > process/ipresult.txt; cat process/ipresult.txt | tail -7 | head -1 | awk '{print $(NF)}' > process/ipdone.txt && rm -rf process/ips.txt process/ipresult.txt''')
	f = open("process/ipdone.txt", "r")
	data = f.read()
	a= (data)
	ipwindow=Tk()
	ipwindow.configure(bg="skyblue")
	e=("The ip address for",url.get(),"is: ")
	label=Label(ipwindow, text= e ).grid(row=0,column=0)
	ipwindow.title("IP result")
	ipwindow.geometry("450x100+580+430")
	ipwindow.resizable(True,0)
	time.sleep(2)
	entry=Entry(ipwindow)
	entry.insert(0, a)
	entry.grid(row=0,column=1)
	f.close()
	os.system("cd process; rm -rf ipresult.txt ipdone.txt")
	ipwindow.mainloop()
	

root=Tk()
root.title("Mr.X")
root.geometry("420x600+600+600")
root.resizable(0,0)
criedit=Label(root,text="           web Scanner          ", 
font=("Times 30 bold italic"), fg="black").grid(row
=1)
web=Label(root,text="Enter Website:").grid(row=2,column=0, sticky="w")
url=StringVar()
webentry=Entry(root,textvariable=url, relief=SUNKEN, borderwidth=5).grid(row=2,column=0)
#wordlist=StringVar()
Label(root, text="Enter filepath: ").grid(row=3,sticky="w", column=0)
wordlist=StringVar()
wordlistentry=Entry(root,textvariable=wordlist, relief=SUNKEN, borderwidth=5)
wordlistentry.grid(row=3,column=0)

browsefilepath=Button(root, text="Browse",command=browse).grid(row=3,column=0,sticky="e")

iplookup=Button(root, text="IPLookup          ", bg="lightblue",activebackground='#00ff00', font="Times 13 bold italic", cursor="hand2", fg="black", command=ip).grid(row=4, column=0, sticky="nsew")
Label1=Label(root,  bg="lightblue").grid(row=5, column=0, sticky="nsew")

domaintoip=Button(root, text="Domain to IP",activebackground='#00ff00',font="Times 13 bold italic",cursor="hand2", bg="lightblue", fg="black", command=domain).grid(row=6, column=0, sticky="nsew")
Label3=Label(root,  bg="lightblue").grid(row=7, column=0, sticky="nsew")

nmap=Button(root, text="NMap", bg="lightblue",activebackground='#00ff00',font="Times 13 bold italic",cursor="hand2", fg="black", command=startnmap).grid(row=8, column=0, sticky="nsew")
Label3=Label(root,  bg="lightblue").grid(row=9, column=0, sticky="nsew")

onionscanner=Button(root, text="Onion Scanner",activebackground='#00ff00',font="Times 13 bold italic",cursor="hand2", bg="lightblue", fg="black", command=onion).grid(row=10, column=0, sticky="nsew")
Label5=Label(root,  bg="lightblue").grid(row=11, column=0, sticky="nsew")

scanvulnerability=Button(root, text="Scan Vulnerability",activebackground='#00ff00',font="Times 13 bold italic",cursor="hand2", bg="lightblue", fg="black", command=webs).grid(row=12, column=0, sticky="nsew")
Label6=Label(root,  bg="lightblue").grid(row=13, column=0, sticky="nsew")

exit=Button(root, text="Exit", bg="lightblue", fg="red",activebackground='#00ff00',font="Times 13 bold italic",cursor="hand2", command=destroy).grid(row=14, column=0, sticky="nsew")

labelimage = Label(root)
labelimage.grid(row=0,column=0,sticky="ewns")
filename = 'process/logo2.png'
img = Image.open(filename)
resized_img = img.resize((300, 160))
root.photoimg = ImageTk.PhotoImage(resized_img)
labelimage.configure(image=root.photoimg)

label1=Label(root, text= " ").grid(row=15,column=0, sticky="w")
label2=Label(root, text= "Vulnerability Scanner", font="Times 13 bold italic").grid(row=15,column=0)

root.mainloop()
