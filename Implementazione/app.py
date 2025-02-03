from flask import Flask, render_template, request, send_from_directory
from music21 import stream, note, chord, metadata, meter, instrument
import os
import random
from presets.genre_presets import GENRE_FUNCTIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'generated'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def generate_base_melody():
    s = stream.Stream()
    s.metadata = metadata.Metadata(title="AI Composition")
    s.append(meter.TimeSignature('4/4'))
    s.append(instrument.Piano())

    # Genera semplice melodia
    pitches = [60, 62, 64, 65, 67, 69, 71]  # Scala di Do maggiore
    for _ in range(8):
        n = note.Note(random.choice(pitches))
        n.duration.quarterLength = random.choice([0.5, 1.0])
        s.append(n)
    
    return s

def save_midi(stream_obj, filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    stream_obj.write('midi', fp=path)
    return path