import chromadb

client = chromadb.PersistentClient(path="chromadb/")
collection = client.get_or_create_collection(name="book_versions")

def save_version(text, metadata):
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[metadata["version_id"]]
    )

def search_version(query):
    results = collection.query(query_texts=[query], n_results=1)
    return results

