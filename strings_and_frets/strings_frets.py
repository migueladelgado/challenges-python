#Strings and Frets
#Challenge URL: https://edabit.com/challenge/9c5nHopKXkZH6zXij
#Notes 
#C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B
import guitar as g
guitar = g.create_guitar()

def string_fret(string, fret):
    note = guitar[fret][string - 1]
    if not note:
        return print('Invalid Input')
    if string < 1:
        return print('No Such String!!!')
    if fret > 24:
        return print('Not a valid fret!!!')
    return print(note)


#testing 
string_fret(2, 10) # "A"
string_fret(0, 16) # "No Such String!!!"
string_fret(2, 19) # F#/GB
string_fret(3, 0) # G



