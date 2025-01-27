# -*- coding: future_fstrings -*-
from generate_target_sents import get_inaugural_words
import attack
import os
import datasets
from datasets import CTRLF_DatasetWrapper
from moviepy.audio.AudioClip import AudioArrayClip
import tensorflow as tf

def main():
    # Load the inaugural words as targets
    inaugural_words = get_inaugural_words()
    # counter to keep track of the index within inaugural words
    inaugural_counter = 100

    # Specify name of the out file
    label_filename = "labels.csv"
    # Specify the headers of the out file
    headers = "Keyword, TEDLIUM_SampleID, TED_TALK_ID, TEDLIUM_SET, MSWC_AudioID, start_time, end_time, confidence"

    # Open out file and populate with headers
    label_file = open(label_filename, "a")
    label_file.write(headers)

    x = CTRLF_DatasetWrapper()

    num_files = 1000

    for i in range(100,num_files):
        print("Audio Sample ID: " , i)
        try:
            # Get information for a single tedlium audio file
            ted_results = x.get(i)

            # Extract the necessary information from the pandas dataframe
            sample_waveform = ted_results["TED_waveform"][0]
            sample_waveform = sample_waveform.reshape(sample_waveform.shape[1],1)
            sample_transcript = ted_results["TED_transcript"]
            sample_keyword = ted_results["keyword"]
            sample_subset = ted_results["TED_talk_id"]
            sample_id = "adversarial_" + str(i)
            sample_rate = ted_results["TED_sample_rate"][0]
            start_time = ted_results["keyword_start_time"]
            end_time = ted_results["keyword_end_time"]
            confidence = ted_results["confidence"]
            out_filename = f"Data/adversarial/{sample_id}.wav" 
            keyword_id = ted_results["MSWC_ID"]

            # Define a file to temporarly store the original audio in
            filename = "temp.wav"
            wav_file = AudioArrayClip(sample_waveform, fps = sample_rate)
            wav_file.write_audiofile(filename)

            # Get n words from the inaugural dataset, where n corresponds to the length of the transcript
            target = ""
            while True:
                target = " ".join(inaugural_words[inaugural_counter:inaugural_counter+len(sample_transcript)])
                if not(target == "-"):
                    break
            print(type(target), target)
            inaugural_counter = inaugural_counter+len(sample_transcript)

            attack.main(inp = [filename], target = target, out = out_filename, iterations = 1000)

            # Delete the temp file
            os.remove(filename)

            # Save the information to the csv file
            label_row = f"{sample_keyword},{sample_id},{sample_subset},{sample_id},{keyword_id},{start_time},{end_time},{confidence}"
            label_file.write(label_row)
        except Exception as exc:
            print("Exception at Audio Sample ID: ", i)
            print("Exception message: ", exc) 
            continue


main()
