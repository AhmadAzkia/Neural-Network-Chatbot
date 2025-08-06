# JSON FILES COMBINATION SCRIPT
# Script untuk menggabungkan multiple JSON files untuk training

import json
import os

def combine_intent_files():
    """
    Menggabungkan semua file intents_*.json menjadi satu struktur
    untuk training neural network
    """
    combined_intents = {"intents": []}
    
    # List semua file intent JSON
    intent_files = [
        'intents_greeting.json',
        'intents_courses.json', 
        'intents_grades.json',
        'intents_finance.json',
        'intents_campus.json',
        'intents_graduation.json',
        'intents_closing.json',
        'intents_academic.json',
        'intents_general.json'
    ]
    
    print("🔄 Combining multiple JSON files...")
    
    for file_name in intent_files:
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                combined_intents["intents"].extend(data["intents"])
                print(f"✅ Loaded: {file_name} - {len(data['intents'])} intents")
        else:
            print(f"⚠️  File not found: {file_name}")
    
    print(f"\n📊 Total combined intents: {len(combined_intents['intents'])}")
    
    # Hitung total patterns dan responses
    total_patterns = sum(len(intent['patterns']) for intent in combined_intents['intents'])
    total_responses = sum(len(intent['responses']) for intent in combined_intents['intents'])
    
    print(f"📈 Total patterns: {total_patterns}")
    print(f"💬 Total responses: {total_responses}")
    
    return combined_intents

# Test the combination
if __name__ == "__main__":
    combined_data = combine_intent_files()
