from generate_target_sents import get_inaugural_sentences
import attack
import os
import datasets
from datasets import CTRLF_DatasetWrapper
from moviepy.audio import AudioClip

def main():
    # Load the inaugural sentences as targets
    #paras = get_inaugural_sentences()

    x = CTRLF_DatasetWrapper()

    num_files = 1

    for i in range(num_files):
        ted_results, mswc_result, label_dict = x.get(i)
        sample_waveform = ted_results.get("waveform")
        sample_rate = ted_results.get("sample_rate")
        filename = "sample-000000.wav"
        wav_file = AudioClip(sample_waveform, fps = sample_rate)
        wav_file.write_audiofile(filename)
        out_filename = str(i)+"_adversarial.wav"
        #para = paras[i]
        attack.main(inp = [wav_file], target = "this is a test please work or else", out = out_filename, iterations = 100)


main()
