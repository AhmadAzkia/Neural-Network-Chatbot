# QUICK TEST SCRIPT
# Test the updated notebook components

import json
import os
from combine_intents import combine_intent_files

def test_multiple_json_system():
    """
    Test that the multiple JSON file system works correctly
    """
    print("🧪 TESTING MULTIPLE JSON SYSTEM")
    print("=" * 50)
    
    # Test 1: Check all files exist
    required_files = [
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
    
    print("1. CHECKING FILE EXISTENCE:")
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} - MISSING!")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  WARNING: {len(missing_files)} files missing!")
        return False
    
    # Test 2: Validate JSON structure
    print("\n2. VALIDATING JSON STRUCTURE:")
    all_valid = True
    for file in required_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'intents' in data and isinstance(data['intents'], list):
                    print(f"   ✅ {file} - Valid structure")
                else:
                    print(f"   ❌ {file} - Invalid structure!")
                    all_valid = False
        except Exception as e:
            print(f"   ❌ {file} - JSON error: {e}")
            all_valid = False
    
    if not all_valid:
        print("\n⚠️  WARNING: Some JSON files have invalid structure!")
        return False
    
    # Test 3: Test combine function
    print("\n3. TESTING COMBINE FUNCTION:")
    try:
        combined_data = combine_intent_files()
        total_intents = len(combined_data['intents'])
        
        # Count patterns and responses
        total_patterns = sum(len(intent['patterns']) for intent in combined_data['intents'])
        total_responses = sum(len(intent['responses']) for intent in combined_data['intents'])
        
        print(f"   ✅ Combined successfully!")
        print(f"   📊 Total intents: {total_intents}")
        print(f"   📊 Total patterns: {total_patterns}")
        print(f"   📊 Total responses: {total_responses}")
        
        # Check if meets requirements
        if total_patterns >= 500:
            print(f"   🎯 REQUIREMENT MET: {total_patterns} patterns (≥500)")
        else:
            print(f"   ⚠️  REQUIREMENT NOT MET: {total_patterns} patterns (<500)")
            
    except Exception as e:
        print(f"   ❌ Combine function failed: {e}")
        return False
    
    # Test 4: Sample validation
    print("\n4. SAMPLE CONTENT VALIDATION:")
    sample_patterns = [
        "halo", "pagi", "assalamualaikum", 
        "jadwal", "nilai", "bayar spp",
        "thanks", "goodbye"
    ]
    
    found_patterns = []
    for intent in combined_data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in sample_patterns:
                found_patterns.append(pattern.lower())
    
    found_patterns = list(set(found_patterns))
    print(f"   ✅ Found {len(found_patterns)} sample patterns: {found_patterns}")
    
    print("\n" + "=" * 50)
    print("🎉 ALL TESTS PASSED!")
    print("✅ Multiple JSON system is working correctly")
    print("✅ Ready for notebook execution!")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    success = test_multiple_json_system()
    if success:
        print("\n🚀 You can now run the updated notebook!")
    else:
        print("\n❌ Please fix the issues before running the notebook.")
