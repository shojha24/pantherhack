from TTS.api import TTS

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)
# Run TTS
# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# Text to speech to a file
"""tts.tts_to_file(text="This is Brad Pitt", speaker=tts.speakers[0], language=tts.languages[0], file_path="pitt.wav")
tts.tts_to_file(text="This is Denzel Washington", speaker=tts.speakers[0], language=tts.languages[0], file_path="washington.wav")
tts.tts_to_file(text="This is Johnny Depp", speaker=tts.speakers[0], language=tts.languages[0], file_path="depp.wav")
tts.tts_to_file(text="This is Tom Cruise", speaker=tts.speakers[0], language=tts.languages[0], file_path="cruise.wav")
tts.tts_to_file(text="This is Jennifer Lawrence", speaker=tts.speakers[0], language=tts.languages[0], file_path="lawrence.wav")"""
tts.tts_to_file(text="Face not recognized. Intruder.", speaker=tts.speakers[0], language=tts.languages[0], file_path="intruder.wav")






