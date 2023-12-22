This Python program does the following:
  1. Fetches the top 10 articles from Google News
  2. Chooses an article at random
  3. Creates a summary of that article via ChatGPT 3.5 turbo
  4. Creates an artistic representation of the article based on the summary via Dall-E
  5. Creates a caption for the art piece via ChatGPT 3.5 turbo
  6. Posts the image and caption to Instagram

This is executed 3 times per day (6am, 12pm, and 6pm PST) via an Azure Function, but can also be run manually via NewsArt.py.

Requires a .env file to be created at the root directory with the following:
```
OPENAI_API_KEY=<Your OpenAI Key>
INSTA_USER=<Your Instagram Username>
INSTA_PASSWORD=<Your Instagram Password>
```

All dependent packages can be installed via:
```
pip install -r requirements.txt
```
