from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(
    title="Sentiment Analysis Service",
    description="MicroServe Innovations - ML Sentiment Analysis API",
    version="1.0.0"
)

class TextInput(BaseModel):
    text: str

class SentimentOutput(BaseModel):
    text: str
    sentiment: str
    confidence: float
    service: str
    version: str

@app.get("/")
def read_root():
    return {
        "service": "sentiment-service",
        "version": "1.0.0",
        "status": "running",
        "description": "Sentiment Analysis API for MicroServe Innovations"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "sentiment-service"}

@app.post("/predict")
def predict_sentiment(input_data: TextInput) -> SentimentOutput:
    """
    Analyze the sentiment of input text.
    Returns: positive, negative, or neutral sentiment with confidence score.
    """
    text = input_data.text.lower()

    # Simple sentiment analysis (for demo purposes)
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'love', 'best', 'happy']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'worst', 'poor', 'sad', 'disappointing']

    positive_count = sum(1 for word in positive_words if word in text)
    negative_count = sum(1 for word in negative_words if word in text)

    if positive_count > negative_count:
        sentiment = "positive"
        confidence = min(0.95, 0.6 + (positive_count * 0.1))
    elif negative_count > positive_count:
        sentiment = "negative"
        confidence = min(0.95, 0.6 + (negative_count * 0.1))
    else:
        sentiment = "neutral"
        confidence = 0.5 + random.uniform(0, 0.2)

    return SentimentOutput(
        text=input_data.text,
        sentiment=sentiment,
        confidence=round(confidence, 2),
        service="sentiment-service",
        version="1.0.0"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
















from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(
    title="Spam Detection Service",
    description="MicroServe Innovations - ML Spam Detection API",
    version="1.0.0"
)

class MessageInput(BaseModel):
    message: str

class SpamOutput(BaseModel):
    message: str
    is_spam: bool
    confidence: float
    service: str
    version: str

@app.get("/")
def read_root():
    return {
        "service": "spam-service",
        "version": "1.0.0",
        "status": "running",
        "description": "Spam Detection API for MicroServe Innovations"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "spam-service"}

@app.post("/predict")
def detect_spam(input_data: MessageInput) -> SpamOutput:
    """
    Detect if a message is spam or not.
    Returns: spam classification with confidence score.
    """
    message = input_data.message.lower()

    # Simple spam detection (for demo purposes)
    spam_keywords = [
        'winner', 'free', 'click here', 'congratulations', 'prize',
        'urgent', 'act now', 'limited time', 'offer', 'discount',
        'buy now', 'cash', 'credit card', 'guarantee'
    ]

    spam_count = sum(1 for keyword in spam_keywords if keyword in message)

    if spam_count >= 2:
        is_spam = True
        confidence = min(0.95, 0.65 + (spam_count * 0.1))
    elif spam_count == 1:
        is_spam = random.choice([True, False])
        confidence = 0.5 + random.uniform(0, 0.2)
    else:
        is_spam = False
        confidence = 0.7 + random.uniform(0, 0.25)

    return SpamOutput(
        message=input_data.message,
        is_spam=is_spam,
        confidence=round(confidence, 2),
        service="spam-service",
        version="1.0.0"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
