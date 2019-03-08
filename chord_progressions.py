####Mike's Big Chord Progression Producer####
###Made by Michael Cuevas###
##Borrowed chord format from Aaron Keller##

import numpy as np
import os
import glob
import itertools

#Chord Name Format:
#Name[0] = Key (ie. C, D, etc.)
#Name[1] = Accidental (b = flat, S = sharp (Could not use # because Python))
#Name[2] = Quality (M = Major, m = Minor, o = Diminished, 0 = Half-Diminished, a = Augmented (Could not use + because Python))
#Name[3] = Triad/Seventh (7 = Seventh)

#Chord Array Format:
#####[C,C#,D,D#,E,F,F#,G,G#,A,A#,B]
#####[C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B]

#Chord:
#C
C_M = np.array([1,0,0,0,1,0,0,1,0,0,0,0]) #C Major
C_M7= np.array([1,0,0,0,1,0,0,1,0,0,0,1]) #C Major 7
C_m = np.array([1,0,0,1,0,0,0,1,0,0,0,0]) #C minor
C_m7= np.array([1,0,0,1,0,0,0,1,0,0,1,0]) #C minor 7
C_o = np.array([1,0,0,1,0,0,1,0,0,0,0,0]) #C Diminished
C_o7= np.array([1,0,0,1,0,0,1,0,0,1,0,0]) #C Fully-Diminished 7
C_07= np.array([1,0,0,1,0,0,1,0,0,0,1,0]) #C Half-Diminished 7
C_a = np.array([1,0,0,0,1,0,0,0,1,0,0,0]) #C Augmented

#C#/Db
CSM = np.roll(C_M, 1) #C Sharp Major / D Flat Major
CSM7= np.roll(C_M7,1) #C Sharp Major 7 / D Flat Major 7
CSm = np.roll(C_m, 1) #C Sharp Minor / D Flat minor
CSm7= np.roll(C_m7,1) #C Sharp Minor 7 / D Flat Minor 7
CSo = np.roll(C_o, 1) #C Sharp Diminished / D Flat Diminished
CSo7= np.roll(C_o7,1) #C Sharp Fully-Diminished 7 / D Flat Fully-Diminished 7
CS07= np.roll(C_07,1) #C Sharp Half-Diminished 7 / D Flat Half-Diminished 7
CSa = np.roll(C_a, 1) #C Sharp Augmented / D Flat Augmented

#D
D_M = np.roll(C_M, 2) #D Major
D_M7= np.roll(C_M7,2) #D Major 7
D_m = np.roll(C_m, 2) #D Minor
D_m7= np.roll(C_m7,2) #D Minor 7
D_o = np.roll(C_o, 2) #D Diminished
D_o7= np.roll(C_o7,2) #D Fully-Diminished 7
D_07= np.roll(C_07,2) #D Half-Diminished 7
D_a = np.roll(C_a, 2) #D Augmented

#D#/Eb
DSM = np.roll(C_M, 3) #D Sharp Major / E Flat Major
DSM7= np.roll(C_M7,3) #D Sharp Major 7 / E Flat Major
DSm = np.roll(C_m, 3) #D Sharp Minor / E Flat minor
DSm7= np.roll(C_m7,3) #D Sharp Minor 7 / E Flat Minor 7
DSo = np.roll(C_o, 3) #D Sharp Diminished / E Flat Diminished
DSo7= np.roll(C_o7,3) #D Sharp Fully-Diminished 7 / E Flat Fully-Diminished 7
DS07= np.roll(C_07,3) #D Sharp Half-Diminished 7 / E Flat Half-Diminished 7
DSa = np.roll(C_a, 3) #D Sharp Augmented / E Flat Augmented

#E
E_M = np.roll(C_M, 4) #E Major
E_M7= np.roll(C_M7,4) #E Major 7
E_m = np.roll(C_m, 4) #E Minor
E_m7= np.roll(C_m7,4) #E Minor 7
E_o = np.roll(C_o, 4) #E Diminished
E_o7= np.roll(C_o7,4) #E Fully-Diminished 7
E_07= np.roll(C_07,4) #E Half-Diminished 7
E_a = np.roll(C_a, 4) #E Augmented

#E#/F
F_M = np.roll(C_M, 5) #E Sharp Major / F Major
F_M7= np.roll(C_M7,5) #E Sharp Major 7 / F Major 7
F_m = np.roll(C_m, 5) #E Sharp Minor / F minor
F_m7= np.roll(C_m7,5) #E Sharp Minor 7 / F Minor 7
F_o = np.roll(C_o, 5) #E Sharp Diminished / F Diminished
F_o7= np.roll(C_o7,5) #E Sharp Fully-Diminished 7 / F Fully-Diminished 7
F_07= np.roll(C_07,5) #E Sharp Half-Diminished 7 / F Half-Diminished 7
F_a = np.roll(C_a, 5) #E Sharp Augmented / F Augmented

#F#/Gb
FSM = np.roll(C_M, 6) #F Sharp Major / G Flat Major
FSM7= np.roll(C_M7,6) #F Sharp Major 7 / G Flat Major
FSm = np.roll(C_m, 6) #F Sharp Minor / G Flat minor
FSm7= np.roll(C_m7,6) #F Sharp Minor 7 / G Flat Minor 7
FSo = np.roll(C_o, 6) #F Sharp Diminished / G Flat Diminished
FSo7= np.roll(C_o7,6) #F Sharp Fully-Diminished 7 / G Flat Fully-Diminished 7
FS07= np.roll(C_07,6) #F Sharp Half-Diminished 7 / G Flat Half-Diminished 7
FSa = np.roll(C_a, 6) #F Sharp Augmented / G Flat Augmented

#G
G_M = np.roll(C_M, 7) #G Major
G_M7= np.roll(C_M7,7) #G Major 7
G_m = np.roll(C_m, 7) #G Minor
G_m7= np.roll(C_m7,7) #G Minor 7
G_o = np.roll(C_o, 7) #G Diminished
G_o7= np.roll(C_o7,7) #G Fully-Diminished 7
G_07= np.roll(C_07,7) #G Half-Diminished 7
G_a = np.roll(C_a, 7) #G Augmented

#G#/Ab
GSM = np.roll(C_M, 8) #G Sharp Major / A Flat Major
GSM7= np.roll(C_M7,8) #G Sharp Major 7 / A Flat Major
GSm = np.roll(C_m, 8) #G Sharp Minor / A Flat minor
GSm7= np.roll(C_m7,8) #G Sharp Minor 7 / A Flat Minor 7
GSo = np.roll(C_o, 8) #G Sharp Diminished / A Flat Diminished
GSo7= np.roll(C_o7,8) #G Sharp Fully-Diminished 7 / A Flat Fully-Diminished 7
GS07= np.roll(C_07,8) #G Sharp Half-Diminished 7 / A Flat Half-Diminished 7
GSa = np.roll(C_a, 8) #G Sharp Augmented / A Flat Augmented

#A
A_M = np.roll(C_M, 9) #A Major
A_M7= np.roll(C_M7,9) #A Major 7
A_m = np.roll(C_m, 9) #A Minor
A_m7= np.roll(C_m7,9) #A Minor 7
A_o = np.roll(C_o, 9) #A Diminished
A_o7= np.roll(C_o7,9) #A Fully-Diminished 7
A_07= np.roll(C_07,9) #A Half-Diminished 7
A_a = np.roll(C_a, 9) #A Augmented

#A#/Bb
ASM = np.roll(C_M, 10) #A Sharp Major / B Flat Major
ASM7= np.roll(C_M7,10) #A Sharp Major 7 / B Flat Major
ASm = np.roll(C_m, 10) #A Sharp Minor / B Flat minor
ASm7= np.roll(C_m7,10) #A Sharp Minor 7 / B Flat Minor 7
ASo = np.roll(C_o, 10) #A Sharp Diminished / B Flat Diminished
ASo7= np.roll(C_o7,10) #A Sharp Fully-Diminished 7 / B Flat Fully-Diminished 7
AS07= np.roll(C_07,10) #A Sharp Half-Diminished 7 / B Flat Half-Diminished 7
ASa = np.roll(C_a, 10) #A Sharp Augmented / B Flat Augmented

#B
B_M = np.roll(C_M, 11) #B Major
B_M7= np.roll(C_M7,11) #B Major 7
B_m = np.roll(C_m, 11) #B Minor
B_m7= np.roll(C_m7,11) #B Minor 7
B_o = np.roll(C_o, 11) #B Diminished
B_o7= np.roll(C_o7,11) #B Fully-Diminished 7
B_07= np.roll(C_07,11) #B Half-Diminished 7
B_a = np.roll(C_a, 11) #B Augmented

ChordSet = [C_M,C_M7,C_m,C_m7,C_o,C_o7,C_07,C_a,CSM,CSM7,CSm,CSm7,CSo,CSo7,CS07,CSa,D_M,D_M7,D_m,D_m7,D_o,D_o7,D_07,D_a,DSM,DSM7,DSm,DSm7,DSo,DSo7,DS07,DSa,E_M,E_M7,E_m,E_m7,E_o,E_o7,E_07,E_a,F_M,F_M7,F_m,F_m7,F_o,F_o7,F_07,F_a,FSM,FSM7,FSm,FSm7,FSo,FSo7,FS07,FSa,G_M,G_M7,G_m,G_m7,G_o,G_o7,G_07,G_a,GSM,GSM7,GSm,GSm7,GSo,GSo7,GS07,GSa,A_M,A_M7,A_m,A_m7,A_o,A_o7,A_07,A_a,ASM,ASM7,ASm,ASm7,ASo,ASo7,AS07,ASa,B_M,B_M7,B_m,B_m7,B_o,B_o7,B_07,B_a]

chord_map = np.array(["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"])
chord_map2 = np.array(["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"])

#base_path = "./UMAPianoDB-Poly-3/chords/UMAPiano-DB-"
#base_path = 'C:\\Users\\Michael Cuevas\\Desktop\\automated-roman-numeral-analysis\\UMAPiano-DB-Poly-3\\chords\\UMAPiano-DB-'

ChordSet = [A_m,E_m7,A_m]
i=0
j=0
k=0
g=0
lost_chords = np.array(['S', 'T', 'R'])
lost_chords2 = np.array(['A', 'R', 'T'])
for name in ChordSet:
    base_path = 'C:/Users/Michael Cuevas/Desktop/automated-roman-numeral-analysis/UMAPiano-DB-Poly-3/chords/UMAPiano-DB-'
    base_path4 = 'C:/Users/Michael Cuevas/Desktop/automated-roman-numeral-analysis/UMAPiano-DB-Poly-4/chords/UMAPiano-DB-' 
    end_path = '-NO-*'
    non_zero = np.nonzero(name)
    if(np.size(non_zero) <= 3):
        # finds the notes in each chord and finds permutations of them
        chord_notes3 = chord_map[non_zero]
        #chord_notes3 = np.sort(chord_notes)
        chord_notes4 = chord_map2[non_zero] 
        #chord_notes4 = np.sort(chord_notes2)
        # finds different possible paths for the chords
        paths = list(itertools.permutations(chord_notes3))
        paths2 = list(itertools.permutations(chord_notes4))
        paths2.append(str(chord_notes4))
        paths.append(str(chord_notes3))
        print(paths)
        path = []
        path2 = []
        i=0
        for chord_notes in paths:
            path.append(base_path + str(chord_notes[0]) + '*' + str(chord_notes[1]) + '*' + str(chord_notes[2]) + '*' + end_path)
        for chord_notes2 in paths2:
            path2.append(base_path + str(chord_notes2[0]) + '*' + str(chord_notes2[1]) + '*' + str(chord_notes2[2]) + '*' + end_path)
            #path3 = base_path + chord_notes3[0] + '*' + chord_notes3[1] + '*' + chord_notes3[2] + '*' + end_path
            #path4 = base_path + chord_notes4[0] + '*' + chord_notes4[1] + '*' + chord_notes4[2] + '*' + end_path
    else:
        chord_notes3 = chord_map[non_zero]
        #chord_notes3 = np.sort(chord_notes)
        chord_notes4 = chord_map2[non_zero] 
        #chord_notes4 = np.sort(chord_notes2)

        # finds different possible paths for the chords
        paths = list(itertools.permutations(chord_notes3))
        paths2 = list(itertools.permutations(chord_notes4))
        #paths2.append(str(chord_notes4))
        #paths2.append(str(chord_notes3))
        path = []
        path2 = []
        #print(chord_notes2)
        #print(paths)
        #print(paths2)
        i=0
        for chord_notes in paths:
            path.append(base_path4 + str(chord_notes[0]) + '*' + str(chord_notes[1]) + '*' + str(chord_notes[2]) + '*' + str(chord_notes[3]) + '*' + end_path)
        for chord_notes2 in paths2:
            path2.append(base_path4 + str(chord_notes2[0]) + '*' + str(chord_notes2[1]) + '*' + str(chord_notes2[2]) + '*' + str(chord_notes2[3]) + '*' + end_path)
            i = i+1
        
       
        #path = base_path4 + chord_notes[0] + '*' + chord_notes[1] + '*' + chord_notes[2] + '*' + chord_notes[3] + '*' + end_path
        #path2 = base_path4 + chord_notes2[0] + '*' + chord_notes2[1] + '*' + chord_notes2[2] + '*' + end_path
        #path3 = base_path4 + chord_notes3[0] + '*' + chord_notes3[1] + '*' + chord_notes3[2] + '*' + end_path
        #path4 = base_path4 + chord_notes4[0] + '*' + chord_notes4[1] + '*' + chord_notes4[2] + '*' + end_path
 
    # Fetches a list of all possible files for the given path
    posFile = np.zeros(len(path))
    #print(path)
    exist = np.zeros(len(path))
    posFile2 = np.zeros(len(path2))
    exist2 = np.zeros(len(path2))
    existingPath = []
    existingPath2 = []
    #print(path)
    for i in range(len(path)):
        posFile[i] = len(glob.glob(os.path.expandvars(path[i]))) 
        #print(posFile[i])
        exist[i] = posFile[i] > 0
        if(exist[i]):
            posFile[i] = 1
            existingPath.append(glob.glob(os.path.expandvars(path[i])))
        else:
            posFile[i] = 0
        posFile2[i] = len(glob.glob(os.path.expandvars(path2[i])))
        exist2[i] = posFile2[i] > 0
        if(exist2[i]):
            posFile2[i] = 1
            existingPath2.append(glob.glob(os.path.expandvars(path2[i])))
        else:
            posFile2[i] = 0
   
    #posFile = glob.glob(os.path.expandvars(path))
    #posFile2 = glob.glob(os.path.expandvars(path2))
    #posFile3 = glob.glob(os.path.expandvars(path3))
    #posFile4 = glob.glob(os.path.expandvars(path4))
       

    # Checks if chords exist in the database
    #exist = len(posFile) > 0
    #exist2 = len(posFile2) > 0 

    #if the chords exist, print the middle one in the list (should hopefully be octave 4)
    #if(exist): 
    #    print(posFile[int(len(posFile)/2)])
    #if(exist2):
    #    print(posFile2[int(len(posFile2)/2)])
    #if(exist3):
    #    print(posFile3[int(len(posFile3)/2)])
    #if(exist4):
    #    print(posFile4[int(len(posFile4)/2)])
    #print(exist[exist>0])
    #print(exist2[exist2>0])
    if(not(len(exist[exist>0]) or (len(exist2[exist2>0])))):
        print(chord_notes3)
        #print(str(os.path.exists(os.path.expandvars(path))))
        #print(str(os.path.exists(os.path.expandvars(path2))))
        #print(path)
        #print(path2 + '\n\n')
        k = k+1
        #lost_chords = np.concatenate((lost_chords, chord_notes), axis=0)
        #lost_chords2 = np.concatenate((lost_chords2, chord_notes2), axis=0)
    else:
        g = g+1
        print(existingPath)
        print(existingPath2)
print('failed to find: ' + str(k) + ' chords')
print('able to find: ' + str(g) + ' chords')
#for numtimes in range(int((np.shape(lost_chords)[0])/3)):
    #index = numtimes*3
    #print('Notes: ' + lost_chords[index] + ' ' + lost_chords[index+1] + ' ' + lost_chords[index+2] + ' / ' + lost_chords2[index] + ' ' + lost_chords2[index+1] + ' ' + lost_chords2[index+2])
#Progression = ChordSet
#for name in ChordSet:
    
