from openai import OpenAI
from gnews import GNews
import random
import os


print("Fetching top news article...\n")
google_news = GNews(language='en', country='US',period='1d', max_results=1)
google_news.exclude_websites = ['reuters.com']
top_news = google_news.get_top_news()
article = google_news.get_full_article(top_news[0]['url'])
article_title = article.title
article_text = article.text
article_prompt = article.title + "/n" + article.text
article_prompt = article_prompt[:3900]

#Build Content
client=OpenAI(api_key="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")


print("Preparing Insta post for: " + article_title + "...\n")

art_prompt = "Create an artistic rendition of the following news article in an art style chosen at random.\n"
art_prompt += article_prompt

picture_response = client.images.generate(
  model="dall-e-3",
  prompt=art_prompt,
  size="1024x1024",
  quality="hd",
  n=1,
)

image_url = picture_response.data[0].url
revised_prompt = picture_response.data[0].revised_prompt

print(image_url)
print ("\n")

text_prompt = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You run an Instagram account for news inspired artwork."},
    {"role": "user", "content": """Provide a short and engaging Instagram post caption for 
     artwork created by the following prompt about a current event. Be sure to include hashtags, 
     include the art style used, and reference the news event itself.\n"""+revised_prompt}
  ]
)
print (text_prompt.choices[0].message.content +"\n")