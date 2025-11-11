#from fastapi import FastAPI, Request
#from transformers import pipeline

#app = FastAPI()
#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#@app.post("/summarize")
#async def summarize(request: Request):
#    data = await request.json()
#    text = data.get("text", "")
#    result = summarizer(text, max_length=120, min_length=30, do_sample=False)
#    return {"summary": result[0]["summary_text"]}


from fastapi import FastAPI

app = FastAPI(title="RLHF News Summarization System")

@app.get("/health")
def health():
    """
    Health check endpoint for Sprint 0 verification.
    Returns HTTP 200 if the API is up.
    """
    return {"status": "ok", "message": "FastAPI backend is live"}

@app.get("/")
def root():
    return {"message": "Welcome to RLHF News Summarization API 🚀"}
