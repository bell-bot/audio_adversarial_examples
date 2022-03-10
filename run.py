from generate_target_sents import get_inaugural_sentences
import attack
import os
import datasets
from datasets import CTRLF_DatasetWrapper

def main():
    # Load the inaugural sentences as targets
    #paras = get_inaugural_sentences()

    x = CTRLF_DatasetWrapper(path_to_labels_csv = "/audio_adversarial_examples/Data", path_to_TED="/audio_adversarial_examples/Data")

    num_files = 100

    for i in range(num_files):
        sample = x.get(i)
        out_filename = f"{i}_adversarial.wav"
        sample_waveform = sample[]
        #para = paras[i]
        #out = [filename[:-4]+"_adversarial.wav"]
        #attack.main(inp = [filename], target = "this is a test please work or else", out = out, iterations = 1000)


main()
