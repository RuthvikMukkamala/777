from pinecone import Pinecone, Index, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import TextNode
import fitz
import os

class DataIngestor:
    def __init__(self, index_name):
        self.name = index_name
        self.api_key = os.environ["PINECONE_API_KEY"]
        self.pc = Pinecone(api_key=self.api_key)

        if self.name not in self.pc.list_indexes().names():
            self.pc.create_index(
                index_name,
                dimension=1536,
                metric="euclidean",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
        self.pinecone_index = self.pc.Index(index_name)

    def data_ingestor_pipeline(self, file_path):
        doc = fitz.open(file_path)

        text_parser = SentenceSplitter(
            chunk_size=1024,
            # separator=" ",
        )

        text_chunks = []
        doc_idxs = []
        for doc_idx, page in enumerate(doc):
            page_text = page.get_text("text")
            cur_text_chunks = text_parser.split_text(page_text)
            text_chunks.extend(cur_text_chunks)
            doc_idxs.extend([doc_idx] * len(cur_text_chunks))


