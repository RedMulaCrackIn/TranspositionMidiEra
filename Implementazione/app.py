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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_midi():
    try:
        genre = request.form.get('genre', '').lower()
        if genre not in GENRE_FUNCTIONS:
            return render_template('error.html', error="Seleziona un genere valido")

        # Genera e processa
        base_stream = generate_base_melody()
        processed_stream = GENRE_FUNCTIONS[genre](base_stream)
        
        # Salva i file
        original_filename = f"original_{random.randint(1000,9999)}.mid"
        processed_filename = f"processed_{random.randint(1000,9999)}.mid"
        
        save_midi(base_stream, original_filename)
        save_midi(processed_stream, processed_filename)

        return render_template('player.html',
                             original=original_filename,
                             processed=processed_filename,
                             genre=genre.capitalize())

    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/generated/<filename>')
def serve_midi(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, port=5001)