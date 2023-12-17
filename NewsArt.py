from newsapi import NewsApiClient
from openai import OpenAI
from gnews import GNews
import random
import os

'''
# Get News Article
newsapi = NewsApiClient(api_key='b27c3ac5f9d0475881c77344d879f82e')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(sources='associated-press', page_size=10)

#top_article = top_headlines["articles"][0]
top_article = random.choice(top_headlines["articles"])
article_title = top_article["title"]
article_description = top_article["description"]
article_content = top_article["content"]

#print (article_title)
#print (article_description)
#print (article_content)
'''

print("Fetching top news article...\n")
google_news = GNews(language='en', country='US',period='1d', max_results=1)
top_news = google_news.get_top_news()
article = google_news.get_full_article(top_news[0]['url'])
article_title = article.title
article_text = article.text
article_prompt = article.title + "/n" + article.text
article_prompt = article_prompt[:3900]


#Build Content
client=OpenAI(api_key="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")


print("Preparing Insta post for: " + article_title + "...\n")

'''
article_summary = "This is the title of the news article: " + article_title
article_summary += "\nThis is the description of the news article: " + article_description

text_prompt = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You run an Instagram account for news inspired artwork."},
    {"role": "user", "content": """Provide an short and engaging Instagram post caption for a 
     piece of art inspired by the following news article title and description. Be sure to include hashtags and reference the news event itself. Don't 
     add text to say who created the artwork.\n"""+article_summary}
  ]
)
print (text_prompt.choices[0].message.content)

art_prompt = """Create an artistic representation in a random art style for the following news article. Don't include text in the art piece. 
If the title or description is not appropriate for your content filters, make the text less offensive by 
explaining the subject in a more wholesome way."""
art_prompt += "\n"+article_summary
'''

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