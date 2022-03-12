from generate_target_sents import get_inaugural_sentences
import attack
import os
import datasets
from datasets import CTRLF_DatasetWrapper

def main():
    # Load the inaugural sentences as targets
    #paras = get_inaugural_sentences()

    x = CTRLF_DatasetWrapper(path_to_labels_csv = "/audio_adversarial_examples/Data/", path_to_TED="/audio_adversarial_examples/Data/")

    num_files = 1

    for i in range(num_files):
        sample = x.get(i)
        out_filename = str(i)+"_adversarial.wav"
        sample_waveform = sample[]
        para = paras[i]
        attack.main(inp = [sample], target = "this is a test please work or else", out = out_filename, iterations = 100)


main()
