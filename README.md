# setup
`git clone `
`cd midi_vs_backing_track`
`virtualenv -p python3 .env`
`source .env/bin/activate`
`pip install -r requirements.txt`

alternatively you can install the requirements on your global python3, its just one requirement anyway

# usage

for a description of the input arguments, do `python check_midi_vs_audio.py --help`

here is a sample command:
`python check_midi_vs_audio.py --midi-file "../song_barker/songs/old_macdonald_harmonized/song.mid" --backing-track "../song_barker/songs/old_macdonald_harmonized/C.aac" --output hello.wav`
