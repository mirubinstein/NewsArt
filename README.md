# News Art - AI Powered Instagram Account
This Python program does the following (NewsArt.py):
  1. Fetches the top 10 articles from Google News
  2. Chooses an article at random
  3. Creates a summary of that article via ChatGPT 3.5 turbo
  4. Creates an artistic representation of the article based on the summary via Dall-E 3
  5. Creates a caption for the art piece via ChatGPT 3.5 turbo
  6. Posts the image and caption to Instagram

This is executed 3 times per day (6am, 12pm, and 6pm PST) via an Azure Function, but can also be run manually via NewsArt.py.

Requires the following environment variables set or a .env file to be created at the root directory with the following:
```
OPENAI_API_KEY=<Your OpenAI Key>
INSTA_USER=<Your Instagram Username>
INSTA_PASSWORD=<Your Instagram Password>
```

# Kids Art - AI Powered Instagram Account
This repo also includes another side project (KidsArt.py) which does the following:
  1. Comes up with a Dalle-prompt with the mind of a kid via ChatGPT 3.5 turbo
  2. Creates an image using that prompt via Dall-E 3
  3. Posts the image and prompt to Instagram

This is executed 1 time per day (12pm PST) via an Azure Function, but can also be run manually via KidsArt.py.

Requires the following environment variables set or a .env file to be created at the root directory with the following:
```
OPENAI_API_KEY=<Your OpenAI Key>
KIDS_USER=<Your Instagram Username>
KIDS_PASSWORD=<Your Instagram Password>
```

# Setup
All dependent packages can be installed via:
```
pip install -r requirements.txt
```


