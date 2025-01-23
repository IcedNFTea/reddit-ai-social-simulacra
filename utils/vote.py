from utils import constant #yeah maybe not the best way to do this

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using OpenAI API.
    Returns 'up', 'down', or 'none' based on the sentiment.
    """
    try:
        # Analyze sentiment using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4o-2024-11-20",  # just using the same one for consistency
            messages=[
                {"role": "system", "content": "You are an AI that analyzes sentiment for Reddit posts and comments."},
                {"role": "user", "content": f"Analyze the sentiment of the following text and return 'positive', 'negative', or 'neutral':\n\n{text}\n\nSentiment:"}
            ],
            max_tokens=10,
            temperature=0
        )

        # Extract the sentiment from the response
        sentiment = response.choices[0].message.content.strip().lower()

        if sentiment == 'positive':
            return 'up'
        elif sentiment == 'negative':
            return 'down'
        else:
            return 'none'

    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'none'

def vote_post(post):
    try:
        sentiment = analyze_sentiment(post.content)  
        if sentiment == 'up':
            post.upvote()
            print(f"Upvoted post: {post.id}")
        elif sentiment == 'down':
            post.downvote()
            print(f"Downvoted post: {post.id}")
        else:
            print(f"No vote cast for post: {post.id}")
    except Exception as e:
        print(f"Error voting on post: {e}")

def vote_comment(comment):
    try:
        sentiment = analyze_sentiment(comment.content)
        if sentiment == 'up':
            comment.upvote()
            print(f"Upvoted comment: {comment.id}")
        elif sentiment == 'down':
            comment.downvote()
            print(f"Downvoted comment: {comment.id}")
        else:
            print(f"No vote cast for comment: {comment.id}")
    except Exception as e:
        print(f"Error voting on comment: {e}")
