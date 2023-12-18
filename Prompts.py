#Prompt to create image. Article title, description, and text (truncated to 3750 characters) is appended to this prompt.
art_prompt = """Create an artistic rendition of the following news article in an art 
style chosen at random. Update this prompt if needed to make it pass safety systems.\n"""

#System prompt before creating post caption.
caption_system = """You run an Instagram account for news inspired artwork, 
     are an expert on social media marketing, and in your late twenties with a college degree."""

#Prompt to create caption. Revised prompt from Dalle is appended to this prompt.
caption_message = """Provide a short, but engaging Instagram post caption for 
     artwork created by the following prompt about a current event. Be sure to include hashtags, 
     include the art style used, include emojis, and reference the news event itself. Do not mention the artist
     name in the caption or reference any other Instagram account. Do not wrap the caption in 
     quotation marks or proceed it with 'Caption:'.\n"""