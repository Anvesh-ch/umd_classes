-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Create table for document embeddings
CREATE TABLE IF NOT EXISTS documents (
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT,
  embedding vector(384),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Optional feedback table for RLHF
CREATE TABLE IF NOT EXISTS feedback (
  id SERIAL PRIMARY KEY,
  prompt TEXT,
  summary TEXT,
  rating INT,
  created_at TIMESTAMP DEFAULT NOW()
);