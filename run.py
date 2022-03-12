from generate_target_sents import get_inaugural_sentences
import attack
import os
import datasets
from datasets import CTRLF_DatasetWrapper

def main():
    # Load the inaugural sentences as targets
    #paras = get_inaugural_sentences()

    x = CTRLF_DatasetWrapper()

    num_files = 1

    for i in range(num_files):
        sample = x.get(i)
        out_filename = str(i)+"_adversarial.wav"
        #para = paras[i]
        attack.main(inp = [sample], target = "this is a test please work or else", out = out_filename, iterations = 100)


main()
