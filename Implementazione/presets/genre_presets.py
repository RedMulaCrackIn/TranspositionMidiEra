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

def apply_jazz(original):
    jazz = stream.Stream()
    jazz.metadata = metadata.Metadata(title="Jazz Version")
    
    # Swing rhythm
    for n in original.recurse().notes:
        new_n = note.Note(n.pitch)
        new_n.duration.quarterLength = 0.75 if n.offset % 1 == 0 else 0.25
        jazz.append(new_n)
    
    return jazz

def apply_blues(original):
    blues = original.transpose(-2)
    blues.metadata.title = "Blues Version"
    
    # Blue notes
    for n in blues.recurse().notes:
        if n.pitch.midi == 64:  # Mi naturale
            n.pitch.transpose(-1, inPlace=True)
    
    return blues

GENRE_FUNCTIONS = {
    'classical': apply_classical,
    'jazz': apply_jazz,
    'blues': apply_blues
}
