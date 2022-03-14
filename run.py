from generate_target_sents import get_inaugural_sentences
import attack
import os
import datasets
from datasets import CTRLF_DatasetWrapper
from moviepy.audio.AudioClip import AudioArrayClip

def main():
    # Load the inaugural sentences as targets
    #paras = get_inaugural_sentences()

    x = CTRLF_DatasetWrapper()

    num_files = 1

    for i in range(num_files):
        ted_results, mswc_result, label_dict = x.get(i)
        sample_waveform = ted_results.get("waveform")
        print(sample_waveform.shape)
        sample_waveform = sample_waveform.reshape(sample_waveform.shape[1],1)
        print(sample_waveform.shape)
        sample_rate = ted_results.get("sample_rate")
        filename = "temp.wav"
        wav_file = AudioArrayClip(sample_waveform, fps = sample_rate)
        wav_file.write_audiofile(filename)
        out_filename = "test_adversarial.wav"
        #para = paras[i]
        attack.main(inp = [filename], target = "this is a test", out = out_filename, iterations = 100)


main()
