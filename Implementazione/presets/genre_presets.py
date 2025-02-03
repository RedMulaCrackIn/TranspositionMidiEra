from music21 import stream, note, chord, meter, metadata

def apply_classical(original):
    classical = original.transpose(0)
    classical.metadata.title = "Classical Version"
    
    # Aggiungi dinamiche
    for n in classical.recurse().notes:
        if n.offset % 2 == 0:
            n.addLyric("p")
        else:
            n.addLyric("f")
    
    return classical