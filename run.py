from generate_target_sents import get_inaugural_sentences
import attack
import os
import datasets
from datasets import CTRLF_DatasetWrapper
import wave

def main():
    # Load the inaugural sentences as targets
    #paras = get_inaugural_sentences()

    x = CTRLF_DatasetWrapper()

    num_files = 1

    for i in range(num_files):
        ted_results, mswc_result, label_dict = x.get(i)
        sample_waveform = ted_results.get("waveform")
        filename = "temp_file"
        wav_file = wave.open(filename, "wb")
        wav_file.writeframes(sample_waveform)
        out_filename = str(i)+"_adversarial.wav"
        #para = paras[i]
        attack.main(inp = [wav_file], target = "this is a test please work or else", out = out_filename, iterations = 100)


main()
