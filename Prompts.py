#Prompt to create image. Article title, description, and text (truncated to 3750 characters) is appended to this prompt.
art_prompt = """Create a painting for the following news article in any art style. If the article is inappropriate, 
make it appropriate enough for Dall-E. Use as much of the following detail as possible. Don’t use text.\n"""

#System prompt before creating post caption.
caption_system = """You run an Instagram account for news inspired artwork, 
     are an expert on social media marketing, and in your late twenties with a college degree."""

#Prompt to create caption. Revised prompt from Dalle is appended to this prompt.
caption_message = """Provide a short, but engaging Instagram post caption for 
     artwork created by the following prompt about a current event. Be sure to include hashtags, 
     include the art style used, include emojis, and reference the news event itself. Do not mention the artist
     name or say who the art is by in the caption. Do not mention any other Instagram account. Do not wrap the caption in 
     quotation marks or proceed it with 'Caption:'.\n"""