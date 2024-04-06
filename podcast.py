import requests
import xml.etree.ElementTree as ET
from urllib.parse import unquote
import subprocess
import sys
import os
from main import create_summaries

def podcast_way(url, name, gpt):
    print(url)
# RSS feed URL'
    response = requests.get(url)
    print("hello 1")
    response.raise_for_status()
    print("hello 2")
    if (os.path.exists("hello.mp3")):
        os.remove("hello.mp3")
        os.remove("hello.wav")
    print("sup broski")
    root = ET.fromstring(response.content)

    # Initialize variable to keep track of whether the episode was found
    episode_found = False
    print("made here")
    for item in root.findall('./channel/item'):
        title = item.find('title').text
        print("made here")
        if name.lower() in title.lower():  # Case insensitive search
            audio_url = item.find('enclosure').get('url')
            audio_url = unquote(audio_url)  # Ensure the URL is correctly formatted
            
            # Optional: Print the episode title and URL for confirmation
            print(f"Found episode: {title}")
            print(f"Audio URL: {audio_url}")

            # Download the audio file
            audio_response = requests.get(audio_url)
            audio_response.raise_for_status()

            # Create a filename from the episode title (simplified)
            filename = 'hello.mp3'  # Replace invalid characters for filenames

            # Save the audio file
            with open(filename, 'wb') as audio_file:
                audio_file.write(audio_response.content)
            
            print(f"Episode audio saved as: {filename}")
            
            episode_found = True
            break  # Stop searching once the episode is found and downloaded

    if not episode_found:
        print("Episode not found. Please check the title and try again.")
    else:
        title = filename.replace(".mp4", "")

        # convert mp4 file to wav (16-bit)
        new_filename = "hello.wav"
        print("ran: "+ title)
        subprocess.run([
            'ffmpeg',
            '-i', "hello.mp3",
            '-ar', '16000',
            '-ac', '1',
            '-c:a', 'pcm_s16le',
            "hello.wav"
        ])

        # call local whisper model
        result = subprocess.check_output([
            './main',
            '-f', '../Podcast-Summarizer/hello.wav'
        ], cwd="../whisper.cpp")
        transcript = result.decode(sys.stdout.encoding).strip()
        print(transcript)
        summary = create_summaries(transcript, gpt)
        return summary


