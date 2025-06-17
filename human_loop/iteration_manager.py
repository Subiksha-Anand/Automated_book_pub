def human_iteration_loop(text):
    print("\n🔍 AI Output:\n")
    print(text)
    
    while True:
        user_input = input("\nEnter your edits or type 'skip' to finalize: ")
        if user_input.strip().lower() == 'skip':
            break
        else:
            text = user_input  # In real UI, this would be a text box input
    
    return text
