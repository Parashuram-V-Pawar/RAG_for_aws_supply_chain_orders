import logging
from src.rag_pipeline import rag_pipeline

logging.basicConfig(level=logging.INFO)

logging.info("Starting RAG pipeline...")
rag_pipeline()
logging.info("RAG pipeline terminated.")
