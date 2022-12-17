import matplotlib.pyplot as plt
import numpy as np

threshold = 3

filenameIn = 'phonetest'
filenameOut = 'testAnalysis'

pathIn = 'C:/Users/wp200/OneDrive/Documents/VSCode/' + filenameIn + '.txt'
pathOut = 'C:/Users/wp200/OneDrive/Documents/VSCode/' + filenameOut + '.txt'

peaks = [['Frequency (Hz)','Amplitude (dB)']]
xcoords = []
ycoords = []
xpeaks = []
ypeaks = []
with open(pathIn, 'r') as f:
    next(f)
    last = f.readline() #sets initial value for last
    last1 = f.readline() 
    current = f.readline() #sets initial value for current
    nxt1 = f.readline()

    while True:

        nxt = f.readline() #sets value of next to the next line
        
        if not nxt: #if the line contains nothing, stop
            break

        a = last.split() #splits the value of last into its frequency and decible values individually
        b = last1.split()
        c = current.split() #splits the value of current into its frequency and decible values individually
        d = nxt1.split()
        e = nxt.split() #splits the value of nxt into its frequency and decible values individually

        xcoords.append(float(c[0]))
        ycoords.append(float(c[1]))

        if ((float(c[1]) - float(a[1]) > threshold) and ((float(c[1]) - float(e[1])) > threshold) and (float(c[1]) > float(b[1])) and (float(c[1]) > float(d[1]))):
            peaks.append(current.strip().split())
            

        last = last1
        last1 = current #advances last1 to the value of current
        current = nxt1 #advances current to the value of nxt1
        nxt1 = nxt

with open(pathOut, 'w') as out:
    out.write("AUDIO ANALYSIS OUTPUT DATA\n-------------------------------\n\nPEAK VALUES:\n\n")
    for i in range(len(peaks)):
        out.write((str(peaks[i][0])).ljust(20) + str(peaks[i][1]) + "\n")

    out.write("\n\nDEVIATION FROM THEORETICAL\n(Based on first peak value)\n\nFrequency Recorded (Hz)    Frequency Predicted (Hz)    Deviation (%) \n")
    for i in range(len(peaks)-1):
        actual = float(peaks[i+1][0])
        expected = float(peaks[1][0])*(i+1)

        out.write(str(actual).ljust(27) + (str(expected)).ljust(28) + ((str(((actual - expected) / expected)*100)) + "%") + "\n")

for i in range(len(peaks)-1):
    xpeaks.append(float(peaks[i+1][0]))
    ypeaks.append(float(peaks[i+1][1]))

xmin = 0
xmax = 1500

plt.ylim(-120,0)
plt.xlim(xmin,xmax)
plt.xticks(np.arange(xmin, xmax, float(peaks[1][0])))
plt.xticks(rotation = 60) 
plt.plot(xcoords,ycoords)
plt.plot(xpeaks, ypeaks, 'o')
plt.show()