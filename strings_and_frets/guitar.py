def create_guitar():
    #Create tuple of notes and unpack into variables
    notes = ('C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B')
    c, cdb, d, deb, e, f, fgb, g, gab, a, abb, b = notes
    #Create dictionary of frets with a list of the notes on each string
    guitar = {
        0  : [e, a, d, g, b, e],
        1  : [f, abb, deb, gab, c, f],
        2  : [fgb, b, e, a, cdb, fgb],
        3  : [g, c, f, abb, d, g],
        4  : [gab, cdb, fgb, b, deb, gab],
        5  : [a, d, g, c, e, a],
        6  : [abb, deb, gab, cdb, f, abb],
        7  : [b, e, a, d, fgb, b],
        8  : [c, f, abb, deb, g, c],
        9  : [cdb, fgb, b, e, gab, cdb],
        10 : [d, g, c, f, a, d],
        11 : [deb, gab, cdb, fgb, abb, deb], 
        12 : [e, a, d, g, b, e],
        13 : [f, abb, deb, gab, c, f],
        14 : [fgb, b, e, a, cdb, fgb],
        15 : [g, c, f, abb, d, g],
        16 : [gab, cdb, fgb, b, deb, gab],
        17 : [a, d, g, c, e, a],
        18 : [abb, deb, gab, cdb, f, abb],
        19 : [b, e, a, d, fgb, b],
        20 : [c, f, abb, deb, g, c],
        21 : [cdb, fgb, b, e, gab, cdb],
        22 : [d, g, c, f, a, d],
        23 : [deb, gab, cdb, fgb, abb, deb],
        24 : [e, a, d, g, b, e]
    }

    #Realized that I input the notes backwards, so lazily reversing the order
    for fret in guitar: 
        guitar[fret] = list(reversed(guitar[fret]))
        
    return guitar