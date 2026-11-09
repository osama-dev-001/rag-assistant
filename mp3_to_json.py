import whisper
import json
import os

model = whisper.load_model('large-v2')

audios = os.listdir("resources/Tutorial_Audio")

for audio in audios:
    audio_number = audio.split("_")[0]
    audio_title = audio.split("_")[1][:-4]
    
    result = model.transcribe(audio= f"resources/Tutorial_Audio/{audio}", language="hi", task="translate", word_timestamps=False, verbose=False)
    
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number": audio_number, "title": audio_title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        
    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
    
    with open(f"resources/Tutorial_Jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata, f)