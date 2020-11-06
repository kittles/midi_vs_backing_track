import subprocess as sp
import argparse
from midi2audio import FluidSynth
import os

root_dir = os.path.dirname(os.path.realpath(__file__))
tmp_dir = os.path.join(root_dir, 'tmp')
sound_font = os.path.join(root_dir, 'SalC5Light2.sf2')
fs = FluidSynth(sound_font=sound_font)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--midi-file', '-m', help='the midi file to synthesize', type=str)
    parser.add_argument('--backing-track', '-b', help='the backing track (.aac format) to compare the midi synth to', type=str, default=1)
    parser.add_argument('--output', '-o', help='where the comparison track is output to', type=str)
    args = parser.parse_args()


    #input_fp = '../songs/jingle_bells_harmonized/song.mid'
    #backing_fp_aac = '../songs/jingle_bells_harmonized/C.aac'

    #input_fp = '../songs/old_macdonald_harmonized/song.mid'
    #backing_fp_aac = '../songs/old_macdonald_harmonized/C.aac'

    input_fp = args.midi_file
    backing_fp_aac = args.backing_track

    # make a wav of the backing track
    backing_fp = os.path.join(tmp_dir, 'backing.wav')
    sp.call('ffmpeg -nostats -hide_banner -loglevel panic -y -i {} {}'.format(backing_fp_aac, backing_fp), shell=True)

    output_fp = os.path.join(tmp_dir, 'midi-audio.wav')
    output_louder_fp = os.path.join(tmp_dir, 'midi-audio-louder.wav')
    if args.output:
        both_fp = args.output
    else:
        both_fp = os.paht.join(root_dir, 'midi-audio-with-backing.wav')


    # render the midi as a wav
    fs.midi_to_audio(input_fp, output_fp)
    sp.call('ffmpeg -i {} -y -filter:a "volume=2" {}'.format(output_fp, output_louder_fp), shell=True)

    # join the two wavs together
    cmd = 'ffmpeg -i {} -i {} -y -filter_complex amix=inputs=2:duration=longest {}'.format(
        output_louder_fp,
        backing_fp,
        both_fp
    )
    sp.call(cmd, shell=True)

    print('output track location:', both_fp)

    sp.call('play {}'.format(both_fp), shell=True)
