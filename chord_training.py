####Aaron's Big Chord Training Set####
###Made by Aaron Keller###
import numpy as np

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

####Stack chords into 2D array####
set = [C_M,C_M7,C_m,C_m7,C_o,C_o7,C_07,C_a,CSM,CSM7,CSm,CSm7,CSo,CSo7,CS07,CSa,D_M,D_M7,D_m,D_m7,D_o,D_o7,D_07,D_a,DSM,DSM7,DSm,DSm7,DSo,DSo7,DS07,DSa,E_M,E_M7,E_m,E_m7,E_o,E_o7,E_07,E_a,F_M,F_M7,F_m,F_m7,F_o,F_o7,F_07,F_a,FSM,FSM7,FSm,FSm7,FSo,FSo7,FS07,FSa,G_M,G_M7,G_m,G_m7,G_o,G_o7,G_07,G_a,GSM,GSM7,GSm,GSm7,GSo,GSo7,GS07,GSa,A_M,A_M7,A_m,A_m7,A_o,A_o7,A_07,A_a,ASM,ASM7,ASm,ASm7,ASo,ASo7,AS07,ASa,B_M,B_M7,B_m,B_m7,B_o,B_o7,B_07,B_a]
training_chord_set = np.zeros(shape=(96,12))
training_chord_labels = np.zeros(training_chord_set.shape[0])
for i in range(training_chord_set.shape[0]):
    training_chord_set[i,:] = set[i]
    training_chord_labels[i] = i

##Make dictionary of chord labels
chord_dictionary = {
    '0': 'C_M_',
    '1': 'C_M7',
    '2': 'C_m_',
    '3': 'C_m7',
    '4': 'C_o_',
    '5': 'C_o7',
    '6': 'C_07',
    '7': 'C_a_',
    '8': 'CSM_',
    '9': 'CSM7',
    '10': 'CSm_',
    '11': 'CSm7',
    '12': 'CSo_',
    '13': 'CSo7',
    '14': 'CS07',
    '15': 'CSa_',
    '16': 'D_M_',
    '17': 'D_M7',
    '18': 'D_m_',
    '19': 'D_m7',
    '20': 'D_o_',
    '21': 'D_o7',
    '22': 'D_07',
    '23': 'D_a_',
    '24': 'DSM_',
    '25': 'DSM7',
    '26': 'DSm_',
    '27': 'DSm7',
    '28': 'DSo_',
    '29': 'DSo7',
    '30': 'DS07',
    '31': 'DSa_',
    '32': 'E_M_',
    '33': 'E_M7',
    '34': 'E_m_',
    '35': 'E_m7',
    '36': 'E_o_',
    '37': 'E_o7',
    '38': 'E_07',
    '39': 'E_a_',
    '40': 'F_M_',
    '41': 'F_M7',
    '42': 'F_m_',
    '43': 'F_m7',
    '44': 'F_o_',
    '45': 'F_o7',
    '46': 'F_07',
    '47': 'F_a_',
    '48': 'FSM_',
    '49': 'FSM7',
    '50': 'FSm_',
    '51': 'FSm7',
    '52': 'FSo_',
    '53': 'FSo7',
    '54': 'FS07',
    '55': 'FSa_',
    '56': 'G_M_',
    '57': 'G_M7',
    '58': 'G_m_',
    '59': 'G_m7',
    '60': 'G_o_',
    '61': 'G_o7',
    '62': 'G_07',
    '63': 'G_a_',
    '64': 'GSM_',
    '65': 'GSM7',
    '66': 'GSm_',
    '67': 'GSm7',
    '68': 'GSo_',
    '69': 'GSo7',
    '70': 'GS07',
    '71': 'GSa_',
    '72': 'A_M_',
    '73': 'A_M7',
    '74': 'A_m_',
    '75': 'A_m7',
    '76': 'A_o_',
    '77': 'A_o7',
    '78': 'A_07',
    '79': 'A_a_',
    '80': 'ASM_',
    '81': 'ASM7',
    '82': 'ASm_',
    '83': 'ASm7',
    '84': 'ASo_',
    '85': 'ASo7',
    '86': 'AS07',
    '87': 'ASa_',
    '88': 'B_M_',
    '89': 'B_M7',
    '90': 'B_m_',
    '91': 'B_m7',
    '92': 'B_o_',
    '93': 'B_o7',
    '94': 'B_07',
    '95': 'B_a_'}

chord_vectors = {
    'C_M_': C_M,
    'C_M7': C_M7,
    'C_m_': C_m,
    'C_m7': C_m7,
    'C_o_': C_o,
    'C_o7': C_o7,
    'C_07': C_07,
    'C_a_': C_a,
    'CSM_': CSM,
    'CSM7': CSM7,
    'CSm_': CSm,
    'CSm7': CSm7,
    'CSo_': CSo,
    'CSo7': CSo7,
    'CS07': CS07,
    'CSa_': CSa,
    'D_M_': D_M,
    'D_M7': D_M7,
    'D_m_': D_m,
    'D_m7': D_m7,
    'D_o_': D_o,
    'D_o7': D_o7,
    'D_07': D_07,
    'D_a_': D_a,
    'DSM_': DSM,
    'DSM7': DSM7,
    'DSm_': DSm,
    'DSm7': DSm7,
    'DSo_': DSo,
    'DSo7': DSo7,
    'DS07': DS07,
    'DSa_': DSa,
    'E_M_': E_M,
    'E_M7': E_M7,
    'E_m_': E_m,
    'E_m7': E_m7,
    'E_o_': E_o,
    'E_o7': E_o7,
    'E_07': E_07,
    'E_a_': E_a,
    'F_M_': F_M,
    'F_M7': F_M7,
    'F_m_': F_m,
    'F_m7': F_m7,
    'F_o_': F_o,
    'F_o7': F_07,
    'F_07': F_07,
    'F_a_': F_a,
    'FSM_': FSM,
    'FSM7': FSM7,
    'FSm_': FSm,
    'FSm7': FSm7,
    'FSo_': FSo,
    'FSo7': FSo7,
    'FS07': FS07,
    'FSa_': FSa,
    'G_M_': G_M,
    'G_M7': G_M7,
    'G_m_': G_m,
    'G_m7': G_m7,
    'G_o_': G_o,
    'G_o7': G_o7,
    'G_07': G_07,
    'G_a_': G_a,
    'GSM_': GSM,
    'GSM7': GSM7,
    'GSm_': GSm,
    'GSm7': GSm7,
    'GSo_': GSo,
    'GSo7': GSo7,
    'GS07': GS07,
    'GSa_': GSa,
    'A_M_': A_M,
    'A_M7': A_M7,
    'A_m_': A_m,
    'A_m7': A_m7,
    'A_o_': A_o,
    'A_o7': A_o7,
    'A_07': A_07,
    'A_a_': A_a,
    'ASM_': ASM,
    'ASM7': ASM7,
    'ASm_': ASm,
    'ASm7': ASm7,
    'ASo_': ASo,
    'ASo7': ASo7,
    'AS07': AS07,
    'ASa_': ASa,
    'B_M_': B_M,
    'B_M7': B_M7,
    'B_m_': B_m,
    'B_m7': B_m7,
    'B_o_': B_o,
    'B_o7': B_o7,
    'B_07': B_07,
    'B_a_': B_a}

#Krumhansl-Schmuckler Key Vectors
#Major Keys
C = np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88])
CS = np.roll(C,1)
D = np.roll(C,2)
DS = np.roll(C,3)
E = np.roll(C,4)
F = np.roll(C,5)
FS = np.roll(C,6)
G = np.roll(C,7)
GS = np.roll(C,8)
A = np.roll(C,9)
AS = np.roll(C,10)
B = np.roll(C,11)

#Minor Keys
c = np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
cS = np.roll(c,1)
d = np.roll(c,2)
dS = np.roll(c,3)
e = np.roll(c,4)
f = np.roll(c,5)
fS = np.roll(c,6)
g = np.roll(c,7)
gS = np.roll(c,8)
a = np.roll(c,9)
aS = np.roll(c,10)
b = np.roll(c,11)

key_set = [C,CS,D,DS,E,F,FS,G,GS,A,AS,B,c,cS,d,dS,e,f,fS,g,gS,a,aS,b]
ks_key_set = np.zeros(shape=(24,12))
ks_key_labels = np.zeros(ks_key_set.shape[0])
for i in range(ks_key_set.shape[0]):
    ks_key_set[i,:] = key_set[i]
    ks_key_labels[i] = i

key_dictionary = {
    '0': 'C Major',
    '1': 'C#/Db Major',
    '2': 'D Major',
    '3': 'D#/Eb Major',
    '4': 'E Major',
    '5': 'F Major',
    '6': 'F#/Gb Major',
    '7': 'G Major',
    '8': 'G#/Ab Major',
    '9': 'A Major',
    '10': 'A#/Bb Major',
    '11': 'B Major',
    '12': 'c minor',
    '13': 'c#/db minor',
    '14': 'd minor',
    '15': 'd#/eb minor',
    '16': 'e minor',
    '17': 'f minor',
    '18': 'f#/gb minor',
    '19': 'g minor',
    '20': 'g#/ab minor',
    '21': 'a minor',
    '22': 'a#/bb minor',
    '23': 'b minor'}

key_index_dictionary = {
    'C Major': 0,
    'c minor': 0,
    'C#/Db Major': 1,
    'c#/db minor': 1,
    'D Major': 2,
    'd minor': 2,
    'D# Major': 3,
    'd#/eb minor': 3,
    'E Major': 4,
    'e minor': 4,
    'F Major': 5,
    'f minor': 5,
    'F#/Gb Major': 6,
    'f#/gb minor': 6,
    'G Major': 7,
    'g minor': 7,
    'G#/Ab Major': 8,
    'g#/ab minor': 8,
    'A Major': 9,
    'a minor': 9,
    'A#/Bb Major': 10,
    'a#/bb minor': 10,
    'B Major': 11,
    'b minor': 11}

root_index_dictionary = {
    'C_': 0,
    'CS': 1,
    'D_': 2,
    'DS': 3,
    'E_': 4,
    'F_': 5,
    'FS': 6,
    'G_': 7,
    'GS': 8,
    'A_': 9,
    'AS': 10,
    'B_': 11}

major_roman_dictionary = {
    '00M_': 'I', #Do
    '00m_': 'i',
    '00M7': 'V7/IV',
    '00m7': 'v7/IV',
    '00o_': 'io',
    '00o7': 'io7',
    '0007': 'i07',
    '00a_': 'I+',
    '01M_': 'bII', #Ra
    '01m_': 'bii',
    '01M7': 'bII7',
    '01m7': 'bii7',
    '01o_': 'biio',
    '01o7': 'biio7',
    '0107': 'bii07',
    '01a_': 'bII+',
    '02M_': 'V/V', #Re
    '02m_': 'ii',
    '02M7': 'V7/V',
    '02m7': 'ii7',
    '02o_': 'iio',
    '02o7': 'iio7',
    '0207': 'ii07',
    '02a_': 'II+',
    '03M_': 'bIII', #Me
    '03m_': 'biii',
    '03M7': 'bIII7',
    '03m7': 'biii7',
    '03o_': 'biiio',
    '03o7': 'Cto7',
    '0307': 'biii07',
    '03a_': 'bIII+',
    '04M_': 'V/vi', #Mi
    '04m_': 'iii',
    '04M7': 'V7/vi',
    '04m7': 'v7/vi',
    '04o_': 'iiio',
    '04o7': 'iiio7',
    '0407': 'iii07',
    '04a_': 'III+',
    '05M_': 'IV', #Fa
    '05m_': 'iv',
    '05M7': 'IV7',
    '05m7': 'iv7',
    '05o_': 'ivo',
    '05o7': 'ivo7',
    '0507': 'iv07',
    '05a_': 'IV+',
    '06M_': '#IV', #Fi
    '06m_': '#iv',
    '06M7': '#IV7',
    '06m7': '#iv7',
    '06o_': 'ivo',
    '06o7': 'cto7',
    '0607': '#iv07',
    '06a_': '#IV+',
    '07M_': 'V', #Sol
    '07m_': 'v',
    '07M7': 'V7',
    '07m7': 'v7',
    '07o_': 'vo',
    '07o7': 'vo7',
    '0707': 'v07',
    '07a_': 'V+',
    '08M_': 'bVI', #Le
    '08m_': 'bvi',
    '08M7': 'bVI7',
    '08m7': 'bvi7',
    '08o_': 'bvio',
    '08o7': 'bvio7',
    '0807': 'bvi07',
    '08a_': 'bVI+',
    '09M_': 'VI', #La
    '09m_': 'vi',
    '09M7': 'V7/ii',
    '09m7': 'v7/ii',
    '09o_': 'vio',
    '09o7': 'vio7',
    '0907': 'vi07',
    '09a_': 'VI+',
    '10M_': 'bVII', #Te
    '10m_': 'bvii',
    '10M7': 'bVII7',
    '10m7': 'bvii7',
    '10o_': 'bviio',
    '10o7': 'bviio7',
    '1007': 'bvii07',
    '10a_': 'bVII+',
    '11M_': 'VII', #Ti
    '11m_': 'vii',
    '11M7': 'VII7',
    '11m7': 'vii7',
    '11o_': 'viio',
    '11o7': 'viio7',
    '1107': 'vii07',
    '11a_': 'VII+'}

minor_roman_dictionary = {
    '00M_': 'I', #Do
    '00m_': 'i',
    '00M7': 'V7/IV',
    '00m7': 'v7/IV',
    '00o_': 'io',
    '00o7': 'io7',
    '0007': 'i07',
    '00a_': 'I+',
    '01M_': 'bII', #Ra
    '01m_': 'bii',
    '01M7': 'bII7',
    '01m7': 'bii7',
    '01o_': 'biio',
    '01o7': 'biio7',
    '0107': 'bii07',
    '01a_': 'bII+',
    '02M_': 'V/V', #Re
    '02m_': 'ii',
    '02M7': 'V7/V',
    '02m7': 'ii7',
    '02o_': 'iio',
    '02o7': 'iio7',
    '0207': 'ii07',
    '02a_': 'II+',
    '03M_': 'V/VI', #Me
    '03m_': 'iii',
    '03M7': 'V7/VI',
    '03m7': 'iii7',
    '03o_': 'iiio',
    '03o7': 'iiio7',
    '0307': 'iii07',
    '03a_': 'III+',
    '04M_': '♮iii', #Mi
    '04m_': '♮iii',
    '04M7': '♮III7',
    '04m7': '♮iii7',
    '04o_': '♮iiio',
    '04o7': '♮iiio7',
    '0407': '♮iii07',
    '04a_': '♮III+',
    '05M_': 'IV', #Fa
    '05m_': 'iv',
    '05M7': 'IV7',
    '05m7': 'iv7',
    '05o_': 'ivo',
    '05o7': 'ivo7',
    '0507': 'iv07',
    '05a_': 'IV+',
    '06M_': '#IV', #Fi
    '06m_': '#iv',
    '06M7': '#IV7',
    '06m7': '#iv7',
    '06o_': 'ivo',
    '06o7': 'cto7',
    '0607': '#iv07',
    '06a_': '#IV+',
    '07M_': 'V', #Sol
    '07m_': 'v',
    '07M7': 'V7',
    '07m7': 'v7',
    '07o_': 'vo',
    '07o7': 'vo7',
    '0707': 'v07',
    '07a_': 'V+',
    '08M_': 'VI', #Le
    '08m_': 'vi',
    '08M7': 'VI7',
    '08m7': 'vi7',
    '08o_': 'vio',
    '08o7': 'vio7',
    '0807': 'vi07',
    '08a_': 'VI+',
    '09M_': '♮VI', #La
    '09m_': '♮vi',
    '09M7': '♮VI',
    '09m7': '♮vi',
    '09o_': '♮vio',
    '09o7': '♮vio7',
    '0907': '♮vi07',
    '09a_': '♮VI+',
    '10M_': 'bVII', #Te
    '10m_': 'bvii',
    '10M7': 'bVII7',
    '10m7': 'bvii7',
    '10o_': 'bviio',
    '10o7': 'bviio7',
    '1007': 'bvii07',
    '10a_': 'bVII+',
    '11M_': 'VII', #Ti
    '11m_': 'vii',
    '11M7': 'VII7',
    '11m7': 'vii7',
    '11o_': 'viio',
    '11o7': 'viio7',
    '1107': 'vii07',
    '11a_': 'VII+'}
