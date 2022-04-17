# Purpose of this code is to get the raw transcription lines output by MS Team's "Transcribe Meeting" feature
# Remove empty lines
# Remove timestamps
# Remove name tags
import os

path = "./Transcripts"
transcripts = [f for f in os.listdir(path)]

for fileName in transcripts:
    transcript = open(f"./Transcripts/{fileName}", "r")
    # Create result file
    result = open(f"./Result/{fileName}", "w")
    result.close()
    result = open(f"./Result/{fileName}", "a")
    # Skip over "WEBVTT"
    transcript.readline()
    i = 1
    for line in transcript:
        # Take in every 3rd line, which means skip over the empty lines and timestamps
        if i % 3 == 0:
            s = line
            # Remove name tags
            firstTag = s.find(">") + 1
            secondTag = s.rfind("<")
            s = s[firstTag:secondTag]
            result.write(s + "\n")
        i += 1
    transcript.close()
    result.close()