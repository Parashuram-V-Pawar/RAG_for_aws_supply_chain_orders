import logging
from src.load_and_clean_data import *
from src.embedder import *
from src.vector_store import *
from src.generator import *

logging.basicConfig(level=logging.INFO)

def rag_pipeline():
    logging.info("Data cleaning initiated...")
    d = DataProcesser("data/aws_supply_chain_orders_raw.csv")
    d.load_data()
    df = d.clean_data()
    logging.info("Data cleaning completed...")

    logging.info("Text conversion initiated...")
    t = TextConvertor(df)
    full_df = t.convert()
    logging.info("Text conversion completed...")

    logging.info("Building vector store...")
    v = VectorStore()
    embeddings = v.create_embeddings(full_df['text'].tolist())
    v.build_index(embeddings)
    logging.info("Vector store built successfully...")

    logging.info("RAG system is ready to accept queries...")
    generator = Generator()
    while True:
        query = input("\nEnter query (type 'exit' to quit): ")

        if query.lower() == "exit":
            logging.info("Exiting RAG system...")
            break

        indices = v.search(query, k=10)
        results = full_df.iloc[indices[0]]
        if indices is None or len(indices[0]) == 0:
            print("No relevant data found.")
            continue

        answer = generator.generate(query, results)

        print("\nResponse:\n")
        print(answer)