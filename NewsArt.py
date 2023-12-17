from openai import OpenAI
from gnews import GNews
from instagrapi import Client
import random
import base64

print("Fetching top news article...\n")
google_news = GNews(language='en', country='US',period='1d', max_results=10)
google_news.exclude_websites = ['reuters.com']
top_news = google_news.get_top_news()

chosen_news = random.choice(top_news)

article = google_news.get_full_article(chosen_news['url'])
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
  response_format="b64_json",
  n=1,
)


image_b64 = picture_response.data[0].b64_json
image_filename = "instapost.jpg"

with open(image_filename, "wb") as fh:
    fh.write(base64.b64decode(image_b64))

revised_prompt = picture_response.data[0].revised_prompt

text_prompt = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You run an Instagram account for news inspired artwork."},
    {"role": "user", "content": """Provide a short and engaging Instagram post caption for 
     artwork created by the following prompt about a current event. Be sure to include hashtags, 
     include the art style used, and reference the news event itself. Do not mention the artists
     name in the caption.\n"""+revised_prompt}
  ]
)

post_caption = text_prompt.choices[0].message.content
post_caption = post_caption[1:-1]
post_caption += "\n\nInspired by latest top world news: " + article_title
print (post_caption +"\n")

#Post on Insta
cl = Client()
cl.login("NewsByArt", "n3w5@rt")

media = cl.photo_upload(path=image_filename, caption=post_caption)