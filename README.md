## Overview

Podcast summarization tool, built with GPT and [Whisper.cpp](https://github.com/ggerganov/whisper.cpp)

## Setup

1. Install packages in requirements.txt with `pip install -r requirements.txt`
2. Create a `.env` file with your OpenAI key following `sample.env`
3. Download and set up local Whisper model
    * Clone the repository: `git clone https://github.com/ggerganov/whisper.cpp.git`
    * `cd` into the repository
    * Download a Whisper model: `bash ./models/download-ggml-model.sh base.en`
    * Build the main example: `make`
4. Add desired YouTube videos to `inputs.txt`, one per line
5. Run Jupyter Notebook, results will be in `summaries` directory!