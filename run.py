from generate_target_sents import get_inaugural_sentences
import attack
import os

def main():
    # Load the inaugural sentences as targets
    paras = get_inaugural_sentences()

    # Get the wav files
    filenames = ["/audio_adversarial_examples/data/" + filename for filename in os.listdir("/audio_adversarial_examples/data/")]
    for i in range(len(filenames)):
        filename = filenames[i]
        para = paras[i]
        out = ["adversarial_" + filename]
        attack.main(inp = [filename], target = para, out = out, iterations = 1000)


main()
