from openai import OpenAI
from gnews import GNews
from instagrapi import Client
from dotenv import load_dotenv

import random
import base64
import os
import Prompts
import tempfile

def makeNewsArt():
  #OpenAI API Key and Insta creds need to be stored in .env file
  load_dotenv()
  OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
  INSTA_USER = os.environ.get("INSTA_USER")
  INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD")

  #Get The Article
  print("Fetching top news article...\n")
  google_news = GNews(language='en', period='1d', max_results=10)
  google_news.exclude_websites = ['reuters.com','thehill.com']
  top_news = google_news.get_top_news()

  chosen_news = random.choice(top_news)

  article = google_news.get_full_article(chosen_news['url'])
  article_title = article.title
  article_desc = chosen_news['description']
  article_text = article.text
  article_prompt = article.title + "/n" + article_desc + "/n" + article.text
  article_prompt = article_prompt[:3750]

  #Create Image Based on Article
  client=OpenAI(api_key=OPENAI_API_KEY)

  print("Preparing Insta post for: " + article_title + "...\n")

  art_prompt = Prompts.art_prompt
  art_prompt += article_prompt

  picture_response = client.images.generate(
    model="dall-e-3",
    prompt=art_prompt,
    size="1024x1024",
    quality="hd",
    response_format="b64_json",
    n=1,
  )


  image_b64 = picture_response.data[0].b64_json
  image_filename = os.path.join(tempfile.gettempdir(),"instapost.jpg")

  with open(image_filename, "wb") as fh:
      fh.write(base64.b64decode(image_b64))

  revised_prompt = picture_response.data[0].revised_prompt

  #Create Caption for Post
  text_prompt = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": Prompts.caption_system},
      {"role": "user", "content": Prompts.caption_message+revised_prompt}
    ]
  )

  post_caption = "\U0001f5BC  Inspired by latest top news: " + article_title + "\n\n"
  post_caption += text_prompt.choices[0].message.content

  print (post_caption.encode("utf-8"))

  #Post on Insta
  cl = Client()
  cl.login(INSTA_USER, INSTA_PASSWORD)
  media = cl.photo_upload(path=image_filename, caption=post_caption)

  #Clean Up Image File
  os.remove(image_filename)

if __name__ == '__main__': 
  makeNewsArt() 