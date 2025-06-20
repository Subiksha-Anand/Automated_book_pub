from scraping.fetch_and_screenshot import fetch_and_screenshot
from ai_pipeline.ai_writer import spin_chapter
from ai_pipeline.ai_reviewer import review_chapter
from human_loop.iteration_manager import human_iteration_loop
from storage.chromadb_handler import save_version, search_version
from utils.rl_search import rl_ranked_search
import uuid



def run_pipeline():
    print("\n Step 1: Fetching original chapter...")
    content = fetch_and_screenshot("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

    
    print("\n Step 2: Rewriting with AI Writer...")
    rewritten = spin_chapter(content)

    print("\n Step 3: Reviewing with AI Reviewer...")
    reviewed = review_chapter(rewritten)

    print("\n Step 4: Human-in-the-loop Editing...")
    final_text = human_iteration_loop(reviewed)

    print("\n Step 5: Saving final version to ChromaDB...")
    version_id = f"chapter1_{uuid.uuid4().hex[:8]}"
    save_version(final_text, metadata={"version_id": version_id, "score": 0.9})
    
    print(f"\n Final version saved as {version_id}")

    print("\n Step 6: Retrieving saved version...")
    results = search_version("chapter 1 gates of morning")
    query = "Chapter 1: The Gates of Morning"
    best_match = rl_ranked_search(query, results)

    print(" Final Chapter Output:")
    final_version = final_text
    print(final_version) 

    
    print("\n Retrieved Content:\n")
    print(best_match)

if __name__ == "__main__":
    run_pipeline()
